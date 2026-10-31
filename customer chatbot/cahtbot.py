import re
import json
from datetime import datetime

# ==========================================
# RULE-BASED CUSTOMER SUPPORT CHATBOT
# ==========================================

BOT_NAME = "DathBot"

# FAQ dataset
FAQ_DATA = {
    "business_hours": {
        "keywords": [
            "business hours", "working hours", "opening hours",
            "open", "close", "timings", "time"
        ],
        "response": (
            "Our business hours are Monday to Saturday, "
            "9:00 AM to 6:00 PM."
        )
    },
    "products": {
        "keywords": [
            "product", "products", "item", "items",
            "catalog", "available", "services"
        ],
        "response": (
            "We offer a range of products and services. "
            "Please specify the product you are interested in."
        )
    },
    "pricing": {
        "keywords": [
            "price", "cost", "pricing", "rate", "charges"
        ],
        "response": (
            "Prices depend on the product. Please provide "
            "the product name to get pricing information."
        )
    },
    "delivery": {
        "keywords": [
            "delivery", "shipping", "dispatch", "tracking"
        ],
        "response": (
            "Delivery time depends on your location and product. "
            "Please check your order confirmation for tracking details."
        )
    },
    "returns": {
        "keywords": [
            "return", "refund", "exchange", "replacement"
        ],
        "response": (
            "For returns or refunds, please keep your receipt "
            "and contact our customer support team."
        )
    },
    "contact": {
        "keywords": [
            "contact", "support", "help", "customer care",
            "phone number", "email"
        ],
        "response": (
            "You can contact the customer support team through "
            "the official website's contact page."
        )
    },
    "thanks": {
        "keywords": [
            "thanks", "thank you", "thankyou"
        ],
        "response": "You're welcome! I'm happy to help."
    }
}

# Save FAQ data as a JSON file
def save_faq_data():
    try:
        with open("faq_dataset.json", "w", encoding="utf-8") as file:
            json.dump(FAQ_DATA, file, indent=4)
    except OSError as error:
        print(f"Warning: Could not save FAQ data: {error}")


# Load FAQ data from JSON when available
def load_faq_data():
    try:
        with open("faq_dataset.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("FAQ data must be a JSON object.")

        return data

    except FileNotFoundError:
        save_faq_data()
        return FAQ_DATA

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Warning: Using built-in FAQs. {error}")
        return FAQ_DATA


# Normalize input
def normalize_input(user_input):
    user_input = user_input.lower().strip()
    user_input = re.sub(r"\s+", " ", user_input)
    return user_input


# Check whether a keyword appears as a whole phrase
def contains_keyword(text, keyword):
    pattern = r"(?<!\w)" + re.escape(keyword.lower()) + r"(?!\w)"
    return re.search(pattern, text) is not None


# Identify all matching intents
def identify_intents(user_input, faq_data):
    text = normalize_input(user_input)
    intents = []

    # Greeting detection
    if re.search(
        r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b",
        text
    ):
        intents.append("greeting")

    # Business hours, products, pricing, and other FAQ intents
    for intent, details in faq_data.items():
        keywords = details.get("keywords", [])

        if not isinstance(keywords, list):
            continue

        if any(
            isinstance(keyword, str)
            and contains_keyword(text, keyword)
            for keyword in keywords
        ):
            intents.append(intent)

    # Goodbye detection
    if re.search(
        r"\b(bye|goodbye|exit|quit)\b",
        text
    ):
        intents.append("exit")

    # Remove duplicate intents while preserving order
    return list(dict.fromkeys(intents))


# Generate responses for identified intents
def generate_response(intents, faq_data):
    responses = []

    for intent in intents:
        if intent == "greeting":
            current_hour = datetime.now().hour

            if 5 <= current_hour < 12:
                greeting = "Good morning!"
            elif 12 <= current_hour < 17:
                greeting = "Good afternoon!"
            else:
                greeting = "Good evening!"

            responses.append(
                f"{greeting} I'm {BOT_NAME}, your customer support assistant."
            )

        elif intent == "exit":
            responses.append("Thank you for chatting with me. Goodbye!")

        elif intent in faq_data:
            response = faq_data[intent].get("response")

            if isinstance(response, str) and response.strip():
                responses.append(response)

    if responses:
        return "\n".join(responses)

    return (
        "Sorry, I couldn't understand your question. "
        "You can ask about business hours, products, pricing, "
        "delivery, returns, refunds, or customer support."
    )


# Main chatbot
def main():
    print("=" * 55)
    print(f"Welcome to {BOT_NAME}!")
    print("Your Rule-Based Customer Support Assistant")
    print("=" * 55)
    print("Type 'help' to see available topics.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print()

    faq_data = load_faq_data()

    # Conversation state
    conversation_state = "greeting"

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("Bot: Please enter a message.")
                continue

            # Help command
            if normalize_input(user_input) == "help":
                print(
                    "Bot: I can help with greetings, business hours, "
                    "products, pricing, delivery, returns, refunds, "
                    "and customer support."
                )
                continue

            # Identify intents
            intents = identify_intents(user_input, faq_data)

            # Update conversation state
            if "exit" in intents:
                conversation_state = "exit"
            elif intents:
                conversation_state = "resolution"
            else:
                conversation_state = "fallback"

            # Respond to all matched intents
            response = generate_response(intents, faq_data)
            print(f"Bot: {response}")

            # Exit cleanly
            if conversation_state == "exit":
                break

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat ended. Have a nice day!")
            break

        except Exception as error:
            # Prevent unexpected errors from crashing the chatbot
            print("Bot: Something went wrong. Please try again.")
            print(f"Debug information: {error}")


if __name__ == "__main__":
    main()
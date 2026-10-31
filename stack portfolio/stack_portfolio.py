import csv
import os
from datetime import datetime

# Stock Portfolio Performance Tracker
# Project: Datheon Task 2

PORTFOLIO_FILE = "portfolio.csv"
SUMMARY_FILE = "portfolio_summary.csv"

portfolio = {}


def display_heading():
    print("\n" + "=" * 65)
    print("          STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 65)


def get_positive_float(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Enter a valid number.")


def get_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a whole number.")


def add_stock():
    print("\n--- Add Stock ---")
    ticker = input("Enter stock ticker symbol: ").strip().upper()

    if not ticker or not ticker.isalnum():
        print("Invalid ticker symbol.")
        return

    buy_price = get_positive_float("Enter purchase price per share: ")
    shares = get_positive_int("Enter number of shares: ")
    current_price = get_positive_float("Enter current price per share: ")

    if ticker in portfolio:
        print("This stock already exists in your portfolio.")
        choice = input("Add to existing shares? (y/n): ").lower()

        if choice == "y":
            old = portfolio[ticker]
            total_shares = old["shares"] + shares
            total_cost = (
                old["buy_price"] * old["shares"]
                + buy_price * shares
            )
            old["buy_price"] = total_cost / total_shares
            old["shares"] = total_shares
            old["current_price"] = current_price
            print("Stock position updated successfully.")
        else:
            print("No changes made.")
            return
    else:
        portfolio[ticker] = {
            "buy_price": buy_price,
            "shares": shares,
            "current_price": current_price
        }
        print("Stock added successfully.")

    save_portfolio()


def update_price():
    print("\n--- Update Stock Price ---")
    ticker = input("Enter ticker symbol: ").strip().upper()

    if ticker not in portfolio:
        print("Stock not found in your portfolio.")
        return

    price = get_positive_float("Enter updated current price: ")
    portfolio[ticker]["current_price"] = price

    save_portfolio()
    print("Current price updated successfully.")


def calculate_stock(ticker, stock):
    buy_price = stock["buy_price"]
    shares = stock["shares"]
    current_price = stock["current_price"]

    invested = buy_price * shares
    market_value = current_price * shares
    gain_loss = market_value - invested

    if invested > 0:
        percentage = (gain_loss / invested) * 100
    else:
        percentage = 0

    return invested, market_value, gain_loss, percentage


def view_portfolio():
    print("\n--- Your Stock Portfolio ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("-" * 85)
    print(
        f"{'Ticker':<10}{'Shares':>8}{'Buy Price':>12}"
        f"{'Current':>12}{'Market Value':>16}"
    )
    print("-" * 85)

    for ticker, stock in portfolio.items():
        market_value = stock["current_price"] * stock["shares"]

        print(
            f"{ticker:<10}{stock['shares']:>8}"
            f"{stock['buy_price']:>12.2f}"
            f"{stock['current_price']:>12.2f}"
            f"{market_value:>16.2f}"
        )

    print("-" * 85)


def show_performance():
    print("\n--- Portfolio Performance Report ---")

    if not portfolio:
        print("No stocks available. Add stocks first.")
        return

    total_invested = 0.0
    total_market_value = 0.0

    print("-" * 100)
    print(
        f"{'Ticker':<10}{'Invested':>14}{'Market Value':>16}"
        f"{'Gain/Loss':>14}{'Return %':>12}"
    )
    print("-" * 100)

    for ticker, stock in portfolio.items():
        invested, market_value, gain_loss, percentage = (
            calculate_stock(ticker, stock)
        )

        total_invested += invested
        total_market_value += market_value

        print(
            f"{ticker:<10}{invested:>14.2f}"
            f"{market_value:>16.2f}"
            f"{gain_loss:>14.2f}{percentage:>11.2f}%"
        )

    total_gain_loss = total_market_value - total_invested
    total_return = (
        total_gain_loss / total_invested * 100
        if total_invested else 0
    )

    print("-" * 100)
    print(f"Total Investment:     {total_invested:.2f}")
    print(f"Current Market Value: {total_market_value:.2f}")
    print(f"Total Gain/Loss:      {total_gain_loss:.2f}")
    print(f"Portfolio Return:     {total_return:.2f}%")

    if total_gain_loss > 0:
        print("Overall Status: PROFIT")
    elif total_gain_loss < 0:
        print("Overall Status: LOSS")
    else:
        print("Overall Status: BREAK-EVEN")


def save_portfolio():
    try:
        with open(PORTFOLIO_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Ticker", "Buy Price", "Shares", "Current Price"
            ])

            for ticker, stock in portfolio.items():
                writer.writerow([
                    ticker,
                    stock["buy_price"],
                    stock["shares"],
                    stock["current_price"]
                ])

        print("Portfolio data saved.")
    except OSError as error:
        print("Could not save portfolio:", error)


def load_portfolio():
    if not os.path.exists(PORTFOLIO_FILE):
        return

    try:
        with open(PORTFOLIO_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                ticker = row["Ticker"].strip().upper()

                portfolio[ticker] = {
                    "buy_price": float(row["Buy Price"]),
                    "shares": int(row["Shares"]),
                    "current_price": float(row["Current Price"])
                }

        print("Previous portfolio data loaded.")
    except (OSError, ValueError, KeyError) as error:
        print("Could not load portfolio:", error)


def export_summary():
    if not portfolio:
        print("No stocks available to export.")
        return

    try:
        with open(SUMMARY_FILE, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Report Date", "Ticker", "Buy Price", "Shares",
                "Current Price", "Invested Amount", "Market Value",
                "Gain/Loss", "Gain/Loss Percentage"
            ])

            report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for ticker, stock in portfolio.items():
                invested, market_value, gain_loss, percentage = (
                    calculate_stock(ticker, stock)
                )

                writer.writerow([
                    report_date,
                    ticker,
                    stock["buy_price"],
                    stock["shares"],
                    stock["current_price"],
                    invested,
                    market_value,
                    gain_loss,
                    round(percentage, 2)
                ])

        print(f"Summary exported to {SUMMARY_FILE}.")
    except OSError as error:
        print("Could not export summary:", error)


def remove_stock():
    ticker = input("Enter ticker to remove: ").strip().upper()

    if ticker in portfolio:
        del portfolio[ticker]
        save_portfolio()
        print("Stock removed successfully.")
    else:
        print("Stock not found.")


def show_menu():
    print("\n1. Add Stock")
    print("2. Update Current Stock Price")
    print("3. View Portfolio")
    print("4. Calculate Performance")
    print("5. Export Summary to CSV")
    print("6. Remove Stock")
    print("7. Save Portfolio")
    print("8. Exit")
    print("-" * 40)


def main():
    load_portfolio()

    while True:
        display_heading()
        show_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            update_price()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            show_performance()
        elif choice == "5":
            export_summary()
        elif choice == "6":
            remove_stock()
        elif choice == "7":
            save_portfolio()
        elif choice == "8":
            save_portfolio()
            print("Thank you for using the tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()
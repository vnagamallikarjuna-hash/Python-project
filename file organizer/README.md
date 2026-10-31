# 📁 File Organizer Automation Using Python

## 📌 Project Overview

File Organizer Automation is a Python-based project that automatically organizes files in a selected folder into different categories based on their file extensions.

The program identifies different file types and moves them into separate folders such as Documents, Images, Videos, Audio, Archives, Code, Installers, and Others.

It uses Python libraries like `os`, `shutil`, `logging`, `pathlib`, and `datetime` to manage files, create folders, move files, prevent duplicate filenames, and maintain activity logs.

This project helps reduce manual file management and keeps folders clean, organized, and easy to access.

## 🎯 Objectives

- To automate file organization using Python.
- To categorize files based on their extensions.
- To reduce manual file management.
- To understand file and folder operations.
- To implement error handling and logging.
- To prevent overwriting files with duplicate names.

## ✨ Features

- **Automatic File Sorting:** Organizes files based on their extensions.
- **Category-Based Organization:** Separates files into different folders.
- **Automatic Folder Creation:** Creates category folders automatically.
- **Duplicate File Handling:** Prevents overwriting files with the same name.
- **Error Handling:** Handles file operation errors.
- **Activity Logging:** Records file movements and errors in `organizer.log`.
- **Final Report:** Displays successfully moved, failed, and skipped files.
- **User Input:** Allows users to select a folder for organization.

## 📂 File Categories

The project organizes files into the following categories:

| Category | File Extensions |
|---|---|
| Documents | PDF, DOC, DOCX, TXT, PPT, XLS, CSV |
| Images | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG |
| Videos | MP4, MKV, AVI, MOV, WMV |
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JAVA, C, CPP, HTML, CSS, JS, PHP, SQL |
| Installers | EXE, MSI, APK, DEB |
| Others | All other file types |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **OS:** File system operations
- **Shutil:** Moving files
- **Logging:** Maintaining activity records
- **Pathlib:** Managing file paths
- **Datetime:** Displaying completion date and time
- **Platform:** Visual Studio Code

## 📁 Project Structure

```text
File-Organizer/
│
├── file_organizer.py
├── organizer.log
└── README.md
```

**Note:** The `organizer.log` file is generated automatically when the program runs.

## ⚙️ How to Run the Project

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Run the Program

Open the terminal and execute:

```bash
python file_organizer.py
```

### Step 4: Enter Folder Path

The program asks you to enter the folder path you want to organize.

Example:

```text
Enter the folder path to organize:
C:\Users\YourName\Downloads
```

### Step 5: Automatic Organization

The program automatically:
- Scans the selected folder.
- Identifies file extensions.
- Creates category folders.
- Moves files into the correct folders.
- Generates an organization report.

## 💡 Python Concepts Used

1. Variables and Data Types
2. Functions
3. Dictionaries and Lists
4. Conditional Statements
5. Loops
6. File Handling
7. Exception Handling
8. File and Folder Management
9. Logging
10. Path Manipulation
11. Modules and Libraries

## 📊 Final Output Report

After organizing files, the program displays:

```text
========================================
       FILE ORGANIZATION REPORT
========================================
Files moved successfully : 15
Files failed             : 0
Items skipped            : 2
Completed at             : Date and Time
Log file                 : organizer.log
========================================
```

*Note: The numbers shown above are sample values.*

## 🚀 Future Enhancements

- Develop a graphical user interface (GUI).
- Add custom file categories.
- Implement an undo option.
- Schedule automatic file organization.
- Add file preview functionality.
- Support additional file extensions.

## 🎓 Project Information

**Project Name:** File Organizer Automation Using Python

**Project Type:** Python Mini Project

**Domain:** Python Automation and File Management

**Programming Language:** Python

**Author:** Nagamallikarjuna Veeramreddy

## 📜 License

This project is developed for educational and learning purposes.

---

⭐ If you find this project useful, feel free to explore and improve it!

# SmartLog Analytics System

## Project Title
SmartLog Analytics System

## Overview of the Project
The SmartLog Analytics System is a text-processing command-line application designed using core Python programming concepts. Built as part of the VITyarthi Python Essentials flipped course evaluation, this application serves as a structural text validation and data analyzer. It processes raw string streams or system logs, cleans out format irregularities, extracts linguistic counts, and provides a clear statistical distribution summary directly on the user's terminal console without encountering system crashes.

---

## Features
* **Module 1 (Data Ingestion & Sanitation):** Validates the incoming string payload to ensure it is not blank, strips extra whitespaces, and normalizes line breaks safely.
* **Module 2 (Linguistic Analytics Engine):** Implements a single-pass loop traversal to calculate character distributions, word masses, vowel counts, and unique vocabulary sizes.
* **Module 3 (Statistical Reporting Dashboard):** Computes an alphanumeric frequency mapping array and presents the top five highest-occurring text characters in a formatted terminal table.
* **Fault-Tolerant Exception Handling:** Employs built-in try-except blocks to catch empty inputs or unexpected execution issues gracefully instead of crashing the program window.

---

## Technologies and Tools Used
* **Programming Language:** Python 3.x
* **Core Concepts Applied:** Object-Oriented Programming (Classes and Methods), Data Structures (Dictionaries, Sets, Lists), Control Flow Structures (Loops, Conditional Branches), String Manipulation, and Exception Handling.

---

## Steps to Install and Run the Project

### 1. Prerequisites
Ensure that Python 3 is installed on your computer. You can check your current Python installation by opening up your terminal or command prompt and running:
```bash
python --version
```

### 2. Workspace Setup
Make sure your project folder contains your three essential required files organized like this:
```text
SmartLog-Analytics/
│
├── smartlog_analytics.py  (Main Codebase)
├── statement.md           (Problem Statement Document)
└── README.md              (System Guide Documentation)
```

### 3. Executing the Program
Navigate into your workspace directory using your terminal window and launch the script with the standard Python execution command:
```bash
python smartlog_analytics.py
```

---

## Instructions for Testing

1. Execute the system using the command line shown in the step above.
2. The interactive interface will prompt you to enter or paste your sample text lines or system logs.
3. Paste any raw paragraph block or system logs into the window.
4. To signal that you are done pasting and want to process the results, hit the Enter key to move to a clean line, then press the End-of-File (EOF) command for your operating system:
   * **Windows Terminal Users:** Press `Ctrl + Z` and then hit `Enter`.
   * **Mac or Linux Terminal Users:** Press `Ctrl + D`.
5. Observe the operational `[INFO]` status tracks and review the final analytical summary table printed on your console.

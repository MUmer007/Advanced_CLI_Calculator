# Advanced_CLI_Calculator
Advanced Python Calculator with History
📖 Overview

This project is a command-line based Advanced Calculator built using Python.
It allows users to evaluate mathematical expressions, view past calculations, and manage calculation history using a text file.

The calculator supports basic and complex arithmetic expressions and stores results persistently for future reference.

🎯 Features

✅ Evaluate mathematical expressions (e.g., 2 + 3 * 4)

✅ Automatically saves calculation history

✅ View previous calculations

✅ Clear calculation history

✅ Handles division by zero errors

✅ Simple and user-friendly CLI interface

✅ Persistent storage using a text file

🧠 Concepts Used

File Handling (read, write, append)

Exception Handling (try-except)

Functions & modular programming

Loops and conditionals

String manipulation

Safe evaluation of expressions

Command-line interaction

📂 Project Structure
📁 advanced-calculator
 ├── calculator.py
 ├── history.txt
 └── README.md


calculator.py → Main Python program

history.txt → Stores calculation history automatically

README.md → Project documentation

▶️ How to Run

Make sure Python 3 is installed.

Open terminal or command prompt.

Navigate to the project directory.

Run the program:

python calculator.py

🖥 Usage Instructions

After running the program, you will see:

--- Advanced Calculator ---
Type a math expression (e.g., 2 + 3 * 4)

Commands:
  history - View history
  clear   - Clear history
  exit    - Quit

🔹 Examples

Calculate:

>> 5 * (3 + 2)
Result: 25


View history:

>> history


Clear history:

>> clear
History cleared.


Exit:

>> exit

📌 Important Notes

History is saved in history.txt

Each calculation is stored as:

expression = result


Float results that are whole numbers are automatically converted to integers

Invalid expressions are handled gracefully

🔒 Safety

The calculator uses a restricted eval() environment to prevent access to Python built-in functions, making it safer for basic mathematical evaluation.

🧑‍💻 Author

Muhammad Umer 


🚀 Future Enhancements

Add scientific functions (sin, cos, log)

GUI version using Tkinter

Better expression validation

Export history to CSV or PDF

⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork it

🛠 Improve and experiment

📜 License

This project is intended for educational and learning purposes.
Free to use, modify, and share.

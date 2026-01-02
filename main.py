HISTORY_FILE = "history.txt"


def add_to_history(expression, result):
    """Save calculation to history file."""
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")


def show_history():
    """Display calculation history."""
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No history found.")
            return

        print("\n--- Calculation History ---")
        for line in reversed(lines):
            print(line.strip())
        print("----------------------------\n")

    except FileNotFoundError:
        print("No history file found.")


def clear_history():
    """Clear calculation history."""
    with open(HISTORY_FILE, "w"):
        pass
    print("History cleared.")


def calculate(expression):
    """Evaluate a mathematical expression safely."""
    try:
        # Evaluate expression
        result = eval(expression, {"__builtins__": None}, {})

        # Convert float integers to int
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print("Result:", result)
        add_to_history(expression, result)

    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception:
        print("Invalid expression. Try again.")


def main():
    print(
        "\n--- Advanced Calculator ---\n"
        "Type a math expression (e.g., 2 + 3 * 4)\n"
        "Commands:\n"
        "  history - View history\n"
        "  clear   - Clear history\n"
        "  exit    - Quit\n"
    )

    while True:
        user_input = input(">> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)


if __name__ == "__main__":
    main()

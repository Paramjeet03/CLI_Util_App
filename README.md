# Utility CLI App

A robust and beginner-friendly **Command Line Interface (CLI)** Python utility application designed to help users perform common mathematical operations and basic file handling directly from the terminal. This is a standalone utility app and is **separate from any quiz or game project**, but can be integrated.

---

## 🧰 Features

* **Prime Number Checker** – Verify if a number is prime.
* **Factorial Calculator** – Compute factorial of a given number.
* **Palindrome Checker** – Determine whether a string or number is a palindrome.
* **File Operations** – Read/write files with custom content.
* **Simple CLI Menu Navigation** – Intuitive numbered menu for operation selection.
* **Log Tracking** – Keeps log of operations performed (`app.log`).
* **Clean Modular Code** – Organized into reusable functions and methods.
* **Colorful Output** – Uses `colorama` for enhanced readability.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Utility_CLI_App.git
cd Utility_CLI_App
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

---

## 🗂️ Project Structure

```
Utility_CLI_App/
├── utils/
│   ├── math_utils.py         # Prime, factorial, palindrome
│   ├── file_utils.py         # File reading/writing
├── logs/
│   └── app.log               # Application logs
├── app.py                    # Main CLI logic
├── requirements.txt          # Required packages
└── README.md                 # Project documentation
```

---

## 📋 Sample Usage

### Main Menu:

```
Welcome to the Utility CLI App

1. 🔢 Check Prime
2. 🧮 Calculate Factorial
3. 🔁 Check Palindrome
4. 📁 File Operations
5. ❌ Exit
```

---

## 🧪 Code Examples

### Prime Checker:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

---

## 📦 Requirements

* Python 3.7+
* `colorama` – For colored CLI text
* `logging` – To keep runtime logs

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧑‍💻 Developer Notes

* Input is stripped and validated to prevent common errors.
* Easy to expand by adding new functions in `utils/` folder.
* Menu entries are loop-based and provide graceful exit options.

---

## 📌 To-Do / Future Enhancements

* Add temperature converter utility
* Add calculator for basic arithmetic
* Add datetime utilities (e.g. age calculator, date diff)
* Multi-language support

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 🙌 Contributing

Pull requests, bug reports, and suggestions are welcome! Fork the repository and help improve this CLI toolkit.

---

**Note:** This README is generated as part of the `docs` effort and should be included in the project root directory as `README.md`.

---

Crafted with ❤️ using Python.

# 🧠 Basic Programming Language Interpreter

> A custom programming language and interpreter built from scratch in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Interpreter](https://img.shields.io/badge/Project-Interpreter-8A2BE2?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📖 About the Project

This project is a **custom programming language interpreter** developed in Python.

The goal of the project is to understand how programming languages work internally by implementing the major stages of an interpreter:

```text
Source Code
     │
     ▼
   Lexer
     │
     ▼
   Tokens
     │
     ▼
   Parser
     │
     ▼
   AST
     │
     ▼
 Interpreter
     │
     ▼
 Runtime Values
     │
     ▼
   Output
```

Instead of executing Python syntax directly, the project defines its **own syntax, keywords, expressions, functions, loops, lists, operators, and built-in functions**.

---

## ✨ Features

### 🔤 Variables

Variables can be created using the `VAR` keyword.

```text
VAR x = 10
VAR name = "Danish"
```

### ➕ Arithmetic Operations

The language supports common arithmetic operations:

```text
VAR sum = 10 + 5
VAR difference = 10 - 5
VAR product = 10 * 5
VAR division = 10 / 5
VAR power = 2 ^ 3
```

### ⚖️ Comparison Operators

```text
x == 10
x != 5
x < 20
x > 5
x <= 10
x >= 10
```

### 🧠 Boolean Operations

```text
x AND y
x OR y
NOT x
```

The language also provides:

```text
TRUE
FALSE
NULL
```

---

## 🔀 Conditional Statements

The language supports conditional execution using `IF`, `ELIF`, `ELSE`, and `END`.

```text
IF x > 10 THEN
    PRINT("x is greater than 10")
ELIF x == 10 THEN
    PRINT("x is equal to 10")
ELSE
    PRINT("x is less than 10")
END
```

---

## 🔁 Loops

### FOR Loop

```text
FOR i = 0 TO 10 THEN
    PRINT(i)
END
```

### FOR Loop with STEP

```text
FOR i = 0 TO 10 STEP 2 THEN
    PRINT(i)
END
```

### WHILE Loop

```text
WHILE x < 10 THEN
    PRINT(x)
END
```

### Loop Control

The language provides:

```text
BREAK
CONTINUE
```

---

## 🧩 Functions

Functions can be defined with parameters.

### Single-expression Function

```text
FUNC add(a, b) -> a + b
```

Usage:

```text
PRINT(add(10, 20))
```

### Multiline Function

```text
FUNC square(x)
    RETURN x * x
END
```

Usage:

```text
VAR result = square(5)
PRINT(result)
```

The interpreter supports function calls, parameters, return values, function contexts, and local symbol tables.

---

## 📦 Lists

Lists can be created using square brackets:

```text
VAR numbers = [1, 2, 3, 4, 5]
```

Empty lists are also supported:

```text
VAR items = []
```

The interpreter contains runtime support for list operations and list indexing.

---

## 🛠️ Built-in Functions

The language provides several built-in functions.

| Function | Purpose |
|---|---|
| `PRINT()` | Prints a value |
| `PRINT_RET()` | Prints/returns a value |
| `INPUT()` | Reads user input |
| `INPUT_INT()` | Reads integer input |
| `CLEAR()` | Clears the screen |
| `CLS()` | Alias for `CLEAR()` |
| `IS_NUM()` | Checks whether a value is a number |
| `IS_STR()` | Checks whether a value is a string |
| `IS_LIST()` | Checks whether a value is a list |
| `IS_FUNC()` | Checks whether a value is a function |
| `APPEND()` | Adds an element to a list |
| `POP()` | Removes an element from a list |
| `EXTEND()` | Extends a list |
| `LEN()` | Returns the length of a list |
| `RUN()` | Runs another program/file |

Example:

```text
VAR numbers = [1, 2, 3]

APPEND(numbers, 4)

PRINT(numbers)
PRINT(LEN(numbers))
```

---

## 🔢 Built-in Constants

The global symbol table contains:

```text
NULL
TRUE
FALSE
MATH_PI
```

Example:

```text
PRINT(MATH_PI)
PRINT(TRUE)
```

---

## 🏗️ Project Architecture

The interpreter is divided into several logical components.

### 1. Lexer

The lexer reads the source code and converts it into tokens.

```text
Source Code
     ↓
Lexer
     ↓
Tokens
```

It recognizes things such as:

- Numbers
- Strings
- Identifiers
- Keywords
- Operators
- Parentheses
- Brackets
- New lines
- Comments

---

### 2. Parser

The parser receives the token stream and builds an **Abstract Syntax Tree (AST)**.

```text
Tokens
   ↓
Parser
   ↓
AST
```

The AST contains nodes representing:

- Numbers
- Strings
- Lists
- Binary operations
- Unary operations
- Variable access
- Variable assignment
- Conditionals
- Loops
- Functions
- Function calls
- Return statements
- Break/continue statements

---

### 3. Interpreter

The interpreter walks through the AST and executes the program.

```text
AST
 ↓
Interpreter
 ↓
Runtime Values
```

The interpreter contains visitors for different AST node types.

---

### 4. Runtime Values

The project defines its own runtime value system, including:

```text
Number
String
List
Function
BuiltInFunction
```

These values support operations appropriate to their types.

---

### 5. Context & Symbol Table

The interpreter uses contexts and symbol tables to manage variables and scopes.

Conceptually:

```text
Global Context
      │
      ├── Variables
      │
      └── Function Context
              │
              └── Local Variables
```

This allows functions to have their own execution context while still being able to access appropriate parent scopes.

---

## 📂 Suggested Project Structure

```text
Basic-Interpreter/
│
├── basic.py
├── string_with_arrows.py
├── README.md
└── examples/
    ├── hello.basic
    ├── variables.basic
    ├── conditions.basic
    ├── loops.basic
    ├── functions.basic
    └── lists.basic
```

> The exact structure may vary depending on how the project is organized locally.

---

## 🚀 Getting Started

### Prerequisites

You need:

- Python 3.x
- A terminal or command prompt
- The project files

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### Run the Interpreter

```bash
python basic.py
```

The exact entry point may depend on how the interpreter is being used in your project.

---

## 🧪 Example Program

A simple example combining several language features:

```text
VAR numbers = [1, 2, 3, 4, 5]

FUNC square(x) -> x * x

FOR i = 0 TO LEN(numbers) THEN
    PRINT(square(i))
END
```

Another example using conditions:

```text
VAR age = 20

IF age >= 18 THEN
    PRINT("Adult")
ELSE
    PRINT("Minor")
END
```

---

## 🧠 Error Handling

The interpreter includes custom error handling for different stages of execution.

Errors are handled during:

```text
Lexing
Parsing
Runtime Execution
```

This allows invalid programs to produce meaningful error information instead of simply crashing the interpreter.

---

## 🎯 Learning Objectives

This project is designed to provide practical understanding of:

- How lexers work
- Tokenization
- Parsing
- Grammar design
- Abstract Syntax Trees
- Recursive descent parsing
- Expression evaluation
- Runtime environments
- Variable scope
- Functions and function calls
- Built-in functions
- Runtime error handling
- Interpreter architecture

---

## 🛣️ Future Improvements

Possible future additions include:

- [ ] More data types
- [ ] Better error messages
- [ ] Improved string operations
- [ ] More list operations
- [ ] Dictionaries / maps
- [ ] `FOR EACH` loops
- [ ] More advanced function features
- [ ] Modules/import system
- [ ] File handling
- [ ] Standard library
- [ ] Interactive REPL improvements
- [ ] Syntax highlighting
- [ ] VS Code extension
- [ ] Automated test suite
- [ ] Better documentation
- [ ] Package/module management

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new language feature"
```

5. Push the branch

```bash
git push origin feature/my-feature
```

6. Open a Pull Request

---

## 📜 License

This project is available under the **MIT License**.

---

## 👨‍💻 Author

**Danish Khan**

B.Tech CSE • Aspiring Software Engineer

Interested in:

- 💻 Software Development
- 🧠 Data Structures & Algorithms
- 🤖 Artificial Intelligence
- 📱 Application Development
- 🐍 Python
- ⚙️ Programming Language Design

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

> **Built from scratch to understand how programming languages work under the hood.** 🚀

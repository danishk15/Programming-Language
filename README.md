<p align="center">
  <img src="assets/banner.png" alt="Quilhawk Banner" width="100%">
</p>

<h1 align="center">🚀 Quilhawk Programming Language</h1>

<p align="center">
A modern interpreted programming language built completely from scratch in Python.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Build](https://github.com/YOUR_USERNAME/quilhawk/actions/workflows/python-tests.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v0.1.0-orange?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-blue?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)

</p>

---

# 📖 Overview

Quilhawk is a lightweight interpreted programming language developed entirely in Python.

This project demonstrates the complete lifecycle of a programming language—from lexical analysis and parsing to Abstract Syntax Tree (AST) generation and runtime interpretation.

The goal of this project is to learn compiler and interpreter design while creating a modern, extensible programming language from scratch.

---

# 🎥 Demo

<p align="center">
<img src="assets/demo.gif" width="900">
</p>

---

# ✨ Features

- 🔤 Custom Lexer
- 🌳 Abstract Syntax Tree (AST)
- 🧠 Recursive Descent Parser
- ⚡ Interpreter
- 📦 Variables
- ➕ Arithmetic Expressions
- ⚖️ Comparison Operators
- 🔀 Boolean Logic
- 🌿 IF / ELIF / ELSE
- 📍 Detailed Error Messages
- 💻 Interactive REPL
- 🚀 Modular Architecture

---

# 🏗️ Project Structure

```text
.
├── .github
│   └── workflows
│       └── python-tests.yml
│
├── assets
│   ├── banner.png
│   ├── logo.png
│   └── demo.gif
│
├── basic.py
├── shell.py
├── grammar.txt
├── string_with_arrows.py
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Current Language Features

## Variables

```text
VAR x = 10
VAR y = 20
```

## Arithmetic

```text
10 + 5
20 - 10
8 * 4
100 / 5
2 ^ 8
```

## Comparison

```text
5 == 5
8 != 3
10 > 2
4 <= 8
```

## Boolean Logic

```text
TRUE AND FALSE
TRUE OR FALSE
NOT FALSE
```

## Conditionals

```text
IF x > y THEN 1
ELIF x == y THEN 0
ELSE -1
```

---

# ⚙️ How It Works

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
Abstract Syntax Tree
      │
      ▼
Interpreter
      │
      ▼
Output
```

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/quilhawk.git
```

```bash
cd quilhawk
```

Run the interpreter.

```bash
python shell.py
```

Example

```text
Quilhawk > VAR x = 5

5

Quilhawk > x + 10

15

Quilhawk > IF x > 3 THEN 100 ELSE 0

100
```

---

# 🛠️ Built With

- Python 3
- Recursive Descent Parsing
- Interpreter Pattern
- AST Architecture

---

# 📚 Concepts Covered

- Lexical Analysis
- Tokenization
- Parsing
- Abstract Syntax Trees
- Runtime Evaluation
- Context Management
- Symbol Tables
- Error Handling
- Interpreter Design

---

# 🗺️ Roadmap

- [x] Lexer
- [x] Tokenizer
- [x] Parser
- [x] Abstract Syntax Tree (AST)
- [x] Interpreter
- [x] Runtime Engine
- [x] Variables
- [x] Constants
- [x] Arithmetic Operators
- [x] Comparison Operators
- [x] Boolean Logic
- [x] IF / ELIF / ELSE
- [ ] While Loops
- [ ] For Loops
- [ ] Functions
- [ ] Recursive Functions
- [ ] Anonymous Functions
- [ ] Closures
- [ ] Strings
- [ ] Lists
- [ ] Dictionaries
- [ ] Classes
- [ ] Objects
- [ ] Modules
- [ ] Imports
- [ ] Exception Handling
- [ ] Standard Library
- [ ] Package Manager
- [ ] Bytecode Compiler
- [ ] Optimizer

---

# 📈 Future Goals

- Develop a complete standard library.
- Add advanced control-flow statements.
- Support user-defined functions.
- Implement object-oriented programming.
- Build a package manager.
- Create a bytecode compiler.
- Improve execution speed.
- Expand language documentation.

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

# 📜 Changelog

See **CHANGELOG.md** for all release notes.

---

# ⭐ Support

If you enjoyed this project, consider giving it a ⭐ on GitHub.

Your support helps the project grow!

---

<div align="center">

## Built with ❤️ by Danish Khan

**Building a programming language one token at a time.**

</div>

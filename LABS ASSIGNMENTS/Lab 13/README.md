# 🧪 Lab 13: Code Refactoring – Improving Legacy Code with AI

## 🎯 Main Motto
The main goal of this lab is to **identify issues in legacy Python code** and use **AI-assisted tools** (like GitHub Copilot or ChatGPT) to **refactor** the code for better **readability, maintainability, and performance** — without changing its original functionality.

By completing this lab, students learn how to:
- Detect inefficiencies and code smells.
- Apply modern Python practices.
- Use AI tools to improve old programs.
- Ensure the refactored code produces the same output as before.

---

## 🧩 Task 1 – Refactoring a Legacy Calculator Script

### 🧠 Description
The legacy calculator used long `if-else` statements and lacked modular design or error handling.

### 🔧 Modifications Done
| Aspect | Legacy Code | Refactored Code |
|--------|--------------|----------------|
| **Structure** | Repetitive `if-elif` for each operation. | Used a **dictionary-based operation mapping**. |
| **Modularity** | All logic in a single block. | Divided into separate **functions** and a `calculator()` driver function. |
| **Error Handling** | None. | Added `try-except` for invalid inputs and handled division by zero. |
| **Readability** | Hard to extend or debug. | Clean and easier to maintain. |

✅ **Result:** Code is modular, readable, and safer to execute.

---

## 🧱 Task 2 – Modernizing a Student Database Program

### 🧠 Description
The old program used global variables and crashed on invalid inputs.

### 🔧 Modifications Done
| Aspect | Legacy Code | Refactored Code |
|--------|--------------|----------------|
| **Design** | Procedural with global list. | Used **OOP design** (`Student` and `StudentDatabase` classes). |
| **Data Management** | Stored data as nested lists. | Stored as **objects with attributes**. |
| **Error Handling** | None. | Added **exceptions** for duplicates and invalid searches. |
| **Scalability** | Difficult to expand. | Modular and extendable with class methods. |

✅ **Result:** Refactored code is object-oriented, reliable, and maintainable.

---

## ⚙️ Task 3 – Optimizing File Processing Performance

### 🧠 Description
The old script read large files using inefficient loops, causing delays.

### 🔧 Modifications Done
| Aspect | Legacy Code | Refactored Code |
|--------|--------------|----------------|
| **File Handling** | Used `open()` and `readlines()`. | Used **context manager (`with open`)**. |
| **Loop Efficiency** | Manual looping through lines. | Replaced with **list comprehension / generator**. |
| **Performance** | High memory usage, slower. | Optimized for speed and memory. |
| **Code Simplicity** | Verbose and repetitive. | Compact and pythonic. |

✅ **Result:** Faster, more efficient file processing with minimal memory load.

---

## 🧠 Task 4 – Enhancing Readability and Documentation

### 🧠 Description
A scientific computation script had unclear variable names and no documentation.

### 🔧 Modifications Done
| Aspect | Legacy Code | Refactored Code |
|--------|--------------|----------------|
| **Variable Naming** | Used unclear names (`c`, `d`, `r`). | Replaced with **meaningful names** (`compute_value`, `data`, `results`). |
| **Documentation** | No comments or docstrings. | Added **inline comments and docstrings**. |
| **Code Structure** | Logic in global scope. | Wrapped in a **`main()` function**. |
| **Readability** | Hard to interpret. | Clean and well-structured. |

✅ **Result:** Readable, consistent, and documented scientific script.

---

## 🧭 Overall Improvements
- Introduced **functions** and **OOP principles**.  
- Added **exception handling** for robust execution.  
- Improved **loop efficiency** and file handling.  
- Enhanced **readability, modularity, and maintainability**.  
- Demonstrated how **AI tools** accelerate refactoring and modernization.

---

## 🧾 Tools Used
- **Python 3.x**  
- **GitHub Copilot** (AI code suggestions)  
- **VS Code**  
- **Git & GitHub** (version control)

---

## 📘 Author
**Name:** *[Your Name]*  
**Roll No:** *[Your Roll Number]*  
**Course:** *Python Programming / Software Engineering*  
**Lab:** *13 – Code Refactoring with AI*

---

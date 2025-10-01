# OxygenLang-Compiler
A programming language with a GUI-based compiler in Python. Supports variable assignments, loops, conditionals, and output display, demonstrating compiler concepts like lexing, parsing, AST, and execution

````markdown
# OxygenLang Compiler

**OxygenLang** is a programming language with a **GUI-based compiler** built in Python.  
It supports variable assignments, loops, conditionals, and output display, demonstrating compiler concepts such as **lexical analysis, parsing, AST, and code execution**.

---

## Features

- **Variable assignment** using `let`  
  ```oxygen
  let x = 5
  let y = x + 10
````

* **Printing values** using `show`

  ```oxygen
  show x
  show "Hello OxygenLang!"
  ```
* **Conditional statements (`if/else`)**

  ```oxygen
  if x > 5 then
      show "Big"
  else
      show "Small"
  end
  ```
* **While loops**

  ```oxygen
  while x < 5
      show x
      let x = x + 1
  end
  ```
* **Comments** using `#`

  ```oxygen
  # This is a comment
  ```
* **GUI popup window** with:

  * Code editor
  * Compile button
  * Output display panel

---

## Requirements

* Python 3.x
* No external libraries required (uses built-in `tkinter`)

---

## Installation & Usage

1. Clone or download this repository.
2. Run the Python file:

   ```bash
   python oxygenlang_gui.py
   ```
3. A popup window will open:

   * **Top panel:** Write OxygenLang code.
   * **Compile button:** Execute the code.
   * **Bottom panel:** View program output.

---

## Example Program

```oxygen
# OxygenLang Demo
let x = 0
let y = 3
show "Starting loop"

while x < y
    show x
    let x = x + 1
end

if x == y then
    show "Loop finished!"
else
    show "Error"
end
```

**Output:**

```
Starting loop
0
1
2
Loop finished!
```

---

## How It Works

1. **Lexer:** Tokenizes source code into keywords, identifiers, numbers, operators, and strings.
2. **Parser:** Converts tokens into an **Abstract Syntax Tree (AST)**.
3. **Compiler / Executor:** Walks the AST to execute OxygenLang code.
4. **GUI:** Uses `tkinter` for a text editor and output display.

---

## Project Structure

```
oxygenlang_gui.py      # Main Python file with GUI and compiler
README.md              # Project documentation
```

---

## Future Enhancements

* Add **syntax highlighting** in the editor.
* Support **functions and scopes**.
* Add **data types** like lists, floats, and booleans.
* Add **file open/save functionality**.
* Build a **JIT compiler version** of OxygenLang.

---

## Author

Created by **Nilesh Gosavi** – a project demonstrating **compiler design and GUI-based compilers in Python**.







import tkinter as tk
from tkinter import scrolledtext, messagebox


class OxygenLang:
    def __init__(self):
        self.symbol_table = {}

    def eval_expr(self, expr):
        """Evaluate expressions with variable substitution."""
        try:
            for var, val in self.symbol_table.items():
                expr = expr.replace(var, str(val))
            return eval(expr)
        except Exception as e:
            return f"Error: {e}"

    def execute(self, commands, output_widget=None):
        i = 0
        while i < len(commands):
            line = commands[i].strip()

            # Ignore empty lines and comments
            if not line or line.startswith("#"):
                i += 1
                continue

            # used Variable assignment using 'let'
            if line.startswith("let"):
                _, rest = line.split("let", 1)
                var, expr = rest.split("=")
                var = var.strip()
                value = self.eval_expr(expr.strip())
                self.symbol_table[var] = value

            # Show command 
            elif line.startswith("show"):
                expr = line.replace("show", "").strip()
                result = self.eval_expr(expr)
                if output_widget:
                    output_widget.insert(tk.END, str(result) + "\n")
                else:
                    print(result)

            # If statement with or without else 
            elif line.startswith("if"):
                cond = line.replace("if", "").replace("then", "").strip()
                cond_result = self.eval_expr(cond)

                if_body = []
                else_body = []
                inside_else = False

                i += 1
                while i < len(commands) and commands[i].strip() != "end":
                    if commands[i].strip().startswith("else"):
                        inside_else = True
                        i += 1
                        continue
                    if not inside_else:
                        if_body.append(commands[i])
                    else:
                        else_body.append(commands[i])
                    i += 1

                if cond_result:
                    self.execute(if_body, output_widget)
                else:
                    self.execute(else_body, output_widget)

            # While loop
            elif line.startswith("while"):
                cond = line.replace("while", "").strip()

                loop_body = []
                i += 1
                while i < len(commands) and commands[i].strip() != "end":
                    loop_body.append(commands[i])
                    i += 1

                while self.eval_expr(cond):
                    self.execute(loop_body, output_widget)

            i += 1



def run_code():
    code = editor.get("1.0", tk.END).strip().split("\n")
    output.delete("1.0", tk.END)  # clear output
    interpreter = OxygenLang()
    interpreter.execute(code, output)


# Create Tkinter Window
window = tk.Tk()
window.title("OxygenLang Compiler")

# Editor
editor_label = tk.Label(window, text="Write OxygenLang Code:")
editor_label.pack()
editor = scrolledtext.ScrolledText(window, width=60, height=15)
editor.pack()

# Run Button
run_button = tk.Button(window, text="Run Program", command=run_code)
run_button.pack(pady=5)

# Output Area
output_label = tk.Label(window, text="Output:")
output_label.pack()
output = scrolledtext.ScrolledText(window, width=60, height=10, state="normal")
output.pack()

window.mainloop()

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False, False)
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        btns = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in btns:
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(frame, text=char, font=("Arial", 18), command=lambda c=char: self.on_button_click(c))
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        clear_btn = tk.Button(self, text="C", font=("Arial", 18), command=self.clear)
        clear_btn.pack(fill="both", padx=10, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.expression)
                if isinstance(result, float):
                    result = round(result, 10)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
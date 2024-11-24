
import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("PyCalc")

    entry = tk.Entry(root, width=40)
    entry.pack()

    def evaluate_expression():
        try:
            result = eval(entry.get())
            result_label.config(text=f"Result: {result}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    button = tk.Button(root, text="Calculate", command=evaluate_expression)
    button.pack()

    result_label = tk.Label(root, text="Result: ")
    result_label.pack()

    root.mainloop()

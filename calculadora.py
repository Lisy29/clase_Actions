import tkinter as tk
root = tk.Tk(); root.title("Calculadora")
entry = tk.Entry(root, font=("Arial", 18), justify="right"); entry.grid(row=0, column=0, columnspan=4, sticky="we")
def click(v): entry.insert(tk.END, v)
def calc(): entry.delete(0, tk.END); entry.insert(0, eval(expression)) if (expression := entry.get()) else None
def clear(): entry.delete(0, tk.END)
buttons = ["7","8","9","/","4","5","6","*","1","2","3","-","C","0","=","+"]
for i, b in enumerate(buttons): (clear if b=="C" else calc if b=="=" else lambda v=b: click(v)) and tk.Button(root, text=b, font=("Arial", 14), width=4, command=clear if b=="C" else calc if b=="=" else lambda v=b: click(v)).grid(row=1+i//4, column=i%4)
root.mainloop()

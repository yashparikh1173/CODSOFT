import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity, use_uppercase, use_lowercase, use_digits, use_punctuation):
    characters = ''
    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_punctuation:
            characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid input", "Please enter a positive number for the length.")
            return

        complexity = complexity_var.get()
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_punctuation = punctuation_var.get()
        
        password = generate_password(length, complexity, use_uppercase, use_lowercase, use_digits, use_punctuation)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

def copy_to_clipboard():
    password = result_label.cget("text").replace("Generated Password: ", "")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

def clear_inputs():
    length_entry.delete(0, tk.END)
    complexity_var.set("custom")
    uppercase_var.set(False)
    lowercase_var.set(False)
    digits_var.set(False)
    punctuation_var.set(False)
    update_checkbuttons()
    result_label.config(text="")

def update_checkbuttons():
    state = tk.NORMAL if complexity_var.get() == "custom" else tk.DISABLED
    uppercase_checkbutton.config(state=state)
    lowercase_checkbutton.config(state=state)
    digits_checkbutton.config(state=state)
    punctuation_checkbutton.config(state=state)

def exit_application():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, pady=5)

complexity_var = tk.StringVar(value="custom")

tk.Label(root, text="Complexity Level:").grid(row=1, column=0, pady=5)
tk.Radiobutton(root, text="Low (Lowercase only)", variable=complexity_var, value="low", command=update_checkbuttons).grid(row=1, column=1, pady=5)
tk.Radiobutton(root, text="Medium (Letters + Digits)", variable=complexity_var, value="medium", command=update_checkbuttons).grid(row=2, column=1, pady=5)
tk.Radiobutton(root, text="High (Letters + Digits + Punctuation)", variable=complexity_var, value="high", command=update_checkbuttons).grid(row=3, column=1, pady=5)
tk.Radiobutton(root, text="Custom", variable=complexity_var, value="custom", command=update_checkbuttons).grid(row=4, column=1, pady=5)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
punctuation_var = tk.BooleanVar()

uppercase_checkbutton = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_checkbutton.grid(row=5, column=0, columnspan=2, pady=5)

lowercase_checkbutton = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_checkbutton.grid(row=6, column=0, columnspan=2, pady=5)

digits_checkbutton = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbutton.grid(row=7, column=0, columnspan=2, pady=5)

punctuation_checkbutton = tk.Checkbutton(root, text="Include Punctuation", variable=punctuation_var)
punctuation_checkbutton.grid(row=8, column=0, columnspan=2, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=9, column=0, columnspan=2, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=10, column=0, columnspan=2, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=11, column=0, columnspan=2, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.grid(row=12, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=13, column=0, columnspan=2, pady=10)

# Initialize the state of the checkbuttons
update_checkbuttons()

# Run the application
root.mainloop()

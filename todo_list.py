import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x400")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', padding=6, relief='flat', background='#ff9800', font=('Arial', 10, 'bold'))
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 12))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header label
        self.header_label = ttk.Label(self.main_frame, text="My To-Do List", style='Header.TLabel')
        self.header_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Task list frame
        self.task_frame = ttk.Frame(self.main_frame, padding="10", relief='sunken', style='TFrame')
        self.task_frame.grid(row=1, column=0, rowspan=6, padx=(0, 10), sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Task listbox with scrollbar
        self.task_listbox = tk.Listbox(self.task_frame, height=15, width=40, selectmode=tk.SINGLE, font=('Arial', 12))
        self.task_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.scrollbar = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.task_listbox.yview)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Button frame
        self.button_frame = ttk.Frame(self.main_frame, padding="10", style='TFrame')
        self.button_frame.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        # Buttons
        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.update_button = ttk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.mark_done_button = ttk.Button(self.button_frame, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=root.destroy)
        self.exit_button.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # Initialize task list
        self.tasks = []
        self.populate_tasks()

    def populate_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " (Done)" if task['done'] else ""
            self.task_listbox.insert(tk.END, task['task'] + status)

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter the task name:")
        if task_name:
            self.tasks.append({'task': task_name, 'done': False})
            self.populate_tasks()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task_name = simpledialog.askstring("Update Task", "Enter the new task name:")
            if new_task_name:
                self.tasks[selected_index]['task'] = new_task_name
                self.populate_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def mark_done(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['done'] = True
            self.populate_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.populate_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

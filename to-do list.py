import tkinter as tk
from tkinter import messagebox
from tkinter import font

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Set window size and position
        window_width = 400
        window_height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.tasks = []

        # Default font
        self.default_font = ("Helvetica", 12)

        # Add Task entry
        tk.Label(master, text="Task:", font=self.default_font).grid(row=0, column=0, padx=10, pady=10)
        self.task_entry = tk.Entry(master, width=30, font=self.default_font)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # Priority selection
        tk.Label(master, text="Priority:", font=self.default_font).grid(row=1, column=0, padx=10, pady=10)
        self.priority_var = tk.StringVar(master)
        self.priority_var.set("High")  # Default priority
        priorities = ["High", "Medium", "Low"]
        self.priority_menu = tk.OptionMenu(master, self.priority_var, *priorities)
        self.priority_menu.grid(row=1, column=1, padx=10, pady=10)

        # Time limit entry
        tk.Label(master, text="Time Limit (e.g., HH:MM):", font=self.default_font).grid(row=2, column=0, padx=10, pady=10)
        self.time_limit_entry = tk.Entry(master, width=10, font=self.default_font)
        self.time_limit_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=self.default_font)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Task listbox with checkboxes
        self.task_frame = tk.Frame(master)
        self.task_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(self.task_frame, width=40, font=self.default_font, yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Delete Task button
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=self.default_font)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.update_listbox()

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        time_limit = self.time_limit_entry.get()
        if task:
            color = "black"  # Default color for low priority tasks
            if priority == "High":
                color = "red"
            elif priority == "Medium":
                color = "green"
            self.tasks.append((task, priority, time_limit, color, False))  # False indicates task is not completed
            self.task_entry.delete(0, tk.END)
            self.time_limit_entry.delete(0, tk.END)
            self.update_listbox()

    def delete_task(self):
        selected_tasks_indices = self.task_listbox.curselection()
        if selected_tasks_indices:
            selected_tasks = [self.tasks[int(i)] for i in selected_tasks_indices]
            for task in selected_tasks:
                self.tasks.remove(task)
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, (task, priority, time_limit, color, completed) in enumerate(self.tasks):
            task_display = f"{task} - Priority: {priority} - Time Limit: {time_limit} {'(Completed)' if completed else ''}"
            self.task_listbox.insert(tk.END, task_display)
            self.task_listbox.itemconfig(i, fg=color)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

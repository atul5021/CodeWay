from tkinter import messagebox, filedialog, Tk, Entry, Button, Listbox

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x300")

        self.tasks = []

        self.task_entry = Entry(self.master, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.display_button = Button(self.master, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack(pady=5)

        self.remove_button = Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.save_button = Button(self.master, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = Button(self.master, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        self.exit_button = Button(self.master, text="Exit", command=self.master.destroy)
        self.exit_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Task Display", "No tasks found. Add some tasks!")
        else:
            tasks_str = "\n".join(self.tasks)
            messagebox.showinfo("Task Display", f"Tasks:\n{tasks_str}")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks.pop(index)
            self.update_task_listbox()
            messagebox.showinfo("Task Removed", f"Task '{task}' removed successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def save_tasks(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task}\n")
            messagebox.showinfo("Save Tasks", f"Tasks saved to {filename}.")

    def load_tasks(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as file:
                self.tasks = [line.strip() for line in file]
            self.update_task_listbox()
            messagebox.showinfo("Load Tasks", f"Tasks loaded from {filename}.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, "end")
        for task in self.tasks:
            self.task_listbox.insert("end", task)

def main():
    root = Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

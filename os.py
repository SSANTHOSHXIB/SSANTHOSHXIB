import tkinter as tk
import subprocess
import os

class Terminal(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.text = tk.Text(self, height=20, width=80, bg="black", fg="white")
        self.text.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self, bg="black", fg="white", insertbackground="white")
        self.entry.pack(fill=tk.X)
        
        self.entry.bind("<Return>", self.run_command)

        self.history = []
        self.history_index = 0

        self.prompt = '>> '
        self.text.insert(tk.END, self.prompt)

    def run_command(self, event):
        command = self.entry.get()
        self.history.append(command)
        self.history_index = len(self.history)

        self.text.insert(tk.END, "\n" + self.prompt + command + "\n")

        try:
            if command.startswith("cd "):
                path = command[3:]
                os.chdir(path)
            elif command.endswith(".sh"):
                subprocess.run(command, shell=True)
            elif command.startswith("nano "):  
                file_path = command[8:]
                subprocess.Popen(["notepad.exe", file_path])
            elif command.startswith("gcc "):  
                file_path = command[4:]
                exe_path = os.path.splitext(file_path)[0] + ".exe"
                compile_command = f"gcc {file_path} -o {exe_path}"
                result = subprocess.run(compile_command, shell=True, stderr=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    run_command = f"{exe_path}"
                    output = subprocess.check_output(run_command, shell=True, stderr=subprocess.STDOUT, text=True)
                    self.text.insert(tk.END, output + "\n")
                else:
                    self.text.insert(tk.END, "Compilation Error: " + result.stderr + "\n")
            else:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                self.text.insert(tk.END, output + "\n")
        except subprocess.CalledProcessError as e:
            self.text.insert(tk.END, "Error: " + str(e) + "\n")

        self.text.insert(tk.END, self.prompt)
        self.entry.delete(0, tk.END)

    def handle_up_key(self, event):
        if self.history_index > 0:
            self.history_index -= 1
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.history[self.history_index])

    def handle_down_key(self, event):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.history[self.history_index])
        elif self.history_index == len(self.history) - 1:
            self.history_index += 1
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("COMMAND LINE")
    root.geometry("1920x1080")
    root.configure(bg="black")
    terminal = Terminal(root)
    terminal.pack(fill=tk.BOTH, expand=True)

    root.bind("<Up>", terminal.handle_up_key)
    root.bind("<Down>", terminal.handle_down_key)

    root.mainloop()

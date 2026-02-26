import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class ReadMeForge:
    def __init__(self, root):
        self.root = root
        self.root.title("README Forge - Project Documenter")
        self.root.geometry("600x700")
        self.root.configure(bg="#F8FAFC")
        
        self.db_path = "data/data.json"
        self.initialize_data()
        self.data = self.read_data()
        
        self.setup_ui()

    def initialize_data(self):
        if not os.path.exists("data"): os.mkdir("data")
        if not os.path.exists(self.db_path):
            default = {
                'languages': ['Python', 'Javascript', 'HTML', 'CSS'],
                'Python': ['Flask', 'Pandas', 'OpenCV', 'Numpy', 'Pillow'],
                'Javascript': ['React', 'Vue', 'Node.js'],
                'HTML': ['Bootstrap', 'Tailwind'],
                'CSS': ['Sass', 'Animate.css']
            }
            with open(self.db_path, "w") as f:
                json.dump(default, f, indent=2)

    def read_data(self):
        with open(self.db_path, "r") as f:
            return json.load(f)

    def setup_ui(self):
        # --- Header ---
        header = tk.Frame(self.root, bg="#F8FAFC", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="README Forge", font=("Helvetica", 24, "bold"), 
                 bg="#F8FAFC", fg="#1E293B").pack()

        # --- Main Form ---
        form = tk.Frame(self.root, bg="white", bd=1, relief="solid", padx=20, pady=20)
        form.pack(fill="both", expand=True, padx=40, pady=10)

        # Basic Info
        self.create_label_entry(form, "Project Name:", "name_var")
        self.create_label_entry(form, "Short Description:", "desc_var")
        self.create_label_entry(form, "Installation Guide:", "guide_var")

        # Language Selection
        tk.Label(form, text="Select Languages:", font=("Helvetica", 10, "bold"), bg="white").pack(anchor="w", pady=(10,0))
        self.lang_listbox = tk.Listbox(form, selectmode="multiple", height=4, exportselection=0)
        for lang in self.data['languages']:
            self.lang_listbox.insert(tk.END, lang)
        self.lang_listbox.pack(fill="x", pady=5)
        self.lang_listbox.bind('<<ListboxSelect>>', self.update_packages)

        # Package Selection
        tk.Label(form, text="Select Packages (hold Ctrl to multi-select):", font=("Helvetica", 10, "bold"), bg="white").pack(anchor="w")
        self.pack_listbox = tk.Listbox(form, selectmode="multiple", height=5, exportselection=0)
        self.pack_listbox.pack(fill="x", pady=5)

        # Actions
        btn_frame = tk.Frame(self.root, bg="#F8FAFC", pady=20)
        btn_frame.pack(fill="x", padx=40)

        tk.Button(btn_frame, text="GENERATE README", bg="#3B82F6", fg="white", 
                  font=("Helvetica", 12, "bold"), relief="flat", height=2,
                  command=self.generate_readme).pack(fill="x")

    def create_label_entry(self, parent, label_text, var_name):
        tk.Label(parent, text=label_text, font=("Helvetica", 10, "bold"), bg="white").pack(anchor="w")
        var = tk.StringVar()
        setattr(self, var_name, var)
        tk.Entry(parent, textvariable=var, font=("Helvetica", 11), bg="#F1F5F9", bd=0).pack(fill="x", pady=(0, 10), ipady=5)

    def update_packages(self, event):
        selected_indices = self.lang_listbox.curselection()
        self.pack_listbox.delete(0, tk.END)
        for i in selected_indices:
            lang = self.lang_listbox.get(i)
            if lang in self.data:
                for p in self.data[lang]:
                    self.pack_listbox.insert(tk.END, f"{lang}: {p}")

    def generate_readme(self):
        title = self.name_var.get().strip()
        if not title:
            messagebox.showerror("Error", "Project Name is required!")
            return

        # Gather Selected Packages
        selected_packs = [self.pack_listbox.get(i) for i in self.pack_listbox.curselection()]
        package_str = "\n".join([f"- {p}" for p in selected_packs])

        content = f"""# {title}
{self.desc_var.get()}

## Stack & Dependencies
{package_str if package_str else "Standard library only."}

## Installation
```bash
{self.guide_var.get()}
Future Plans
No plans yet!
"""
        with open(f"{title}_README.md", "w") as f:
            f.write(content)
            messagebox.showinfo("Success", f"{title}_README.md generated successfully!")
if __name__ == "__main__":
    root = tk.Tk()
    app = ReadMeForge(root)
    root.mainloop()
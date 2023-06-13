import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".yft") or filename.endswith(".ytd"):
            files.append(filename)
    return files

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

def browse_vehicles_meta():
    file_path = filedialog.askopenfilename(filetypes=(("Meta Files", "*.meta"), ("All Files", "*.*")))
    vehicles_meta_entry.delete(0, tk.END)
    vehicles_meta_entry.insert(tk.END, file_path)

def browse_carvariations_meta():
    file_path = filedialog.askopenfilename(filetypes=(("Meta Files", "*.meta"), ("All Files", "*.*")))
    carvariations_meta_entry.delete(0, tk.END)
    carvariations_meta_entry.insert(tk.END, file_path)

def rename_files():
    directory = directory_entry.get()
    old_value = old_value_entry.get()
    new_value = new_value_entry.get()

    if not directory or not old_value or not new_value:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    files = get_files_in_directory(directory)

    if not files:
        messagebox.showinfo("Info", "No .yft or .ytd files found in the directory.")
        return

    for filename in files:
        new_filename = filename.replace(old_value, new_value)
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        try:
            os.rename(old_file_path, new_file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to rename file {filename}: {str(e)}")

        vehicles_meta_path = vehicles_meta_entry.get()
        carvariations_meta_path = carvariations_meta_entry.get()

        replace_in_file(vehicles_meta_path, old_value, new_value)
        replace_in_file(carvariations_meta_path, old_value, new_value)

    messagebox.showinfo("Info", "Batch rename completed successfully.")

def replace_in_file(file_path, old_value, new_value):
    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            content = file.read()
            content = content.replace(old_value, new_value)

        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to replace in file {file_path}: {str(e)}")

# Create the GUI
window = tk.Tk()
window.title("Text File Utilities")
window.geometry("800x500")
window.configure(bg="#202124")

# Dark mode theme
window.tk.call("tk", "scaling", 2.0)
window.tk_setPalette(background="#202124", foreground="white")
entry_bg_color = "#282c34"
button_bg_color = "#3f51b5"

# Directory field
directory_label = tk.Label(window, text="Directory containing .yft and .ytd:", bg="#202124", fg="white")
directory_label.pack()
directory_entry = tk.Entry(window, bg=entry_bg_color)
directory_entry.pack()
directory_button = tk.Button(window, text="Browse", command=browse_directory, bg=button_bg_color, fg="white")
directory_button.pack()

# Vehicles.meta field
vehicles_meta_label = tk.Label(window, text="Location of vehicles.meta:", bg="#202124", fg="white")
vehicles_meta_label.pack()
vehicles_meta_entry = tk.Entry(window, bg=entry_bg_color)
vehicles_meta_entry.pack()
vehicles_meta_button = tk.Button(window, text="Browse", command=browse_vehicles_meta, bg=button_bg_color, fg="white")
vehicles_meta_button.pack()

# Carvariations.meta field
carvariations_meta_label = tk.Label(window, text="Location of carvariations.meta:", bg="#202124", fg="white")
carvariations_meta_label.pack()
carvariations_meta_entry = tk.Entry(window, bg=entry_bg_color)
carvariations_meta_entry.pack()
carvariations_meta_button = tk.Button(window, text="Browse", command=browse_carvariations_meta, bg=button_bg_color, fg="white")
carvariations_meta_button.pack()

# Old value field
old_value_label = tk.Label(window, text="Old value:", bg="#202124", fg="white")
old_value_label.pack()
old_value_entry = tk.Entry(window, bg=entry_bg_color)
old_value_entry.pack()

# New value field
new_value_label = tk.Label(window, text="New value:", bg="#202124", fg="white")
new_value_label.pack()
new_value_entry = tk.Entry(window, bg=entry_bg_color)
new_value_entry.pack()

# Batch rename button
rename_button = tk.Button(window, text="Batch Rename", command=rename_files, bg=button_bg_color, fg="white")
rename_button.pack()


window.mainloop()
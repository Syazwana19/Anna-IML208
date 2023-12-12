import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class PersonalShopperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Shopper App")
        self.root.geometry("400x300")

        self.shoppers = []

        # Main window widgets
        self.label = tk.Label(root, text="Personal Shopper App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Shopper", command=self.add_shopper)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Shoppers", command=self.view_shoppers)
        self.view_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Shopper", command=self.update_shopper)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Shopper", command=self.delete_shopper)
        self.delete_button.pack(pady=5)

        # Data display screen
        self.data_label = tk.Label(root, text="Data Display", font=("Helvetica", 12))
        self.data_label.pack(pady=5)

        self.data_text = tk.Text(root, height=8, width=40)
        self.data_text.pack(pady=5)

    def update_data_screen(self):
        self.data_text.delete(1.0, tk.END)
        if not self.shoppers:
            self.data_text.insert(tk.END, "No shoppers available.")
        else:
            shopper_list = "\n".join(self.shoppers)
            self.data_text.insert(tk.END, f"Shoppers:\n{shopper_list}")

    def add_shopper(self):
        name = simpledialog.askstring("Add Shopper", "Enter Shopper Name:")
        if name:
            self.shoppers.append(name)
            messagebox.showinfo("Success", f"Shopper '{name}' added successfully!")
            self.update_data_screen()

    def view_shoppers(self):
        self.update_data_screen()

    def update_shopper(self):
        if not self.shoppers:
            messagebox.showinfo("Info", "No shoppers available.")
        else:
            old_name = simpledialog.askstring("Update Shopper", "Enter Shopper Name to Update:")
            if old_name in self.shoppers:
                new_name = simpledialog.askstring("Update Shopper", "Enter New Shopper Name:")
                if new_name:
                    self.shoppers[self.shoppers.index(old_name)] = new_name
                    messagebox.showinfo("Success", f"Shopper '{old_name}' updated to '{new_name}' successfully!")
                    self.update_data_screen()
            else:
                messagebox.showerror("Error", f"Shopper '{old_name}' not found.")

    def delete_shopper(self):
        if not self.shoppers:
            messagebox.showinfo("Info", "No shoppers available.")
        else:
            name = simpledialog.askstring("Delete Shopper", "Enter Shopper Name to Delete:")
            if name in self.shoppers:
                self.shoppers.remove(name)
                messagebox.showinfo("Success", f"Shopper '{name}' deleted successfully!")
                self.update_data_screen()
            else:
                messagebox.showerror("Error", f"Shopper '{name}' not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalShopperApp(root)
    root.mainloop()



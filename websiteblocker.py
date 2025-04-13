import tkinter as tk
from tkinter import simpledialog, messagebox
import platform
import os
import re

# Detect OS and set hosts file path
if platform.system() == "Windows":
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux":
    HOSTS_PATH = r"/etc/hosts"
else:
    messagebox.showerror("Unsupported OS", "Only Windows and Linux are supported.")
    exit()

REDIRECT_IP = "127.0.0.1"

class WebsiteBlockerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Blocker")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self.build_main_menu()

    def build_main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Website Blocker", font=('Arial', 14, 'bold')).pack(pady=(0, 10))

        block_button = tk.Button(self.main_frame, text="Block", command=self.show_block_interface, width=20)
        block_button.pack(pady=5)

        unblock_button = tk.Button(self.main_frame, text="Unblock", command=self.show_unblock_interface, width=20)
        unblock_button.pack(pady=5)

    def get_blocked_sites(self):
        if not os.path.exists(HOSTS_PATH):
            return []
        try:
            with open(HOSTS_PATH, 'r') as file:
                lines = file.readlines()
        except PermissionError:
            messagebox.showerror("Permission Denied", "Admin/root permission is required to read the hosts file.")
            return []

        blocked = []
        for line in lines:
            if REDIRECT_IP in line:
                parts = line.strip().split()
                if len(parts) > 1:
                    blocked.append(parts[1])
        return blocked

    def show_block_interface(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Blocked Websites:", font=('Arial', 12, 'bold')).pack()

        self.blocked_listbox = tk.Listbox(self.main_frame, width=50)
        self.blocked_listbox.pack(pady=5)
        for site in self.get_blocked_sites():
            self.blocked_listbox.insert(tk.END, site)

        tk.Button(self.main_frame, text="Add New", command=self.add_new_site_dialog).pack(pady=5)
        tk.Button(self.main_frame, text="Back", command=self.build_main_menu).pack(pady=5)

    def show_unblock_interface(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Unblock Websites", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2)

        blocked_sites = self.get_blocked_sites()

        for i, site in enumerate(blocked_sites, start=1):
            tk.Label(self.main_frame, text=site).grid(row=i, column=0, sticky='w', padx=5)
            btn = tk.Button(self.main_frame, text="X", fg='red', command=lambda s=site: self.unblock_site(s))
            btn.grid(row=i, column=1, padx=5)

        tk.Button(self.main_frame, text="Back", command=self.build_main_menu).grid(row=len(blocked_sites)+1, column=0, columnspan=2, pady=10)

    def add_new_site_dialog(self):
        site = simpledialog.askstring("Add Website", "Enter website URL(without http or https) to block (e.g., example.com):")
        if site:
            self.block_website(site)
            self.show_block_interface()

    def block_website(self, site):
        try:
            with open(HOSTS_PATH, 'r+') as file:
                content = file.read()
                if site not in content:
                    file.write(f"{REDIRECT_IP} {site}\n")
                    messagebox.showinfo("Success", f"{site} has been blocked.")
                else:
                    messagebox.showinfo("Info", f"{site} is already blocked.")
        except PermissionError:
            messagebox.showerror("Permission Denied", "Admin/root permission is required to block websites.")

    def unblock_site(self, site):
        try:
            with open(HOSTS_PATH, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if site not in line:
                        file.write(line)
                file.truncate()
            messagebox.showinfo("Success", f"{site} has been unblocked.")
            self.show_unblock_interface()
        except PermissionError:
            messagebox.showerror("Permission Denied", "Admin/root permission is required to unblock websites.")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteBlockerApp(root)
    root.mainloop()

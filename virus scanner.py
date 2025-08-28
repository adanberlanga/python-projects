import os
import threading
import tkinter as tk
from tkinter import messagebox, ttk
import hashlib

# Dummy virus signatures (hashes of known malicious files)
VIRUS_SIGNATURES = {
    "e99a18c428cb38d5f260853678922e03",  # Example MD5 hash
    "098f6bcd4621d373cade4e832627b4f6"
}

# Get Internet Explorer Downloads folder path
def get_ie_downloads_folder():
    import winreg
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Internet Explorer\Main") as key:
            downloads = winreg.QueryValueEx(key, "Default Download Directory")[0]
            return downloads
    except Exception:
        # Fallback to default Downloads folder
        return os.path.join(os.environ["USERPROFILE"], "Downloads")

def md5sum(filename):
    h = hashlib.md5()
    try:
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

class VirusScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IE Downloads Virus Scanner")
        self.is_scanning = False
        self.scan_thread = None

        self.start_btn = ttk.Button(root, text="Start Scan", command=self.start_scan)
        self.start_btn.pack(pady=10)

        self.cancel_btn = ttk.Button(root, text="Cancel", command=self.cancel_scan, state=tk.DISABLED)
        self.cancel_btn.pack(pady=10)

        self.progress = ttk.Label(root, text="Ready.")
        self.progress.pack(pady=10)

    def start_scan(self):
        self.is_scanning = True
        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.progress.config(text="Scanning...")
        self.scan_thread = threading.Thread(target=self.scan_files)
        self.scan_thread.start()

    def cancel_scan(self):
        self.is_scanning = False
        self.progress.config(text="Scan cancelled.")
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)

    def scan_files(self):
        folder = get_ie_downloads_folder()
        infected = []
        try:
            files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        except Exception:
            files = []
        for idx, file in enumerate(files):
            if not self.is_scanning:
                break
            self.progress.config(text=f"Scanning: {os.path.basename(file)} ({idx+1}/{len(files)})")
            hashval = md5sum(file)
            if hashval and hashval in VIRUS_SIGNATURES:
                infected.append(file)
        self.is_scanning = False
        self.root.after(0, self.show_result, infected)

    def show_result(self, infected):
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        if infected:
            messagebox.showwarning("Scan Complete", f"Virus detected in:\n" + "\n".join(infected))
        else:
            messagebox.showinfo("Scan Complete", "No viruses found.")
        self.progress.config(text="Ready.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VirusScannerApp(root)
    root.mainloop()
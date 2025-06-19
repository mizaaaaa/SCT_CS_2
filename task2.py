import os
import platform
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog
from tkinter.messagebox import askyesno

ctk.set_appearance_mode("dark")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue", etc.

class ImageEncryptorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image Encryptor/Decryptor")
        self.geometry("500x550")
        self.resizable(False, False)
        self.selected_file = None
        self.tk_img = None
        self.preview_widget = None

        # Title
        ctk.CTkLabel(self, text="🔒 Image Encryptor", font=("Arial", 20, "bold")).pack(pady=15)

        # File selection
        ctk.CTkLabel(self, text="Step 1: Select an Image").pack()
        self.file_label = ctk.CTkLabel(self, text="No file selected", text_color="grey")
        self.file_label.pack(pady=2)

        ctk.CTkButton(self, text="Browse", command=self.choose_file).pack(pady=5)

        # Image Preview placeholder (initially empty)
        self.preview_frame = ctk.CTkFrame(self)
        self.preview_frame.pack(pady=10)

        # Key entry
        ctk.CTkLabel(self, text="Step 2: Enter Key (0-255)").pack(pady=5)
        self.key_entry = ctk.CTkEntry(self, justify="center")
        self.key_entry.pack(pady=5)

        # Buttons
        ctk.CTkButton(self, text="🔐 Encrypt", command=self.encrypt_action, fg_color="green").pack(pady=10)
        ctk.CTkButton(self, text="🔓 Decrypt", command=self.decrypt_action, fg_color="blue").pack(pady=5)

    def choose_file(self):
        self.selected_file = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if self.selected_file:
            self.file_label.configure(text=os.path.basename(self.selected_file))
            self.display_preview(self.selected_file)

    def display_preview(self, path):
        try:
            img = Image.open(path).resize((150, 150))
            self.tk_img = ImageTk.PhotoImage(img)

            if self.preview_widget:
                self.preview_widget.configure(image=self.tk_img)
                self.preview_widget.image = self.tk_img
            else:
                self.preview_widget = ctk.CTkLabel(self.preview_frame, image=self.tk_img, text="")
                self.preview_widget.image = self.tk_img
                self.preview_widget.pack()
        except:
            if self.preview_widget:
                self.preview_widget.configure(text="(Preview failed)", image="", text_color="red")
            else:
                self.preview_widget = ctk.CTkLabel(self.preview_frame, text="(Preview failed)", text_color="red")
                self.preview_widget.pack()

    def open_file(self, path):
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":
                os.system(f"open '{path}'")
            elif platform.system() == "Linux":
                os.system(f"xdg-open '{path}'")
        except:
            self.show_popup("Error", "Could not open the image file.", "red")

    def get_key(self):
        try:
            key = int(self.key_entry.get())
            if 0 <= key <= 255:
                return key
            else:
                self.show_popup("Invalid Key", "Key must be between 0 and 255.", "orange")
        except ValueError:
            self.show_popup("Invalid Input", "Key must be an integer.", "orange")
        return None

    def encrypt_decrypt_image(self, key, mode):
        try:
            img = Image.open(self.selected_file).convert("RGB")
            pixels = img.load()

            for x in range(img.width):
                for y in range(img.height):
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (r ^ key, g ^ key, b ^ key)

            base, ext = os.path.splitext(self.selected_file)
            out_path = f"{base}_{'encrypted' if mode == 'encrypt' else 'decrypted'}{ext}"

            if os.path.exists(out_path):
                if not askyesno("File exists", f"{out_path} already exists. Overwrite?"):
                    return

            img.save(out_path)
            self.show_popup("Success", f"{mode.capitalize()}ed image saved:\n{out_path}", "green")
            self.open_file(out_path)

        except Exception as e:
            self.show_popup("Error", str(e), "red")

    def encrypt_action(self):
        if not self.selected_file:
            self.show_popup("No File", "Please select an image file first.", "orange")
            return
        key = self.get_key()
        if key is not None:
            self.encrypt_decrypt_image(key, "encrypt")

    def decrypt_action(self):
        if not self.selected_file:
            self.show_popup("No File", "Please select an image file first.", "orange")
            return
        key = self.get_key()
        if key is not None:
            self.encrypt_decrypt_image(key, "decrypt")

    def show_popup(self, title, message, color):
        popup = ctk.CTkToplevel(self)
        popup.geometry("300x120")
        popup.title(title)
        popup_label = ctk.CTkLabel(popup, text=message, text_color=color, wraplength=280)
        popup_label.pack(pady=10, padx=10)
        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)

if __name__ == "__main__":
    app = ImageEncryptorApp()
    app.mainloop()

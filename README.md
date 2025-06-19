# Image Encryptor/Decryptor

A simple GUI application for encrypting and decrypting image files using a key-based XOR operation. Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern dark theme and [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) for image processing.

## Features

- Encrypt any `.png`, `.jpg`, `.jpeg`, or `.bmp` image using a numeric key (0-255).
- Decrypt previously encrypted images with the same key.
- Simple and intuitive GUI.
- Image file preview before encryption/decryption.
- Overwrite-protection for output files.
- Cross-platform support (Windows, macOS, Linux).


## Requirements

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)
- [CustomTkinter](https://pypi.org/project/customtkinter/)

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/mizaaaaa/SCT_CS_2.git
   cd SCT_CS_2
   ```
   

2. **Install dependencies:**
   ```bash
   pip install pillow customtkinter
   ```

## Usage

1. **Run the application:**
   ```bash
   python task2.py
   ```

2. **Encrypt or Decrypt an Image:**
   - Click on **Browse** to select an image file.
   - Preview of the image appears in the window.
   - Enter a numeric key between 0 and 255.
   - Click **Encrypt** to encrypt the image or **Decrypt** to decrypt it.
   - The output file will be saved in the same directory as the original with `_encrypted` or `_decrypted` appended to the filename.

3. **Notes:**
   - Use the same key for decryption that was used for encryption.
   - The app will prompt if you attempt to overwrite an existing file.

## How It Works

This app uses a simple XOR cipher:
- Each pixel's RGB values are XORed with the provided key.
- The process is reversible: apply the same operation with the same key to decrypt.

## Limitations

- This encryption is not secure for sensitive data; it's for educational/demo purposes only.
- Only standard RGB images are supported.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

---


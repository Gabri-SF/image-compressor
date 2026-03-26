![Python Version](https://img.shields.io)
![Pillow](https://img.shields.io)
![License](https://img.shields.io)
![Repo Size](https://img.shields.io)
![Last Commit](https://img.shields.io)

# 📸 Batch Image Compressor CLI


A lightweight, powerful Python tool to recursively compress and resize images (**JPG, PNG, WebP**) while preserving folder structures. It automatically skips build folders (like `node_modules` or `.git`) and only overwrites files if the compression actually reduces the file size.

## ✨ Features

- 📂 **Recursive Processing:** Walks through all subdirectories.
- ⚡ **Smart Compression:** Supports JPEG, PNG, and WebP with optimized settings.
- 📏 **Auto-Resizing:** Set a maximum width or height to scale down large photos.
- 🛡️ **Safe Overwrite:** Only replaces the original file if the new version is smaller.
- 🧪 **Dry Run Mode:** Preview results without modifying any files.
- 🚫 **Smart Ignore:** Automatically skips development and cache folders (`node_modules`, `.next`, `dist`, etc.).

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- [Pillow](https://python-pillow.org) (Python Imaging Library)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gabri-SF/image-compressor.git
   cd image-compressor
   ```
   
## Examples
   ```bash
   python compress_images.py ./images # Basic Usage
   python compress_images.py ./images --quality 80 # Set custom quality
   python compress_images.py ./images --max-width 1200 --max-height 800 # Resize images (max width / height)
   python compress_images.py ./images --dry-run # Dry run (no file changes)
   python compress_images.py ./images --quality 75 --max-width 1920 --dry-run # Combine options (most common use)
   python compress_images.py ./images --quality 50 # Apply aggressive compression
   python compress_images.py . # Process current directory
   python compress_images.py /Users/gabriel/Desktop/photos --quality 70 # Use absolute path
   ```
## Tips
- Use --dry-run first to avoid unwanted quality loss
- JPEG benefits most from --quality
- PNG compression is lossless (quality affects compression level only)
- Script already avoids increasing file size 👍

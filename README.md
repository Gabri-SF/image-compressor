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

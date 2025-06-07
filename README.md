# 📄 PDFSplit – Command-Line PDF Splitter

Split long PDFs (lecture slides, books, papers) into smaller, manageable chunks — ideal for summarizing with **ChatGPT** or **Claude**.

✅ Cross-platform  
✅ No install needed  
✅ Works fully offline  
✅ Just download and run

---

## Quick Start

### Step 1: Download

Get the latest version from the [Releases page](https://github.com/sachaheizmann/PDF-splitter/releases):

| OS        | File name              |
|-----------|-------------------------|
| Windows   | `pdfsplit-windows.exe`   |
| macOS     | `pdfsplit-macos`         |
| Linux     | `pdfsplit-linux`         |

---

### Step 2: One-Time Setup (Run from Anywhere)

#### Windows

1. Rename `pdfsplit-windows.exe` → `pdfsplit.exe`
2. Move it to `C:\Program Files\PDFSplit\`
3. Add that folder to your **System PATH**:
   - Search for "Environment Variables"
   - Edit system `Path`, click "New", and add:
     ```
     C:\Program Files\PDFSplit\
     ```
4. Open a new **Command Prompt** and run:

```cmd
pdfsplit --help


#### macOS
run
``
chmod +x ~/Downloads/pdfsplit-macos
sudo mv ~/Downloads/pdfsplit-macos /usr/local/bin/pdfsplit
``
If blocked on first run:

xattr -dr com.apple.quarantine /usr/local/bin/pdfsplit

✅ Now run from anywhere:

pdfsplit --help

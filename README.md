# pdfsplit – Command-Line PDF Splitter

Split long PDFs (lecture slides, books, papers) into smaller, manageable chunks — ideal for summarizing with **ChatGPT** or **Claude**.

Cross-platform  
No install needed  
Works fully offline  
Just download and run

---

## Quick Start

### Step 1: Download

Follow the steps for your OS OR get the latest version from the [Releases page](https://github.com/sachaheizmann/pdfsplit/releases):

| OS        | File name              |
|-----------|-------------------------|
| Windows   |  `pdfsplit-windows.exe`    |
| macOS     | `pdfsplit-macos`         |
| Linux     | `pdfsplit-linux`         |

---

### Step 2: One-Time Setup (Run from Anywhere)

#### Windows

1. run
   ```cmd
   Invoke-WebRequest -Uri "https://github.com/sachaheizmann/pdfsplit/releases/download/v1.0.3/pdfsplit-windows.exe" -OutFile "$env:USERPROFILE\Downloads\pdfsplit.exe"
   ```
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
```

#### macOS
run
```
wget https://github.com/sachaheizmann/pdfsplit/releases/download/v1.0.3/pdfsplit-macos -O pdfsplit
chmod +x pdfsplit
sudo mv pdfsplit /usr/local/bin/pdfsplit
```
If blocked on first run:
```
xattr -dr com.apple.quarantine /usr/local/bin/pdfsplit
```
Now run from anywhere:
```
pdfsplit -h
```

#### Linux
run
```
wget https://github.com/sachaheizmann/pdfsplit/releases/download/v1.0.3/pdfsplit-linux -O pdfsplit
chmod +x pdfsplit
sudo mv pdfsplit /usr/local/bin/pdfsplit
```
Then try:
```
pdfsplit -a -p 10
```

### Usage Examples
Split one PDF into chunks of 10 pages:
```
pdfsplit -f "MySlides.pdf" -p 10
```
Split all PDFs in the folder into 15-page parts:
```
pdfsplit -all -pages 15
```


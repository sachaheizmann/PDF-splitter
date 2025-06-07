# PDF Slide Splitter

Split each PDF in a folder into smaller chunks (e.g. 15 pages each), organize them in folders, and rename duplicates if needed. Perfect for chatgpt summaries since he has trouble summarizing big PDFs.

## Features

- Automatically finds all PDFs in the current folder
- Creates a folder named after each PDF (without `.pdf`)
- Moves the original PDF into its folder
- Splits it into `-part1`, `-part2`, etc.
- If a folder or file exists, it safely skips or renames

## Usage

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/pdf-splitter.git
cd pdf-splitter

# 2. Set up a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your PDFs to this folder

# 5. Run the script
python split_pdf.py


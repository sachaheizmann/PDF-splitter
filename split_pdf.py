from pathlib import Path
from pypdf import PdfReader, PdfWriter
import shutil

# --- Config ---
working_dir = Path(".")
pages_per_split = 15
output_root = Path("output_slides")

# --- Helpers ---
def safe_move_pdf(pdf_path: Path, target_folder: Path) -> Path:
    target_folder.mkdir(parents=True, exist_ok=True)
    target_pdf_path = target_folder / pdf_path.name

    if not target_pdf_path.exists():
        shutil.move(str(pdf_path), target_pdf_path)
        return target_pdf_path
    else:
        base = pdf_path.stem
        suffix = 1
        while True:
            candidate = target_folder / f"{base}-copy{suffix}.pdf"
            if not candidate.exists():
                shutil.move(str(pdf_path), candidate)
                return candidate
            suffix += 1

def split_pdf(input_path: Path, output_dir: Path, chunk_size: int):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    base_name = input_path.stem
    for i in range(0, total_pages, chunk_size):
        writer = PdfWriter()
        for j in range(i, min(i + chunk_size, total_pages)):
            writer.add_page(reader.pages[j])
        part_path = output_dir / f"{base_name}-part{i // chunk_size + 1}.pdf"
        with open(part_path, "wb") as f:
            writer.write(f)
        print(f"Saved: {part_path}")

# --- Main ---
def process_all_pdfs():
    output_root.mkdir(exist_ok=True)
    for pdf_path in working_dir.glob("*.pdf"):
        folder_name = pdf_path.stem
        target_folder = output_root / folder_name

        # Move original PDF into its output folder
        final_pdf_path = safe_move_pdf(pdf_path, target_folder)

        # Skip already-split files
        if "-part" in final_pdf_path.stem:
            continue

        # Split
        split_pdf(final_pdf_path, target_folder, pages_per_split)

if __name__ == "__main__":
    process_all_pdfs()

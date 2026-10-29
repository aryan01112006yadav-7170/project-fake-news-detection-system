import os
import zipfile

source_dir = os.path.abspath(os.path.dirname(__file__))
downloads_dir = os.path.abspath(os.path.join(source_dir, ".."))

zip_filename = "Fake_News_Generator_and_Detector_Project.zip"
zip_path_downloads = os.path.join(downloads_dir, zip_filename)
zip_path_workspace = os.path.join(source_dir, zip_filename)

# Files and directories to include
include_files = [
    "Fake_News_Generator_and_Detector_Colab.ipynb",
    "app.py",
    "fact_checker.py",
    "README.md",
    "PRESENTATION_GUIDE.md",
    "requirements.txt",
    "download_isot_dataset.py",
    "generate_sample_data.py",
    "Fake.csv",
    "True.csv"
]

include_dirs = [
    "sample_data",
    "data"
]

print(f"Creating zip at: {zip_path_downloads}")

with zipfile.ZipFile(zip_path_downloads, "w", zipfile.ZIP_DEFLATED) as zipf:
    for fname in include_files:
        fpath = os.path.join(source_dir, fname)
        if os.path.exists(fpath):
            zipf.write(fpath, arcname=fname)
            print(f"Added file: {fname}")

    for dname in include_dirs:
        dpath = os.path.join(source_dir, dname)
        if os.path.exists(dpath):
            for root, _, files in os.walk(dpath):
                for f in files:
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, source_dir)
                    zipf.write(full_p, arcname=rel_p)
                    print(f"Added: {rel_p}")

# Also copy/create in workspace for convenience
import shutil
shutil.copy2(zip_path_downloads, zip_path_workspace)

print(f"\n[+] Successfully created ZIP file at:\n  1. {zip_path_downloads}\n  2. {zip_path_workspace}")
size_kb = os.path.getsize(zip_path_downloads) / 1024
print(f"[+] Total Archive Size: {size_kb:.2f} KB")

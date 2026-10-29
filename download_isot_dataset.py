"""
ISOT News Dataset Downloader / Preprocessor
Academic Session 2026-2027 | BCS752 Internship Assessment Lab
Student: ARYAN (Roll No: 2300640100026)
Hindustan College of Science and Technology (HCST), Mathura
"""

import os
import sys
import pandas as pd

def check_or_setup_data():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    sample_dir = os.path.join(target_dir, "sample_data")
    
    fake_csv = os.path.join(target_dir, "Fake.csv")
    true_csv = os.path.join(target_dir, "True.csv")
    
    if os.path.exists(fake_csv) and os.path.exists(true_csv):
        print("[+] Fake.csv and True.csv already present in root directory.")
        df_fake = pd.read_csv(fake_csv)
        df_true = pd.read_csv(true_csv)
        print(f"[+] Loaded: Fake={len(df_fake)} rows, True={len(df_true)} rows.")
        return
        
    sample_fake = os.path.join(sample_dir, "Fake.csv")
    sample_true = os.path.join(sample_dir, "True.csv")
    
    if os.path.exists(sample_fake) and os.path.exists(sample_true):
        print("[*] Copying benchmark dataset from sample_data/ ...")
        pd.read_csv(sample_fake).to_csv(fake_csv, index=False)
        pd.read_csv(sample_true).to_csv(true_csv, index=False)
        print("[+] Benchmark dataset prepared successfully.")
    else:
        print("[*] Generating new sample dataset...")
        import generate_sample_data
        print("[+] Datasets generated.")

if __name__ == "__main__":
    check_or_setup_data()

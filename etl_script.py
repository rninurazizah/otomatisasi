import pandas as pd
import os

def run_etl():
    print(" Memulai proses ETL...")
    
    # 1. Read (Extract)
    raw_path = "data/raw_data.csv"
    output_path = "data/clean_data.csv"
    if not os.path.exists(raw_path):
        print(f"File {raw_path} tidak ditemukan!")
        return
        
    df = pd.read_csv(raw_path)
    print(f"Data awal ({len(df)} baris):")
    print(df.head())

    # 2. Transform (Cleaning & Processing)
    # Contoh: Hapus baris kosong & duplikat
    df_clean = df.dropna().drop_duplicates()
    
    # Contoh: Rapikan nama kolom (huruf kecil & hapus spasi)
    # Perbaikan: sesuaikan variabel pemanggil dan variabel perulangannya
    df_clean.columns = [col.strip().lower().replace(" ", "_") for col in df_clean.columns]

    # 3. Load (Save Result)
    output_path = "data/clean_data.csv"
    df_clean.to_csv(output_path, index=False)
    print(f" Proses ETL selesai! Data bersih disimpan ke {output_path} ({len(df_clean)} baris).")

if __name__ == "__main__":
    run_etl()

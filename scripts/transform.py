import pandas as pd
from pathlib import Path

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage et transformation des données extraites"""
    
    # Suppression des doublons
    df = df.drop_duplicates()
    
    # Suppression des lignes avec des valeurs critiques manquantes
    df = df.dropna(subset=["First Name", "Last Name", "Email"])
    
    # Normalisation des chaînes
    df["Country"] = df["Country"].str.strip().str.title()
    df["Technology"] = df["Technology"].str.strip().str.title()
    df["Seniority"] = df["Seniority"].str.strip().str.title()
    
    # Conversion de la date
    df["Application Date"] = pd.to_datetime(df["Application Date"], errors="coerce")
    
    # Conversion des colonnes numériques
    numeric_cols = ["YOE", "Code Challenge Score", "Technical Interview Score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
    
    # Nettoyage des emails 
    df["Email"] = df["Email"].str.strip().str.lower()
    
    # Statistiques basiques
    print("Données transformées :")
    print(df.info())
    
    return df

if __name__ == "__main__":
    # Charger le fichier brut
    raw_path = Path("data/raw/candidates.csv")
    df_raw = pd.read_csv(raw_path, sep=";")
    
    # Transformation
    df_clean = transform_data(df_raw)
    
    # Sauvegarde du fichier nettoyé
    output_path = Path("data/processed/candidates_clean.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(output_path, index=False)
    print(f"Données nettoyées sauvegardées dans {output_path}")

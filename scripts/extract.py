import pandas as pd

def extract_data(path: str) -> pd.DataFrame:
    """Lire le fichier CSV brut et le charger en DataFrame"""
    df = pd.read_csv(path, sep=';')  
    print(f"{len(df)} lignes chargées depuis {path}")
    return df

if __name__ == "__main__":
    df = extract_data("data/raw/candidates.csv")
    print(df.head())

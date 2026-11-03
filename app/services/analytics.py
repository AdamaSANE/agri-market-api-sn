import pandas as pd
from typing import List, Dict

def calculate_market_averages(data: List[Dict]) -> Dict:
    """
    Transforme une liste de dictionnaires en DataFrame Pandas 
    pour calculer les prix moyens par marché.
    """
    if not data:
        return {"message": "Aucune donnée disponible pour l'analyse"}

    # 1. Ingestion : Conversion de la liste de dict (JSON-like) en DataFrame
    df = pd.DataFrame(data)

    # 2. Analyse : Calcul de la moyenne des prix par marché et par produit
    # On groupe par marché et produit, on calcule la moyenne, on arrondit à l'entier (FCFA)
    avg_df = df.groupby(['market', 'product'])['price_cfa'].mean().round().astype(int).reset_index()

    # 3. Export : Reconversion en format dictionnaire pour l'API (FastAPI)
    # L'orientation 'records' produit une structure [{...}, {...}] idéale pour le JSON
    result = avg_df.to_dict(orient='records')
    
    return {"analysis_type": "Market Averages", "data": result}
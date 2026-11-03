from fastapi import FastAPI, HTTPException
from app.models.schemas import PriceCreate
from app.services.analytics import calculate_market_averages
from app.core.config import supabase  # Import de notre connexion base de données

app = FastAPI(
    title="AgriMarket API Sénégal",
    description="API DaaS pour le suivi et l'analyse des prix agricoles.",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Bienvenue sur AgriMarket API Sénégal 🇸🇳", "database": "Connectée"}

# Route POST : Ajouter un vrai prix dans Supabase
# Route POST : Ajouter un vrai prix dans Supabase
@app.post("/api/prices", tags=["Prices"])
def add_price(price_data: PriceCreate):
    
    # 1. On récupère les données sous forme de dictionnaire Python standard
    data_to_insert = price_data.model_dump()
    
    # 2. On force la conversion de la date Pydantic en chaîne de caractères (string)
    data_to_insert['date_recorded'] = str(data_to_insert['date_recorded'])
    
    # Appel à l'API Supabase pour insérer la ligne
    response = supabase.table("prices").insert(data_to_insert).execute()
    
    if not response.data:
        raise HTTPException(status_code=400, detail="Erreur lors de l'insertion dans la base")
        
    return response.data[0]

# Route GET : Récupérer tous les prix depuis Supabase
@app.get("/api/prices", tags=["Prices"])
def get_all_prices():
    response = supabase.table("prices").select("*").execute()
    data = response.data
    return {"total_records": len(data), "data": data}

# Route Analytique : Pandas + Supabase
@app.get("/api/analytics/averages", tags=["Analytics"])
def get_market_averages():
    # 1. Extraction des données brutes depuis la base
    response = supabase.table("prices").select("*").execute()
    data = response.data
    
    # 2. Transformation et calcul des moyennes via Pandas
    analysis_result = calculate_market_averages(data)
    return analysis_result
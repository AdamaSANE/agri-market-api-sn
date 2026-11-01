from fastapi import FastAPI

# Initialisation de l'application (Ces métadonnées apparaîtront dans la documentation)
app = FastAPI(
            title="AgriMarket API Sénégal",
            description="API DaaS pour le suivi et l'analyse des prix agricoles sur les marchés sénégalais.",
            version="1.0.0"
)

# Route racine (Health Check) pour vérifier que le serveur tourne
@app.get("/", tags=["Health"])
def read_root():
    return {
        "message": "Bienvenue sur AgriMarket API Sénégal 🇸🇳", 
        "status": "online",
        "documentation": "/docs"
    }
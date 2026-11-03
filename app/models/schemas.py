from pydantic import BaseModel, Field
from datetime import date

# Modèle de base pour un relevé de prix
class PriceBase(BaseModel):
    market: str = Field(..., description="Nom du marché (ex: Sandaga, Diaobé)")
    product: str = Field(..., description="Nom de la denrée (ex: Oignon, Riz brisé)")
    price_cfa: int = Field(..., gt=0, description="Prix au kilo en FCFA (doit être > 0)")
    date_recorded: date

# Modèle utilisé lors de la réception d'une requête POST
class PriceCreate(PriceBase):
    pass

# Modèle utilisé pour renvoyer la réponse (avec un ID généré)
class PriceResponse(PriceBase):
    id: int
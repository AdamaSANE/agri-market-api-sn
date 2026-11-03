import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Charge les variables cachées dans le fichier .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Création de l'instance client Supabase unique
def get_supabase_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Les clés Supabase sont introuvables dans le fichier .env")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialisation du client
supabase = get_supabase_client()
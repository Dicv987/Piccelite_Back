import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)

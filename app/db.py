from .config import get_supabase_client

supabase = get_supabase_client()

def test_connection():
    response = supabase.table("test_table").select("*").execute()
    return response

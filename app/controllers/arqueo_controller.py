from ..db import supabase
from ..models.inventory_models import ArqueoModel

# Obtener todos los arqueos
def get_arqueos():
    return supabase.table("arqueo").select("*").execute().data

# Obtener arqueo por ID
def get_arqueo_by_id(arqueo_id: int):
    return supabase.table("arqueo").select("*").eq("id", arqueo_id).execute().data

# Crear arqueo (el cálculo de diferencia debe hacerse previamente)
def create_arqueo(arqueo: ArqueoModel):
    return supabase.table("arqueo").insert(arqueo.dict()).execute().data

# Eliminar arqueo
def delete_arqueo(arqueo_id: int):
    return supabase.table("arqueo").delete().eq("id", arqueo_id).execute().data

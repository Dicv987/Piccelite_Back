from ..db import supabase
from ..models.inventory_models import SucursalModel

# Obtener todas las sucursales
def get_sucursales():
    return supabase.table("sucursales").select("*").execute().data

# Obtener sucursal por ID
def get_sucursal_by_id(sucursal_id: int):
    return supabase.table("sucursales").select("*").eq("id", sucursal_id).execute().data

# Crear una nueva sucursal
def create_sucursal(sucursal: SucursalModel):
    return supabase.table("sucursales").insert(sucursal.dict()).execute().data

# Actualizar una sucursal existente
def update_sucursal(sucursal_id: int, sucursal: SucursalModel):
    return supabase.table("sucursales").update(sucursal.dict()).eq("id", sucursal_id).execute().data

# Eliminar una sucursal
def delete_sucursal(sucursal_id: int):
    return supabase.table("sucursales").delete().eq("id", sucursal_id).execute().data

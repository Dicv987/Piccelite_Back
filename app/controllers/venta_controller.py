from ..db import supabase
from ..models.inventory_models import VentaModel

# Obtener todas las ventas
def get_ventas():
    return supabase.table("venta").select("*").execute().data

# Obtener venta por ID
def get_venta_by_id(venta_id: int):
    return supabase.table("venta").select("*").eq("id", venta_id).execute().data

# Crear una nueva venta
def create_venta(venta: VentaModel):
    return supabase.table("venta").insert(venta.dict()).execute().data

# Actualizar una venta
def update_venta(venta_id: int, venta: VentaModel):
    return supabase.table("venta").update(venta.dict()).eq("id", venta_id).execute().data

# Eliminar una venta
def delete_venta(venta_id: int):
    return supabase.table("venta").delete().eq("id", venta_id).execute().data
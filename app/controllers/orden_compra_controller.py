from ..db import supabase
from ..models.inventory_models import OrdenCompraModel

# Obtener todas las ordenes de compra
def get_ordenes_compra():
    return supabase.table("orden_compra").select("*").execute().data

# Obtener orden de compra por ID
def get_orden_compra_by_id(orden_id: int):
    return supabase.table("orden_compra").select("*").eq("id", orden_id).execute().data

# Crear una nueva orden de compra
def create_orden_compra(orden: OrdenCompraModel):
    return supabase.table("orden_compra").insert(orden.dict()).execute().data

# Actualizar una orden de compra
def update_orden_compra(orden_id: int, orden: OrdenCompraModel):
    return supabase.table("orden_compra").update(orden.dict()).eq("id", orden_id).execute().data

# Eliminar una orden de compra
def delete_orden_compra(orden_id: int):
    return supabase.table("orden_compra").delete().eq("id", orden_id).execute().data

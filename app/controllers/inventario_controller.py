from ..db import supabase
from ..models.inventory_models import InventarioModel

# Obtener inventario completo
def get_inventario():
    return supabase.table("inventario").select("*").execute().data

# Obtener inventario por sucursal
def get_inventario_by_sucursal(sucursal_id: int):
    return supabase.table("inventario").select("*").eq("sucursal_id", sucursal_id).execute().data

# Obtener inventario por producto en sucursal específica
def get_producto_inventario(producto_id: int, sucursal_id: int):
    return supabase.table("inventario").select("*").eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute().data

# Actualizar cantidad manualmente (ej. por ajustes)
def update_inventario(producto_id: int, sucursal_id: int, cantidad: int):
    return supabase.table("inventario").update({"cantidad": cantidad}).eq("producto_id", producto_id).eq("sucursal_id", sucursal_id).execute().data

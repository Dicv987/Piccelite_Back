from ..db import supabase
from ..models.inventory_models import ProductoModel

# Obtener todos los productos
def get_productos():
    return supabase.table("productos").select("*").execute().data

# Obtener producto por ID
def get_producto_by_id(producto_id: int):
    return supabase.table("productos").select("*").eq("id", producto_id).execute().data

# Crear un nuevo producto
def create_producto(producto: ProductoModel):
    return supabase.table("productos").insert(producto.dict()).execute().data

# Actualizar un producto existente
def update_producto(producto_id: int, producto: ProductoModel):
    return supabase.table("productos").update(producto.dict()).eq("id", producto_id).execute().data

# Eliminar un producto
def delete_producto(producto_id: int):
    return supabase.table("productos").delete().eq("id", producto_id).execute().data

from ..db import supabase
from ..models.inventory_models import ArqueoDetalleModel

# Crear detalle de arqueo (la diferencia se calcula antes de enviar)
def create_arqueo_detalle(detalle: ArqueoDetalleModel):
    return supabase.table("arqueo_detalle").insert(detalle.dict()).execute().data

# Obtener detalles por ID de arqueo
def get_detalles_by_arqueo(arqueo_id: int):
    return supabase.table("arqueo_detalle").select("*").eq("arqueo_id", arqueo_id).execute().data

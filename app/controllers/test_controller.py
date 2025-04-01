from ..db import supabase
from ..models.test_model import TestModel

def get_test_data():
    response = supabase.table("test_table").select("*").order("id").execute()
    return response.data

def get_test_data_by_id(test_id: int):
    response = supabase.table("test_table").select("*").eq("id", test_id).execute()
    return response.data

def create_test_data(test_data: TestModel):
    response = supabase.table("test_table").insert(test_data.dict()).execute()
    return response.data

def update_test_data(test_id: int, test_data: TestModel):
    response = supabase.table("test_table").update(test_data.dict()).eq("id", test_id).execute()
    return response.data

def delete_test_data(test_id: int):
    response = supabase.table("test_table").delete().eq("id", test_id).execute()
    return response.data

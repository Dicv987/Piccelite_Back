from fastapi import APIRouter
from ..controllers import test_controller
from ..models.test_model import TestModel

router = APIRouter()

@router.get("/test")
def read_test_data():
    return test_controller.get_test_data()

@router.get("/test/{test_id}")
def read_test_data_by_id(test_id: int):
    return test_controller.get_test_data_by_id(test_id)

@router.post("/test")
def create_test_data(test_data: TestModel):
    return test_controller.create_test_data(test_data)

@router.put("/test/{test_id}")
def update_test_data(test_id: int, test_data: TestModel):
    return test_controller.update_test_data(test_id, test_data)

@router.delete("/test/{test_id}")
def delete_test_data(test_id: int):
    return test_controller.delete_test_data(test_id)

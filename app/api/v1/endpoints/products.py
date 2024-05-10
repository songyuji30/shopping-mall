
# items.py
from typing import List
from fastapi import APIRouter, Path, Depends, HTTPException

from app import schemas, crud
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create_product(*, db=Depends(deps.get_db), product_in: schemas.ProductCreate):
  """
  새로운 product 생성
  """
  product = crud.crud_product.create(db=db, obj_in=product_in)
  if product is None:
    raise HTTPException(status_code=400, detail="Item already registered")
  return product

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(
  *,
  db=Depends(deps.get_db), 
  product_id: int = Path(..., description="아이템 ID")
):
  """
  product id로 product 조회
  """
  db_product = crud.crud_product.get(db, product_id=product_id)
  if db_product is None:
    raise HTTPException(status_code=404, detail="Product not found")
  return db_product


@router.get("/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db=Depends(deps.get_db)):
  '''
  product 목록 조회
  '''
  products = crud.crud_product.get_multi(db, skip=skip, limit=limit)
  return products


@router.put("/{product_id}", response_model=schemas.Product)
def update_item(*, db=Depends(deps.get_db), product_id: int, product_in: schemas.ProductUpdate):
  '''
  product id로 product 수정
  '''
  product = crud.crud_product.get(db, product_id=product_id)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  product = crud.crud_product.update(db, db_obj=product, obj_in=product_in)
  return product

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(*, db=Depends(deps.get_db), product_id: int):
  '''
  product id로 product 삭제
  '''
  product = crud.crud_product.get(db, product_id=product_id)
  if not product:
    raise HTTPException(status_code=404, detail="Product not found")
  product = crud.crud_product.remove(db, product_id=product_id)
  return product
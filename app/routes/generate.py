import json
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Dict, Any
from fastapi import Request

from pydantic import BaseModel

class Base(BaseModel):
    constructorTitle: str

router = APIRouter(prefix='/generate')

@router.post('/')
async def generate_document(payload: Request):
  try:
      res = await payload.json()
      print(res)
      return res
  except json.JSONDecodeError:
      raise HTTPException(400, "Invalid JSON format")
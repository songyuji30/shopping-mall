# main.py
from fastapi import FastAPI
from app.api.v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 미들웨어 설정
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

API_V1_STR = "/api/v1"
# API 라우터 추가
app.include_router(api_router, prefix=API_V1_STR)

# 선택적: 루트 경로에 대한 간단한 테스트 엔드포인트
@app.get("/")
def root():
  return {"message": "Hello World from FastAPI"}


import uvicorn

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080)
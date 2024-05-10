from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# PostgreSQL 연결 정보 설정
SQLALCHEMY_DATABASE_URL = settings.get_database_url()

# PostgreSQL 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
Base = declarative_base()
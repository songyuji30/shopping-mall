import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.session import Base

@pytest.fixture(scope="function")
def db_session():
  engine = create_engine("sqlite:///./test.db")
  Base.metadata.create_all(bind=engine)
  TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  session = TestingSessionLocal()

  try: 
    yield session
  finally:
    session.close()
    Base.metadata.drop_all(bind=engine) # 테스트 후 데이터베이스 정리
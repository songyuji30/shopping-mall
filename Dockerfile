# Docker 컨테이너에 사용할 기본 이미지 설정
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}

# 컨테이너 내부의 작업 디렉토리 설정
WORKDIR /app

# poetry.lock과 pyproject.toml 파일을 작업 디렉토리로 복사
COPY poetry.lock pyproject.toml ./ 

# Poetry 설치 및 프로젝트 종속성 설치
RUN pip install --upgrade pip
RUN pip install poetry
RUN pip install pydantic
RUN poetry config virtualenvs.create false
# pyproject.toml 파일에 맞게 poetry.lock 파일을 업데이트합니다.
RUN poetry lock 
RUN poetry install --no-root

# 프로젝트 전체 디렉토리를 작업 디렉토리로 복사
COPY . .

# 컨테이너의 8080 포트 노출
EXPOSE 8080

# 컨테이너 시작 시 실행할 명령 설정
CMD ["./entrypoint.sh"]
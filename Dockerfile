# pull official base image
FROM python:3.10-alpine
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# 작업 디렉토리 설정
WORKDIR /app
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
# 종속 요소 복사본을 만들어서 종속 요소 설치
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# 프로젝트 복제
COPY . .
# 컨테이너의 포트 8000을 노출하고 마이그레이션 및 서버 실행
EXPOSE 8000
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver","0.0.0.0:8000"]


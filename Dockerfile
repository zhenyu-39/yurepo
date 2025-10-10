FROM python:3.12.0-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir django==5.2.6  # 安装和本地一致的Django版本
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
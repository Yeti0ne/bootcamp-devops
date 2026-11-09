FROM python:3.12-slim
RUN useradd --uid 10001 --no-create-home appuser
WORKDIR /app
COPY app.py .
USER 10001
EXPOSE 8000
CMD ["python", "app.py"]

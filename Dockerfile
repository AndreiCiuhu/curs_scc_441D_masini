FROM python:3.12-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "masini.py", "run", "--host=0.0.0.0", "--port=5000"]

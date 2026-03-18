from fastapi import FastAPI
import redis
import os

app = FastAPI()

# Railway сам подставит правильный URL базы в переменную REDIS_URL
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.from_url(REDIS_URL)

@app.get("/")
def read_root():
    return {"message": "Привет! Это мой проект в облаке Railway!"}

@app.get("/status")
def get_status():
    try:
        r.ping()
        return {"status": "Redis доступен ✅"}
    except Exception as e:
        return {"status": "Ошибка базы ❌", "details": str(e)}

@app.get("/test-data")
def test_data():
    # Записываем тестовое значение и тут же его читаем
    r.set("last_visit", "now")
    val = r.get("last_visit")
    return {"redis_data": val}  

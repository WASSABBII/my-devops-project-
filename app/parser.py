import time
import redis

print("Пробую подключиться к Redis...")
# 'my-db' — это имя сервиса из твоего docker-compose.yml
r = redis.Redis(host='my-db', port=6379)

while True:
    try:
        r.ping()
        print("Успех! База данных Redis доступна.")
    except Exception as e:
        print(f"Ошибка: Не могу достучаться до базы: {e}")
    time.sleep(5) 

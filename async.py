import asyncio
import aiohttp
import time

urls = ["https://httpbin.org/get"] * 10  # 10 одинаковых запросов для примера

# Синхронные запросы
def sync_requests():
    import requests
    start = time.time()
    for url in urls:
        requests.get(url).status_code
    return time.time() - start

# Асинхронные запросы
async def async_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        start = time.time()
        for url in urls:
            tasks.append(session.get(url))
        responses = await asyncio.gather(*tasks)
        return time.time() - start

# Запуск
print(f"Синхронные запросы: {sync_requests():.2f} сек")
print(f"Асинхронные запросы: {asyncio.run(async_requests()):.2f} сек")
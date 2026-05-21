import threading
import time

def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)
        time.sleep(1)  # Имитация долгой операции записи

# Синхронная запись
start = time.time()
for i in range(5):
    write_file(f"sync_file_{i}.txt", "Hello")
sync_time = time.time() - start
print(f"Синхронная запись: {sync_time:.2f} сек")

# Многопоточная запись
start = time.time()
threads = []
for i in range(5):
    t = threading.Thread(target=write_file, args=(f"thread_file_{i}.txt", "Hello"))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
thread_time = time.time() - start
print(f"Многопоточная запись: {thread_time:.2f} сек")
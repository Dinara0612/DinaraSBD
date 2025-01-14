import time
import requests


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} seconds.')




import time
import threading
import requests
def read_example() -> None:
 response = requests.get('https://www.example.com')
 print(response.status_code)
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)
thread_start = time.time()
thread_1.start()
thread_2.start()
print('Все потоки работают!')
thread_1.join()
thread_2.join()
thread_end = time.time()
print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')



import time
from functools import wraps
def timethis(func):
 @wraps(func)
 def wrapper(*args, **kwargs):
 start = time.time()
 result = func(*args, **kwargs)
 end = time.time()
 print(func.__name__, end-start)
 return result
 return wrapper

 def f(x, y):
             return x * y
 result = f(7, 8)
 print(result)

 
 

 

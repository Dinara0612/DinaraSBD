import time
from functools import wraps
import pickle

# Декоратор, который выводит время выполнения
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} отработала за {end - start:.8f} секунд")
        return result
    return wrapper


@timethis
def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Загрузка модели
rf1 = load_model("rf_model.pkl")

# Прогноз
data = [[1, 1, 0]]
prediction = rf1.predict(data)
print(f"Прогноз для {data}: {prediction}")

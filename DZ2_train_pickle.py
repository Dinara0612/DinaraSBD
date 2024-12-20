import time
from functools import wraps
from sklearn.ensemble import RandomForestClassifier
import pickle


X = [[0, 0, 0], [0, 0, 1],[1, 1, 0],[0, 1, 1]]
Y = ["t", "t", "f", "f"]

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


# Обучение модели
@timethis
def train_model(X, Y):
    clf = RandomForestClassifier(n_estimators=10)
    return clf.fit(X, Y)

clf = train_model(X, Y)

# Сохранение модели
@timethis
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

save_model(clf, "rf_model.pkl")

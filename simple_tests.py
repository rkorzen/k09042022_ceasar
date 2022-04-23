def add(a, b):
    return a + b


print(__name__)
if __name__ == "__main__":
    print("wykonuje testy")
    assert add(1, 2) == 3

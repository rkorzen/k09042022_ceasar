a: str

a = "ala"
a = 1


def add(a: int, b: int) -> int:

    return a + b


print(add(1, 2))
print(add("a", "b"))


def add2(a: int, b: int) -> int:
    a = float(a)
    result = a + b
    return result

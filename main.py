result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a менша за b")
        if b > 100:
            raise IndexError("b більша за 100")
        return a / b
    except ZeroDivisionError as e:
        print("ZeroDivisionError: ", e)
        return None
    except ValueError as e:
        print("ValueError: ", e)
        return None
    except IndexError as e:
        print("IndexError: ", e)
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 17: 15, 8: 4}
for key in data:
    try:
        res = divider(int(key), int(data[key]))
        if res is not None:
            result.append(res)
    except TypeError as e:
        print("TypeError: ", e)

print(result)

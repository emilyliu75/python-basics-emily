def assert_equals(value_1, value_2) -> bool:
    return value_1 == value_2


def assert_true(value) -> bool:
    return bool(value)


def assert_greater_than(value_1: int, value_2: int) -> bool:
    if not isinstance(value_1, int) or not isinstance(value_2, int):
        raise TypeError(
            "At least one of the values supplied is not an integer"
        )
    return value_1 > value_2


print(f'Are 2 and 2 equal? {assert_equals(2, 2)}')
print(f'Are True and False equal? {assert_equals(True, False)}')
print(f'Is "hello" and "hello" equal? {assert_equals("hello", "hello")}')
print(f'Is 2 and 2.0 equal? {assert_equals(2, 2.0)}')
print(f'Is type(2) and type(2.0) equal? {assert_equals(type(2), type(2.0))}')

print(f'Is 2 == 2 true? {assert_true(2 == 2)}')

print(f'Is 20 greater than 10? {assert_greater_than(20, 10)}')
try:
    print(
        f'Is "hello" greater than "hi"? {assert_greater_than(
            "hello", "hi"
        )}')
except TypeError as e:
    print(e)

print("Execution finished!")

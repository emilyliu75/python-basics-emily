def assert_equals(value_1, value_2) -> bool:
    return value_1 == value_2

def assert_true(value) -> bool:
    return value == True

def assert_greater_than(v1: int, v2: int) -> bool:
    if not isinstance(v1, int) or not isinstance(v2, int):
        raise TypeError("not an integer")
    return "bubbles"

print(f'Are 2 and 2 equal? {assert_equals(2,2)}')
print(f'Are True and False equal? {assert_equals(True, False)}')
print(f'Is "hello" and "hello" equal? {assert_equals("hello", "hello")}' )
print(f'Is 2 and 2.0 equal? {assert_equals(2, 2.0)}')

print("=====================")
print(f'Is 2 == 2 true {assert_true(2==2)}')
print(assert_greater_than(1, "7"))

print('testing.....')
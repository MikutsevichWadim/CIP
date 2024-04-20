def have_common_divisor(a:int, b:int) -> bool:
    for i in range(2, min(a, b)+1):
        if (a % i == 0) and (b % i == 0):
            return True
    return False

def number_no_common_divisor(a:int, min_b:int) -> int:
    b = min_b
    while True:
        if not have_common_divisor(a, b):
            return b
        b += 1
        
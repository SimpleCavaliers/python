# 两数相除的结果(不能用除法)
def divide(dividend: int, divisor: int) -> int:
    result, temp_result, temp_divisor, temp_dividend, temp = 0, 0, divisor, dividend, (2 ** 31) - 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        temp = -(2 ** 31)
    temp_dividend = abs(dividend)
    temp_divisor, divisor = abs(divisor), abs(divisor)
    while temp_divisor <= temp_dividend:
        temp_result += 1
        while (temp_divisor << 1) <= temp_dividend:
            temp_divisor = temp_divisor << 1
            temp_result = temp_result << 1
        result += temp_result
        if result >= abs(temp):
            return temp
        temp_result = 0
        temp_dividend -= temp_divisor
        temp_divisor = divisor
    if temp == -(2 ** 31):
        return -result
    return result


if __name__ == '__main__':
    print(divide(3543, 453))

def factorial(num)-> int:
    result = num
    if result == 0 or result ==1:
        return 1
    else:
        while (num > 1) : 
            num = num -1
            result = result * num; 
    return result

print(factorial(-5))
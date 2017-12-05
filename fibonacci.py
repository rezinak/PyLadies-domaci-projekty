

def get_Fibonacci(numberofdigits):
    fibonacci = [1, 1]
    if numberofdigits == 0:
        fibonacci = []
    elif numberofdigits == 1:
        fibonacci = [1]
    elif numberofdigits == 2:
        fibonacci = fibonacci

    for i in range(numberofdigits - 2):
        new_member = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(new_member)
    return fibonacci


print_me_Fib = get_Fibonacci(2)
print(print_me_Fib)

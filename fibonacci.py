def fibonacci(n):
    if n < 0:
        raise ValueError("Invalid index!")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

def fibonacci_ittter(n):
    if n < 0:
        raise ValueError("Invalid index!")
    else:
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a+b
        return a

def fibonacci_list(n):
    if n < 0:
        raise ValueError("Invalid index!")
    elif n == 0:
        return [0]
    a = [0, 1]
    for i in range(2, n+1):
        a.append(a[i-1]+a[i-2])
    return a

if __name__ == '__main__':
    a = int(input('Enter a number: '))
    print(fibonacci(a))
    print(fibonacci_iter(a))
    print(fibonacci_list(a))
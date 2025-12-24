#1 
def fibonacci(n):
    # return a list of fibonacci numbers
    value = []
    for i in range(n):
        
        fibonacci = i + i - 1
        value.append(fibonacci)
    return value

n = int(input())
print(list(map(cube, fibonacci(n))))
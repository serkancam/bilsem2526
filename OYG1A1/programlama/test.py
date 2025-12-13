def f(n):
    if n<2:
        return 1
    return f(n-1)+f(n-2)

def f2(n):
    if n>5:
        print(n)
    return f2(n+1)


print(f2(1))


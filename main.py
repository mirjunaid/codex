class Fibonacci:
    a = int(input('Enter the starting number of your fibonacci series: '))
    b = int(input('Enter the second number of your fibonacci series: '))
    n = int(input('Enter no of terms of series: '))
    result = 0
    print(f'First {n} terms of this series are: ')
    print(a)

    def fib(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
    for j in range(n):
        result = a + b
        a = b
        b = result
        j += 1
        print(result)


fibonacci = Fibonacci()
print(fibonacci)

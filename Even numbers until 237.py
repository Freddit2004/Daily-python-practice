def EvenNumbers(numbers):
    evens = []
    for n in numbers:
       if n == 237:
           break
       if n % 2 == 0:
            evens.append(n)
    return evens
    
print(EvenNumbers(numbers))
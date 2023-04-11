n = int(input('введите трёхзначное число: '))
print(n)
sum = 0
while n > 0:
    m = n % 10
    sum += m 
    n //= 10
print('сумма трёхзначного числа: ', sum)
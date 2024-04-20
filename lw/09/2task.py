message = 'СТАНКЕВИЧ'


b_func = lambda y, k, T, p: (y**k*T)%p
T_func = lambda b, a, p, x: (b * a**(p-1-x))%p

abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

g = 3
p = 17
x = 2
k = 7
a = g**k%p
y = g**x%p

for letter in message:
    T = abc.index(letter)
    b = b_func(y, k, T, p)
    print(letter, T, b, sep='\t', end='\t')
    T = T_func(b, a, p, x)
    print(T)

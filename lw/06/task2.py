# from lol import have_common_dividers

messages = (
    'КУРОВСКИЙ',
    'КУРОВСКИП',
    'УКРОВСКИЙ',
)

# 25. p=23, q=11, n=p*q=253
# M = Шапский, M = {25, 0, 16, 18, 11, 9, 10}
# H0=100
# H1=(100+25)2mod 253=192
# H2=(192+0)2mod 253 =179
# H3=(179+16)2mod 253=75
# H4=(75+18)2mod 253=47
# H5=(47+11)2mod 253=75
# H6=(75+9)2mod 253=225
# H7=(225+10)2mod 253=71
# Таким образом h(M)=H7=71

abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def hash(message, p, q, h0):
    m = list(map(abc.index, message))
    n = p*q
    h = [h0,]
    print(f'p={p}, q={q}, n=p*q={n}')
    print(f'M = {message}, M = ', end='{')
    print(*(i for i in m), sep=', ', end='}\n')
    print(f'H0 = {h0}')
    for hi in range(len(m)):
        h.append((h[hi]+m[hi])**2 % n)
        print(f'H{hi+1} = ({h[hi]} + {m[hi]})² mod {n} = {h[hi+1]}')
    return h[1:]


for message in messages:
    print(message)
    hash(
        message = message,
        p = 7,
        q = 23,
        h0 = 100,
    )
    print('='*10)

import re

def btd(bit_string):
    bits = re.sub(r'[^01]', '', bit_string)

    return int(bits, 2)


class BinDecLet:

    def __init__(self):

        # русский алфавит в upper-case
        self.abc = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        # :добавлено ё
        self.abcfull = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

        # dec-код, соответствующий по индексу буквам русского
        # алфавита согласно кодировке символов Windows 1251
        self.dec = list(range(192,224))

        self.bin = list(map(lambda x: bin(x), self.dec.copy()))

        self.data = {
            type(str()): self.abc,
            type(int()): self.dec,
            type(bytes()): self.bin,
        }

    def __call__(self, symbol, to_type):
        index = self.data[type(symbol)].index(symbol)
        return self.data[to_type][index]

binDecLet = BinDecLet()

def encrypt2modulo(string, key):
    i = 0
    string_len = len(string)
    key_len = len(key)

    print('Буква','Dec-код','Bin-код\t','Буква','Dec-код','Bin-код\t','Dec-код','Bin-код',sep='\t')

    while i < string_len:

        # open message
        string_let = string[i]
        string_let_dec = binDecLet(string_let, int)
        string_let_bin = binDecLet(string_let, bytes)

        # gamma
        key_let = key[i%key_len]
        key_let_dec = binDecLet(key_let, int)
        key_let_bin = binDecLet(key_let, bytes)

        # cipher
        cipher_bin = bin(int(string_let_bin, 2) ^ int(key_let_bin, 2))
        cipher_dec = int(cipher_bin, 2)

        print(
            string_let,
            string_let_dec,
            string_let_bin[2:].rjust(8, '0'),
            key_let,
            key_let_dec,
            key_let_bin[2:].rjust(8, '0'),
            cipher_dec,
            cipher_bin[2:].rjust(8, '0'),
            sep='\t')
        
        i += 1

def encrypt33modulo(string, key):
    i = 0
    string_len = len(string)
    key_len = len(key)

    print('Буква','Dec-код','Буква','Dec-код','Буква','Bin-код',sep='\t')

    while i < string_len:

        # open message
        string_let = string[i]
        string_let_dec = binDecLet.abcfull.index(string_let)

        # gamma
        key_let = key[i%key_len]
        key_let_dec = binDecLet.abcfull.index(key_let)

        # cipher
        cipher_let_dec = (string_let_dec + key_let_dec) % 32
        cipher_let = binDecLet.abcfull[cipher_let_dec]

        print(
            string_let,
            string_let_dec,
            key_let,
            key_let_dec,
            cipher_let,
            cipher_let_dec,
            sep='\t')
        
        i += 1


string = 'СТАНКЕВИЧ'
arr = (
    '''    1 Антонюк
    2 Апанович
    3 Беспалов
    4 Берней
    5 Бородич
    6 Войтулевич
    7 Дубравский
    8 Дудинский
    9 Зубарь
    10 Касмина
    11 Костюк
    12 Куровский
    13 Лебедь
    14 Леута
    15 Макей
    16 Мандрикевич
    17 Микуцевич
    18 Михайловский
    19 Михно
    20 Ольховик
    21 Остроух
    22 Сенкевич
    23 Соколовский
    24 Трахтенберг
    25 Шапский    '''
)
arr = list(map(lambda x: x.split()[1].upper(), arr.split('\n')))


key = 'КЛЮЧ'

encrypt2modulo(string, key)
print('='*10)
encrypt33modulo(string, key)

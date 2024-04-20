import math

class CipheredMessage(str):

    def __init__(self, message):
        self.message = list(message)

    def __len__(self):
        return len(self.message)
    
    def brute_force(self, start_step, end_step):
        for step in range(start_step, end_step):
            decrypted_message = self.decrypt(step)
            if self.message[0] == decrypted_message[0]:
                yield step, decrypted_message
    
    def decrypt(self, step):

        decrypted_message = ''
        decryption_table = []

        width = step
        height = math.ceil(len(self) / width)
        size = width*height
        difference = size - len(self)
        x = 0
        while x < width:
            y = 0
            while y < height:
                symbol_index = x+y*width-max(difference-height+y, 0)
                decrypted_message += self.message[symbol_index]
                if len(decrypted_message) == len(self):
                    return decrypted_message
                y += 1
            x += 1

ciphered_message = CipheredMessage(
    'ЛЕСЕПЕУЕОНЬНЯПЗННМИЬУИЩЮДТКРТЮБПОХЕИООИФАЕНШЕИБЕВООИЩЕАСРНИЛВЯОЦСАЕЗТОЙИММРЕЗСТАИСЬАИРИТРНАЫ'
)

for decrypt_set in ciphered_message.brute_force(1, 100):
    print(decrypt_set)

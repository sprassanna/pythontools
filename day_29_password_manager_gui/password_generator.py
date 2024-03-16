import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|',
                      ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']

letters_rn = random.randint(3, 5)
numbers_rn = random.randint(2, 4)
spec_char_rn = random.randint(4, 6)


class PasswordGenerator:

    def __init__(self):
        self.unique_password = ''

    def generate_password(self):

        self.unique_password += ''.join([random.choice(LETTERS) for _ in range(letters_rn)])
        self.unique_password += ''.join([str(random.choice(NUMBERS)) for _ in range(numbers_rn)])
        self.unique_password += ''.join([random.choice(SPECIAL_CHARACTERS) for _ in range(spec_char_rn)])

        return  ''.join(random.sample(self.unique_password, len(self.unique_password)))

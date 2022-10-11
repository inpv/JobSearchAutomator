import string
import random
from datas.strings import Strings


class Crypt:

    @staticmethod
    def decipher(text, key):
        shift = 26 - (key + 1)  # shifting the symbols

        alpha_lower = string.ascii_lowercase  # loading lowercase letters
        alpha_upper = string.ascii_uppercase  # loading uppercase letters

        # shifting each of the alphabets by the desired amount
        shifted_alphabet_lower = alpha_lower[shift:] + alpha_lower[:shift]
        shifted_alphabet_upper = alpha_upper[shift:] + alpha_upper[:shift]

        alphabet = alpha_lower + alpha_upper  # merging them into one
        shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper  # the shifted ones too

        table = str.maketrans(alphabet, shifted_alphabet)  # creating a corresponding symbols table

        decoded_text = text.translate(table)  # coding according to the correspondence table

        return decoded_text

    @staticmethod
    def get_random_decrypted_pass():
        passwd = random.choice(Strings.strings)
        pass_index = Strings.strings.index(passwd)
        final_pass = Crypt.decipher(passwd, pass_index)

        return final_pass

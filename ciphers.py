import numpy as np

class CaesarCipher():
    def __init__(self) -> None:
        """
        Creates a Caesar Cipher object. The default shift is 3.
        """
        self.shift = 3

    def set_shift(self, shift: int) -> None:
        """
        Sets the shift used to generate the Caesar Cipher.

        Args:
            shift (int): The shift used to generate the Caesar Cipher.
        """
        self.shift = shift

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Caesar Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """
        ciphertext = ''
        for letter in plaintext:
            if letter.isalpha():
                ciphertext += chr((ord(letter.upper()) + self.shift - 65) % 26 + 65)
            else:
                ciphertext += letter
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Caesar Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """
        

class KeyedCaeserCipher():
    def __init__(self) -> None:
        self.key = 'Caesar'

    def set_key(key: str) -> None:
        

class SimpleSubstitutionCipher():

    def __init__(self) -> None:
        """
        Creates a Simple Substitution Cipher object with the default key 'XYZABCDEFGHIJKLMNOPQRSTUVW'.
        """
        self.key = 'XYZABCDEFGHIJKLMNOPQRSTUVW'

    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Simple Substitution Cipher.

        Args:
            key (str): The key used to generate the Simple Substitution Cipher.
        """
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Simple Substitution Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """


    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Simple Substitution Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """



class AffineCipher():
    """
    An Affine Cipher object. 
    """
    def __init__(self) -> None:
        """
        Creates an Affine Cipher object with the specified exponent and addend.

        Args:
            exponent (int): The exponent in the affine function.
            addend (int): The addend in the affine function.

        """   
        self.exponent = 1
        self.addend = 3

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Affine Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """
        
    
    def decrypt(self, plaintext: str) -> str:
        """
        Decrypts a message using the Affine Cipher.

        Args:
            plaintext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        
    
class HillCipher():
    def __init__(self) -> None:
        """
        Creates a Hill Cipher object.
        """
        self.key = None
        self.key_matrix = None
        self.inverse_key_matrix = None

    def get_key(self) -> str:
        """
        Returns the key used to generate the Hill Cipher.

        Returns:
            str: The key used to generate the Hill Cipher.
        """
        return self.key
    
    def set_key(self, key: np.array) -> None:
        """
        Sets the key used to generate the Hill Cipher.

        Args:
            key (np.array): The key used to generate the Hill Cipher.
        """
        self.key = key
        self.key_matrix = np.array([[ord(letter) - 65 for letter in row] for row in key])
        self.inverse_key_matrix = np.linalg.inv(self.key_matrix)

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Hill Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
        ciphertext = ''
        for i in range(0, len(plaintext), len(self.key_matrix)):
            plaintext_vector = np.array([[ord(letter) - 65] for letter in plaintext[i:i+len(self.key_matrix)]])
            ciphertext_vector = np.dot(self.key_matrix, plaintext_vector) % 26
            for letter in ciphertext_vector:
                ciphertext += chr(letter[0] + 65)
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Hill Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        plaintext = ''
        for i in range(0, len(ciphertext), len(self.key_matrix)):
            ciphertext_vector = np.array([[ord(letter) - 65] for letter in ciphertext[i:i+len(self.key_matrix)]])
            plaintext_vector = np.dot(self.inverse_key_matrix, ciphertext_vector) % 26
            for letter in plaintext_vector:
                plaintext += chr(letter[0] + 65)
        return plaintext
    
class VigenereCipher():
    def __init__(self) -> None:
        """
        Creates a Vigenere Cipher object with the specified key.

        Args:
            key (str): The key used to generate the Vigenere Cipher.
        """
    
    def get_key(self) -> str:
        """
        Returns the key used to generate the Vigenere Cipher.

        Returns:
            str: The key used to generate the Vigenere Cipher.
        """
        return self.key
    
    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Vigenere Cipher.

        Args:
            key (str): The key used to generate the Vigenere Cipher.
        """
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Vigenere Cipher.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Vigenere Cipher.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
    
class OneTimePad():
    def __init__(self, key: str) -> None:
        """
        Creates a One Time Pad object with the specified key.

        Args:
            key (str): The key used to generate the One Time Pad.
        """
        self.key = key
    
    def get_key(self) -> str:
        """
        Returns the key used to generate the One Time Pad.

        Returns:
            str: The key used to generate the One Time Pad.
        """
        return self.key
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the One Time Pad.

        Args:
            plaintext (str): The message to encrypt.

        Returns:
            str: The encrypted message.
        """

        self.key = 
        
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the One Time Pad.

        Args:
            ciphertext (str): The message to decrypt.

        Returns:
            str: The decrypted message.
        """
        
    
class PlayfairCipher():
    def __init__(self) -> None:
        """
        Creates a Playfair Cipher object.
        """

    def get_key(self) -> str:
        """
        Returns the key used to generate the Playfair Cipher.

        Returns:
            str: The key used to generate the Playfair Cipher.
        """
        return self.key
    
    def set_key(self, key: str) -> None:


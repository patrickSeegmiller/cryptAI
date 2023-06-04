import numpy as np

class CaesarCipher():
    def __init__(self) -> None:
        """
        Creates a Caesar Cipher object capable of encrypting and decrypting messages using the Caesar Cipher.
        A Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter
        some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B
        would be replaced by E, and so on. The Caesar Cipher is named for Julius Caesar, who is purported to have used
        it to communicat with his generals. The default key is 3. 
        """

        # Initialize the alphabet and the shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = 3

    def set_key(self, key: int) -> None:
        """
        Sets the shift used to generate the Caesar Cipher.

        Args:
            key (int): The key used to generate the Caesar Cipher.
        """
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Caesar Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, adding the shift, and then finding
        # the character in the ciphertext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) + self.key) % 26]
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Caesar Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """
        
        # Check that the ciphertext is a non-empty string
        if not isinstance(ciphertext, str) or len(ciphertext) == 0:
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Initialize the plaintext as an empty string
        plaintext = ''

        # Iterate over each character in the ciphertext, decrypting it and adding it to the plaintext by
        # finding the index of the character in the ciphertext alphabet, subtracting the shift, and then finding
        # the character in the plaintext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in ciphertext:
            if char.upper() in self.alphabet:
                plaintext += self.alphabet[(self.alphabet.index(char.upper()) - self.shift) % 26]
            else:
                plaintext += char

        # Return the plaintext
        return plaintext
    
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

class KeyedCaeserCipher():
    def __init__(self) -> None:
        """
        Creates a Keyed Caesar Cipher object capable of encrypting and decrypting messages using the Keyed Caesar Cipher.
        A Keyed Caesar Cipher is a special case of the Caesar Cipher that uses a key to generate a new alphabet. For
        example, if the key is 'ZEBRAS', then the alphabet would be 'ZEBRASCDFGHIJKLMNOPQTUVWXY'. The key is then used
        to encrypt and decrypt messages using the new alphabet.
        """
        self.key = None
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Keyed Caesar Cipher. Then converts the key to an alphabet by removing 
        duplicate letters and then appending the remaining letters of the alphabet in order. Then assigns the 
        resulting alphabet to the alphabet attribute.

        Args:
            key (str): The key to convert to an alphabet.

        Raises:
            ValueError: If the key is not a non-empty string.

        """
        # Check that the key is a non-empty string
        if not isinstance(key, str) or len(key) == 0:
            raise ValueError("Key must be a non-empty string.")
        
        # Assign the key to the key attribute for later retrieval or use
        self.key = key

        # Remove duplicate letters from the key
        key = ''.join(sorted(set(key), key=key.index))

        # Append the remaining letters of the alphabet in order
        for char in self.alphabet:
            if char not in key:
                key += char
        
        # Set the alphabet attribute to the key
        self.alphabet = key

    def get_key(self) -> str:
        """
        Returns the key used to generate the Keyed Caesar Cipher.

        Returns:
            str: The key used to generate the Keyed Caesar Cipher.
        """
        return self.key

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts a message using the Keyed Caesar Cipher.
        
        Args:
            plaintext (str): The message to encrypt.
        
        Returns:
            str: The encrypted message.
        """

        # Check that the plaintext is a non-empty string
        if not isinstance(plaintext, str) or len(plaintext) == 0:
            raise ValueError("Plaintext must be a non-empty string.")
        
        # Initialize the ciphertext as an empty string
        ciphertext = ''

        # Iterate over each character in the plaintext, encrypting it and adding it to the ciphertext by
        # finding the index of the character in the plaintext alphabet, adding the shift, and then finding
        # the character in the ciphertext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in plaintext:
            if char.upper() in self.alphabet:
                ciphertext += self.alphabet[(self.alphabet.index(char.upper()) + self.shift) % 26]
            else:
                ciphertext += char
        
        # Return the ciphertext
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts a message using the Keyed Caesar Cipher.
        
        Args:
            ciphertext (str): The message to decrypt.
        
        Returns:
            str: The decrypted message.
        """
        
        # Check that the ciphertext is a non-empty string
        if not isinstance(ciphertext, str) or len(ciphertext) == 0:
            raise ValueError("Ciphertext must be a non-empty string.")
        
        # Initialize the plaintext as an empty string
        plaintext = ''

        # Iterate over each character in the ciphertext, decrypting it and adding it to the plaintext by
        # finding the index of the character in the ciphertext alphabet, subtracting the shift, and then finding
        # the character in the plaintext alphabet at that index. Characters not in the alphabet are left
        # unchanged.
        for char in ciphertext:
            if char.upper() in self.alphabet:
                plaintext += self.alphabet[(self.alphabet.index(char.upper()) - self.shift) % 26]
            else:
                plaintext += char

        # Return the plaintext
        return plaintext

class SimpleSubstitutionCipher():
    def __init__(self) -> None:
        """
        Creates a Simple Substitution Cipher object with the default key 'XYZABCDEFGHIJKLMNOPQRSTUVW'. 
        The Caesar Cipher, the Atbash Cipher, the Affine Cipher, and the Keyed Caesar Cipher are all special cases of the
        Simple Substitution Cipher. Due to the nature of the Simple Substitution Cipher, the key must be a permutation
        of the alphabet. The key defaults to a classic Caesar Cipher with a shift of 3.
        """
        self.key = 'XYZABCDEFGHIJKLMNOPQRSTUVW'

    def set_key(self, key: str) -> None:
        """
        Sets the key used to generate the Simple Substitution Cipher.

        Args:
            key (str): The key used to generate the Simple Substitution Cipher.

        Raises:
            ValueError: If the key is not a non-empty string or is not a permutation of the alphabet.
        """

        # Check that the key is a non-empty string
        if not isinstance(key, str) or len(key) == 0:
            raise ValueError("Key must be a non-empty string.")
        # Check that the key is a permutation of the alphabet
        elif sorted(key) != sorted(self.alphabet):
            raise ValueError("Key must be a permutation of the alphabet.")

        self.key = key

    def get_key(self) -> str:
        """
        Returns the key used to generate the Simple Substitution Cipher.

        Returns:
            str: The key used to generate the Simple Substitution Cipher.
        """
        return self.key

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


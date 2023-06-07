# A virtual implementation of the Enigma cipher machine.

import string
import random

class Rotor():
    def __init__(self, set_type=None) -> None:
        """
        Initializes a rotor with the default settings. The default settings are:
        - The wiring is a random permutation of the alphabet.
        - The position is 0.
        - The ring setting is 0.
        - The notch is 0.
        """
        if set_type == None:
            self.permutation = random.shuffle("".join(string.ascii_uppercase))
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "I":
            self.permutation = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.position = 0
            self.ring_setting = 0
            self.notch = 16
        elif set_type == "II":
            self.permutation = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.position = 0
            self.ring_setting = 0
            self.notch = 4
        elif set_type == "III":
            self.permutation = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.position = 0
            self.ring_setting = 0
            self.notch = 21
        elif set_type == "IV":
            self.permutation = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            self.position = 0
            self.ring_setting = 0
            self.notch = 9
        elif set_type == "V":
            self.permutation = "VZBRGITYUPSDNHLXAWMJQOFECK"
            self.position = 0
            self.ring_setting = 0
            self.notch = 25
        elif set_type == "VI":
            self.permutation = "JPGVOUMFYQBENHZRDKASXLICTW"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "VII":
            self.permutation = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "VIII":
            self.permutation = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Beta":
            self.permutation = "LEYJVCNIXWPBQMDRTAKZGFUHOS"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Gamma":
            self.permutation = "FSOKANUERHMBTIYCWLQPZXVGJD"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Reflector A":
            self.permutation = "EJMZALYXVBWFCRQUONTSPIKHGD"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Reflector B": 
            self.permutation = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Reflector C": 
            self.permutation = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Reflector B Thin":
            self.permutation = "ENKQAUYWJICOPBLMDXZVFTHRGS"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        elif set_type == "Reflector C Thin":
            self.permutation = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
            self.position = 0
            self.ring_setting = 0
            self.notch = 0
        else:
            raise ValueError("Invalid rotor type.")
    
       


    def generate_permutation(self) -> None:
        """
        Generates a random permutation of the alphabet and stores it as the wiring of the rotor. The permutation is generated
        by shuffling the alphabet.
        """

        # Generate a random permutation of the alphabet.
        permutation = list(string.ascii_uppercase)
        random.shuffle(permutation)

        # Set the wiring and generate the inverse.
        self.set_wiring("".join(permutation))

    def set_position(self, position: int) -> None:
        """
        Sets the position of the rotor. The position should be an integer between 0 and 25, inclusive. The position represents
        the letter that is currently at the top of the rotor.
        """
        self.position = position 

    def set_ring_setting(self, ring_setting: int) -> None:
        """
        Sets the ring setting of the rotor. The ring setting should be an integer between 0 and 25, inclusive. The ring setting
        adds a constant offset to the position of the rotor. For example, if the ring setting is 5 and the position is 0, then
        the rotor will behave as if the position is 5.
        """
        
        self.ring_setting = ring_setting

    def set_notch(self, notch: int) -> None:
        """
        Sets the notch of the rotor. The notch should be an integer between 0 and 25, inclusive. The notch represents the
        position of the rotor at which the next rotor will rotate. For example, if the notch is 5, then the next rotor will
        rotate when the position of this rotor is 5.
        """
        pass

    def set_wiring(self, wiring: str) -> None:
        """
        Sets the wiring of the rotor. The wiring should be a string of 26 unique letters. The wiring represents the permutation
        of the alphabet that the rotor implements. For example, if the wiring is "EKMFLGDQVZNTOWYHXUSPAIBRCJ", then the letter
        "A" will be mapped to "E", "B" will be mapped to "K", "C" will be mapped to "M", etc.

        The inverse of the wiring is automatically generated and stored as well.
        """

        # Check that the wiring is a string of 26 unique letters.
        if not isinstance(wiring, str) or len(wiring) != 26 or len(set(wiring)) != 26:
            raise ValueError("wiring must be a string of 26 unique letters.")
        
        # Set the wiring and generate the inverse.

        pass

    def get_position(self) -> int:
        """
        Returns the position of the rotor. The position is an integer between 0 and 25, inclusive. The position represents
        the letter that is currently at the top of the rotor.

        Returns:
            int: The position of the rotor.
            
        """

        return self.position

    def get_ring_setting(self) -> int:
        pass

    def get_notch(self) -> int:
        """
        Returns the notch of the rotor. The notch is an integer between 0 and 25, inclusive. The notch represents the
        position of the rotor at which the next rotor will rotate. As mentioned above, if the notch is 5, then the next rotor will
        rotate when the position of this rotor is 5.
        """

        return self.notch

    def get_wiring(self) -> str:
        pass

    def rotate(self) -> bool:
        """
        Rotates the rotor by one position. If the position is 25, then the position is set to 0. A flag is returned to indicate
        whether or not the next rotor should rotate as well.
        """

        # Rotate the rotor by one position mod 26.
        self.position = (self.position + 1) % 26
        
        # Return a flag indicating whether or not the next rotor should rotate based on whether or not the notch is at the
        # current position.
        if self.position == self.notch:
            return True

class Plugboard():
    def __init__(self, number_of_plugs=0) -> None:
        """
        Initializes a plugboard with the default settings.
        """
        self.number_of_plugs = number_of_plugs
        self.permutation_dict = {letter: letter for letter in string.ascii_uppercase}


    def set_wiring(self, wiring: str) -> None:
        pass

    def get_wiring(self) -> str:
        pass

    def get_wiring_inverse(self) -> str:
        pass

class EnigmaMachine():
    def __init__(self, number_of_rotors: int = 3, number_of_plugs: int = 10) -> None:
        pass
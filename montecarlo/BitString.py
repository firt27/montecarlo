import numpy as np
import math

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        """Constructor
        
        Parameters
        ----------
        N: number of bits
        """
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        """Convert bitstring to string
        
        Parameters
        ----------
        None

        Returns
        -------
        selfString : string
            string representation of bitstring
        """
        selfString = ''
        for bit in self.config:
            selfString += str(bit)
        return selfString

    def __eq__(self, other):
        """Checks equality of two bitstrings
        
        Parameters
        ----------
        other : BitString
            other bitstring
        
        Returns
        -------
        : bool
            boolean value representing equality
        """
        return (self.config == other.config).all()
    
    def __len__(self):
        """Length of the bitstring

        Parameters
        ----------
        None

        Returns
        -------
        : int
            length of bitstring
        """
        return self.N

    def on(self):
        """Counts number of bits equal to 1

        Parameters
        ----------
        None

        Returns
        -------
        : int
            number of bits equal to 1
        """
        num_on = 0
        for bit in self.config:
            if bit == 1:
                num_on += 1
        return num_on
    
    def off(self):
        """Counts number of bits equal to 0
        
        Parameters
        ----------
        None
        
        Returns
        -------
        : int
            number of bits equal to 0"""
        num_off = 0
        for bit in self.config:
            if bit == 0:
                num_off += 1
        return num_off
    
    def flip_site(self,i):
        """Flips the value of the bitstring at the specified site
        
        Parameters
        ----------
        i : int
            index of bit to be flipped
        
        Returns
        -------
        None
        """
        self.config[i] ^= 1
    
    def int(self):
        """Gives the integer corresponding to the bitstring
        
        Parameters
        ----------
        None
        
        Returns
        -------
        : int
            integer corresponding to bitstring
        """
        return int(str(self), 2)
  
    def set_config(self, s:list[int]):
        """Sets the bitstring equal to a given list of bits
        
        Parameters
        ----------
        s : list[int]
            list of bits
        
        Returns
        -------
        None
        """
        self.config = s
        
    def set_int_config(self, dec:int):
        """Configures the bitstring so it corresponds to a given integer
        
        Parameters
        ----------
        dec : int
        
        Returns
        -------
        None
        """

        self.config = np.zeros(self.N, dtype=int) 

        i = 1
        while dec != 0:
            self.config[-i] = dec % 2
            dec = dec // 2
            i += 1
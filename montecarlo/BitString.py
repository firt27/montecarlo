import numpy as np
import math

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        selfString = ''
        for bit in self.config:
            selfString += str(bit)
        return selfString

    def __eq__(self, other):
        return (self.config == other.config).all()
    
    def __len__(self):
        return self.N

    def on(self):
        num_on = 0
        for bit in self.config:
            if bit == 1:
                num_on += 1
        return num_on
    
    def off(self):
        num_off = 0
        for bit in self.config:
            if bit == 0:
                num_off += 1
        return num_off
    
    def flip_site(self,i):
        self.config[i] ^= 1
    
    def int(self):
        return int(str(self), 2)
  
    def set_config(self, s:list[int]):
        self.config = s
        
    def set_int_config(self, dec:int):

        self.config = np.zeros(self.N, dtype=int) 

        i = 1
        while dec != 0:
            self.config[-i] = dec % 2
            dec = dec // 2
            i += 1
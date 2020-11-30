class Fraction:
    
    # Automatically called whenever I use/intiialize/instantiate/create a Fraction object
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    # Automatically called whenever I print() a Fraction object
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def multiply(self, fraction):
        new_numer = self.numer * fraction.numer
        new_denom = self.denom * fraction.denom
        return Fraction(new_numer, new_denom)
    
def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a
 
def nww(a, b):
    return (a*b)/nwd(a, b)
 
class Ulamek:
    """
    Klasa ułamków
    
    Args:
        licznik(int): licznik
        mianownik(int): mianownik
    Attributes:
        licznik(int): licznik
        mianownik(int): mianownik
    Methods:
        __str__(self): zwraca ulamek w formie tekstu l/m
        __add__(self, other): dodaje do ulamka self ulamek other
        __eq__(self, other): sprawdza czy ulamki są równe
        
    Raises:
        AssertionError: Nieprawidłowy typ zmiennych lub mianownik równy 0
    """
    def __init__(self, licznik, mianownik):
        self.__licznik = licznik
        self.__mianownik = mianownik
        self.reduce()
    
    def reduce(self):
        """skraca ułamek do najprostszej postaci"""
        if self.__mianownik < 0:
            self.__mianownik *= -1
            self.__licznik *= -1
        dzielnik = nwd(self.__licznik, self.__mianownik)
        if dzielnik != 1:
            licznik = int(self.__licznik / dzielnik)
            mianownik = int(self.__mianownik / dzielnik)
            self.__licznik = licznik
            self.__mianownik = mianownik
    
    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'
    
    def __add__(self, other):
        assert type(other) == Ulamek, 'Other musi być typu Ulamek'
        omianownik = other.__mianownik
        olicznik = other.__licznik
        if self.__mianownik == omianownik:
            self.__licznik += olicznik
        else:
            wielokrotnosc = nww(self.__mianownik, omianownik)
            k = int(wielokrotnosc / self.__mianownik)
            self.__licznik *= k
            self.__mianownik *= k
            k = int(wielokrotnosc / omianownik)
            olicznik *= k
            omianownik *= k
            self.__licznik += olicznik
        self.reduce()
        return self.__str__()
    
    def __eq__(self, other):
        assert type(other) == Ulamek, 'Other musi być typu Ulamek'
        if self.__licznik == other.__licznik and self.__mianownik == other.__mianownik:
            return True
        return False
    
    @property
    def licznik(self):
        return self.__licznik
    
    @licznik.setter
    def licznik(self, x):
        assert type(x) == int, 'licznik musi być typu int'
        self.__licznik = x
        
    @property
    def mianownik(self):
        return self.__mianownik
    
    @mianownik.setter
    def mianownik(self, x):
        assert type(x) == int, 'mianownik musi być typu int'
        assert x != 0, 'mianownik musi być różny od 0'
        self.__mianownik = x
     
    def __str__(self):
        return f'{self.__licznik}/{self.__mianownik}'
    def __repr__(self):
        return f'{self.__licznik}/{self.__mianownik}'

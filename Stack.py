class _StackNode:
    """prywatna klasa wezel"""
    def __init__(self, item):
        self.dane = item
        self.next = None

class Stack:
    """Implementacja stosu za pomoca listy dowiazanej z wykorzystaniem klasy wezel"""
    def __init__(self):
        """iicjalizacja"""
        self._head = None
        self._size = 0

    def isEmpty(self):
        """sprawdzenie czy stos jest pusty"""
        return self._size == 0
        # lub
        # return self.head is None

    def size(self):
        """zwraca rozmiar stosu"""
        return self._size

    def push(self, element):
        """wlozenie elementu na stos"""
        nowy = _StackNode(element)      # tworzymy nowy wezel
        nowy.next = self._head          # podwiazujemy pod niego aktualna glowe (czyli nasz stos)
        self._head = nowy               # glowa staje sie ten nowy wezel
        self._size += 1                 # zwiekszamy rozmiar stosu
        return

    def pop(self):
        """sciagniecie elementu ze stosu"""
        if self.isEmpty():
            print("operacja pop - Stos jest pusty!!!")
            return False              # ewentualnie wywolaj wyjatek np. assert
            # assert not self.isEmpty(), "Stos jest PUSTY!!!"
       
        self._head = self._head.next    # glowa staje sie nastepny wezel po aktualnej glowie
                                        # w niektorych jezykach programowania trzeba samodzielnie zwolnic pamiec, np. w C++ operacja delete
        self._size -= 1                 # zmniejszamy rozmiar stosu
        return 

    def top(self):
        """zwrocenie eleemntu ze szczytu stosu"""
        if self.isEmpty():
            print("operacja top - Stos jest pusty!!!")
            return False                # ewentualnie wywolaj wyjatek
        return self._head.dane          # zwracamy konkretna dane z naszej glowy

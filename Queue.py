class Node:
    """Klasa wezel - do pamietania pojedynczej danej."""
    def __init__(self, dane=None, next_node=None):
    # konstruktor - domyslnie oba pola maja specjalna wartosc None
    # next_node bedzie wskazywalo na kolejny wezel takiej samej postaci lub na None
        self.dane = dane
        self.next_node  = next_node
    def __str__(self):
        return str(self.dane)

class Queue:
    # Implementacja kolejki FIFO za pomoca listy dowiazanej. Zobacz do podrecznika Cormen et al.
    def __init__(self):
    # konstruktor - domyslnie zmienne _head (glowa) oraz _tail (ogon) maja specjalna wartosc None
    # rozmiar moze byc przydatny do obslugi bledow oraz sprawdzenia czy kolejka nie jest pusta
        self.size = 0
        self._head = None
        self._tail = None

    def isEmpty(self):
    # sprawdzenie czy kolejka FIFO jest pusta
        return self.size == 0

    def enqueue(self, dane):
    # wstawianie do kolejki FIFO - brak obslugi bledow (nadmiar)
        # zapamietujemy poprzdni ogon
        t=self._tail
        # ogonem staje sie nowo wstawiany wezel
        self._tail = Node(dane)
        # sa dwie mozliwosci
        if self.isEmpty() :
            # Jesli lista jest pusta, dany wezel staje sie tez pierwszym
            self._head = self._tail
        else:
            # Jesli lista nie jest pusta, nowy wezel ktory jest teraz ogonem podwiazujemy pod poprzedni ogon
            t.next_node = self._tail
        # zwiekszamy liczbe danych w kolejce FIFO
        self.size += 1

    def dequeue(self):
    # usuwanie z kolejki FIFO
        if self.isEmpty():
            raise ValueError("Kolejka FIFO jest pusta!")
        # glowa staje sie nastepnik glowy
        self._head = self._head.next_node
        # zmniejszamy liczbe danych w kolejce FIFO
        self.size -= 1
        # to ponizej naprawde nie jest potrzebne, ale jest to dodane dla celow dydaktycznych i przejrzystosci kodu
        if self.isEmpty():
            self._tail=None

    def first(self):
    # zwracanie elementu z kolejki FIFO
        if self.isEmpty():
            raise ValueError("Kolejka FIFO jest pusta!")
        return self._head.dane


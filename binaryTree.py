class Node:
    """Klasa Node - do pamietania pojedynczego wezla w drzewie"""
    def __init__(self, dane=None, left=None, right=None):
        self.dane = dane
        self.left_node = left
        self.right_node = right
        
class binaryTree:
    """Klasa drzewo binarne - istotna dana jest tylko korzen"""
    def __init__(self):
        self.korzen = None
        
    def _inorder(self,drzewo):
        
        if drzewo is not None:
            self._inorder(drzewo.left_node)
            print(drzewo.dane)
            self._inorder(drzewo.right_node)
        
    def inorder(self):
    #Wypisywanie w porzadku inorder dla korzenia - procedura zeewnetrzna
        self._inorder(self.korzen)
 
    def _postorder(self,drzewo):
    # Wypisywanie w porzadku postorder dla korzenia - procedura wewnetrzna
        if drzewo is not None:
            self._postorder(drzewo.left_node)
            self._postorder(drzewo.right_node)
            print(drzewo.dane)
        
    def postorder(self):
    #Wypisywanie w porzadku postorder dla korzenia - procedura zeewnetrzna
        self._postorder(self.korzen)
 
    def _breadthFirst(self,drzewo):
    # Wypisywanie metoda przeszukiwania wszerz - procedura wewnetrzna
    # korzystamy z kolejki FIFO (nieistotne jak zaimplementowanej!)
        q = Queue()
    # wkladamy do naszej kolejki FIFO korzen
        q.enqueue(drzewo)
    # odwiedzamy kazdy wezel w drzewie
        while not q.isEmpty():
    # wypisujemy i usuwamy to co jest na poczatku kolejki
            node = q.first()
            q.dequeue()
 
 
            print(node.dane)
 
 
            if node.left_node is not None:
                q.enqueue(node.left_node)
            if node.right_node is not None:
                q.enqueue(node.right_node)
 
    def breadthFirst(self):
        print('breadthFirst')
    # Wypisywanie metoda przeszukiwania wszerz - procedura zewnetrzna
        self._breadthFirst(self.korzen)
        
    def _preorder(self, drzewo):
        if drzewo is not None:
            print(drzewo.dane)
            self._preorder(drzewo.left_node)
            self._preorder(drzewo.right_node)
            
    def preorder(self):
        self._preorder(self.korzen)

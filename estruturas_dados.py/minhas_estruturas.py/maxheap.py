


class Maxheap():
    lista_heap:list
    num_elementos:int
    ultimo_elem:int
    def __init__(self, lista:list):
        self.lista_heap = lista.copy()
        self.num_elementos = len(lista)
        self.ultimo_elem = self.num_elementos -1
        self.__cria_heap__()

    
    def __organiza_heap_recursiva__(self, index:int)->None:
             filho_dir = 2*index  +2
             filho_esq = 2*index  +1

             if self.ultimo_elem >= filho_dir:
                maior_filho = filho_esq if self.lista_heap[filho_esq] > self.lista_heap[ filho_dir] else  filho_dir
             elif self.ultimo_elem >= filho_esq:
                 maior_filho = filho_esq 
             else:
                 return

             if self.lista_heap[index] < self.lista_heap[maior_filho]:
                 self.lista_heap[index], self.lista_heap[maior_filho] = self.lista_heap[maior_filho], self.lista_heap[index]  
                 self.__organiza_heap_recursiva__(maior_filho)      

    def __cria_heap__(self)->None:
        if self.num_elementos == 0:
            print("vetor vazio")
            return 
        for i in range ((self.num_elementos//2)-1 ,-1,-1):
            self.__organiza_heap_recursiva__(i)
                   
    
    def __organiza_heap_ascen__(self, item)->None:
        index_adicionado:int = self.ultimo_elem

        while index_adicionado != 0:
            pai_index: int = (index_adicionado-1)//2 #// é para divisão de inteiros

            if item > self.lista_heap[pai_index]:
                temp = self.lista_heap[pai_index]
                self.lista_heap[pai_index] = item
                self.lista_heap[index_adicionado] = temp
                index_adicionado = pai_index

    def retorna_maior(self)->int or float:
        item: int or float = self.lista_heap[0]
        self.lista_heap[0] = self.lista_heap.pop(self.ultimo_elem)
        self.__organiza_heap_recursiva__(0)     
        return item
    
    def ver_maior(self)->int or float:
        if self.num_elementos == 0:
            print("heap vazia")
            return -189893
        else:
           return self.lista_heap[0]
    
    def inserir_heap(self, item: int or float)->None:
        self.lista_heap.append(item)
        self.num_elementos += 1
        self.ultimo_elem += 1
        
        
    


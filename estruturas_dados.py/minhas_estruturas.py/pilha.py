
class Pilha():
   lista_pilha: list
   num_elemen: int
   topo: int 

   def __init__(self, lista: list):
        self.lista_pilha = lista.copy() 
        self.topo = len(lista) - 1
        self.num_elemen = len(lista)
   
   def __eq__(self, outra_pilha: object) -> bool:
       if not isinstance(outra_pilha, Pilha):
           print("operação de comparação deve ser realizada entre 2 pilhas")
           return False
       else:
           if self.num_elemen != outra_pilha.num_elemen:
               return False
           else:
               for i in self.lista_pilha:
                   if self.lista_pilha[i] != outra_pilha.lista_pilha[i]:
                     return False  
               return True
           
   def __add__ (self, outra_pilha: object) -> object:
        if not isinstance(outra_pilha, Pilha):
           print("operação de comparação deve ser realizada entre 2 pilhas")
           return False
        else:
            nova_pilha = Pilha(self.lista_pilha)
            nova_pilha.push_lista(outra_pilha.lista_pilha)
            return nova_pilha
   
   def pop(self):
       if (self.num_elemen == 0):
           print("pilha vazia")
           return
       item = self.lista_pilha.pop(self.topo)
       self.topo -= 1
       self.num_elemen -= 1
       return item
   
   def push_lista(self, lista:list)->None:
       self.lista_pilha.extend(lista)
       self.topo += len(lista)
       self.num_elemen += len(lista)
   
   def push_elem(self, item)->None:
       self.lista_pilha.append(item)
       self.topo += 1
       self.num_elemen += 1

   def topo_pilha(self):
       if (self.num_elemen == 0):
           print("pilha vazia")
           return None
       item = self.lista_pilha[self.topo]
       return item

   def vazio(self)->bool:
       return (self.num_elemen == 0)
   

       
pilha1 = Pilha([1,2,98,1982,1982])


for i in range(pilha1.num_elemen):
     print(pilha1.pop())


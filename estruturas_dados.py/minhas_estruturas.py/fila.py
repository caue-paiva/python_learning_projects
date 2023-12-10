

class Fila():
   lista_fila: list 
   num_items:int

   def __init__(self,lista:list):
      self.lista_fila = lista.copy()
      self.num_items = len(lista)

   def vazio(self)->bool:
      return (self.num_items == 0)

   def push_elem(self, item)->None:
      self.lista_fila.append(item)
      self.num_items += 1

   def push_lista(self, lista:list)->None:
      self.lista_fila.extend(lista)
      self.num_items += len(lista)
   
   def pop_lista(self):
      if self.vazio():
         print("fila vazia, nao da para remover")
         return None
      item = self.lista_fila.pop(0)
      self.num_items -= 1
      return item 
       

fila1 = Fila([])

print(fila1.vazio())
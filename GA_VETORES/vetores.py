from math import sqrt, acos



class Vetor():
   lista_coord: list  #templates das variaveis individuais de cada classe
   dimensoes: int 
   RAD_PARA_GRAUS: float  = 57.29 # const de conversao usado por todos elementos da classe

   def __init__(self, dimensoes:int):
      self.dimensoes = dimensoes
      self.lista_coord = [0] * dimensoes #inicializa a lista com 0 nas posicoes até dimensoes
   
   def __getitem__(self, index:int):
        if index <= self.dimensoes:
         return self.lista_coord[index]
        else:
           print("o Vetor nao tem essa dimensao")
   
   def __setitem__(self, index: int, valor):
       if index <= self.dimensoes:
         self.lista_coord[index] = valor
       else:
           print("o Vetor nao tem essa dimensao")
       
   def __add__(self, outro_vetor: object)->object:
      if isinstance(outro_vetor,Vetor):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("soma vetorial requer 2 Vetor de mesmo tamanho")
         else:
            novo_vetor = Vetor(self.dimensoes)
            for i in range(self.dimensoes):
               novo_vetor[i] = ( (self[i]) + (outro_vetor[i]) )
            return novo_vetor
         
      else:
         print("soma vetorial requer 2 Vetor da mesma classe")

   def __sub__(self, outro_vetor: object)->object:
      if isinstance(outro_vetor,Vetor):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("subtracao vetorial requer 2 Vetor de mesmo tamanho")
         else:
            novo_vetor = Vetor(self.dimensoes)
            for i in range(self.dimensoes):
               novo_vetor[i] = self[i] - outro_vetor[i]
            return novo_vetor       
      else:
         print("subtracao vetorial requer 2 Vetor da mesma classe")

   def __mul__(self, outro_vetor: object)->float:  #produto escalar: vetor1 * vetor2
      if isinstance(outro_vetor,Vetor):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("produto escalar requer 2 Vetor de mesmo tamanho")
         else:
            prod_escalar: float = 0
            for i in range(self.dimensoes):
               prod_escalar += (self[i] * outro_vetor[i])
            return  prod_escalar
      else:
         print("produto escalar requer 2 Vetor da mesma classe")

   def seta_valores(self, lista_coord: list): #enche um Vetor com uma lista de coordenadas (float ou int)
      if len(lista_coord) != self.dimensoes:
          print("o Vetor nao tem essa dimensao")
          return 
      else:
         for i in range(self.dimensoes):
            self.lista_coord[i] = lista_coord[i]

   def valores(self)->list:
      return self.lista_coord
   
   def dimensao(self)-> int:
      return self.dimensoes
   
   def modulo(self)->float: #modulo do Vetor
      soma: int = 0
      for i in range(self.dimensoes):
         soma += pow(self.lista_coord[i],2)
      return sqrt(soma)
   
   def angulo_rad(self, outro_vetor: object)->float:  #retorna o angulo entre 2 vetores  em radiano 
      if isinstance(outro_vetor,Vetor):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("calcular angulo requer 2 vetores de mesmo tamanho")
         else:
            modulo1: float = self.modulo()
            modulo2: float = outro_vetor.modulo()
            if modulo1 == 0 or modulo2 ==0:
               print("nao se pode calcular angulo de vetores nulos")
               return
            prod_escalar: float = self * outro_vetor
            return acos(prod_escalar/(modulo1*modulo2))       
      else:
         print("calcular angulo requer 2 vetores da mesma classe")
   
   def angulo_grau(self,outro_vetor:object)->float:
      return self.RAD_PARA_GRAUS * self.angulo_rad(outro_vetor)
   
   def normalizar(self)-> object: #retorna um Vetor paralelo ao atual porém com norma/modulo = 1
        novo_vetor = Vetor(self.dimensoes)
        modulo: float = self.modulo()
        if modulo == 0:
           print("nao e possivel normalizar um Vetor com modulo zero")
           return None
        
        for i in range(self.dimensoes):
           novo_vetor[i] = self[i]/modulo

        return novo_vetor

   
vetor1 = Vetor(2)

vetor2 = Vetor(2)

vetor1.seta_valores([1,2])

vetor2.seta_valores([2,-1])

vetor3 = vetor1.normalizar()

#print(prod_escalar)
print(vetor3.valores())
   

         

      
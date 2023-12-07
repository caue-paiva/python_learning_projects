from math import sqrt, acos

class vetores():
   lista_coord: list = []

   def __init__(self, dimensoes:int):
      self.dimensoes = dimensoes
      for i in range(dimensoes):
         self.lista_coord[i] = 0
   
   def __getitem__(self, index:int):
        if index <= self.dimensoes:
         return self.lista_coord[index]
        else:
           print("o vetor nao tem essa dimensao")
   
   def __setitem__(self, index: int, valor):
       if index <= self.dimensoes:
         self.lista_coord[index] = valor
       else:
           print("o vetor nao tem essa dimensao")
       
   def __add__(self, outro_vetor: object)->object:
      if isinstance(outro_vetor,vetores):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("soma vetorial requer 2 vetores de mesmo tamanho")
         else:
            novo_vetor = vetores(self.dimensoes)
            for i in range(self.dimensoes):
               novo_vetor[i] = self[i] + outro_vetor[i]
            return novo_vetor
         
      else:
         print("soma vetorial requer 2 vetores da mesma classe")

   def __sub__(self, outro_vetor: object)->object:
      if isinstance(outro_vetor,vetores):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("subtracao vetorial requer 2 vetores de mesmo tamanho")
         else:
            novo_vetor = vetores(self.dimensoes)
            for i in range(self.dimensoes):
               novo_vetor[i] = self[i] - outro_vetor[i]
            return novo_vetor       
      else:
         print("subtracao vetorial requer 2 vetores da mesma classe")

   def __mod__(self, outro_vetor: object)->float:  #produto escalar: vetor1 % vetor2
      if isinstance(outro_vetor,vetores):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("produto escalar requer 2 vetores de mesmo tamanho")
         else:
            prod_escalar: float = 0
            for i in range(self.dimensoes):
               prod_escalar += (self[i] * outro_vetor[i])
            return  prod_escalar
      else:
         print("produto escalar requer 2 vetores da mesma classe")

   def coordenadas(self)->list:
      return self.lista_coord
   
   def dimensao(self)-> int:
      return self.dimensoes
   
   def modulo(self)->float:
      soma: int 
      for i in range(self.dimensoes):
         soma += pow(self.lista_coord[i],2)
      return sqrt(soma)
   
   def angulo(self, outro_vetor: object)->float:  #retorna o angulo entre 2 vetores  em radiano 
      if isinstance(outro_vetor,vetores):     
         if self.dimensoes != outro_vetor.dimensoes:
            print("calcular angulo requer 2 vetores de mesmo tamanho")
         else:
            modulo1: float = self.modulo()
            modulo2: float = outro_vetor.modulo()
            if modulo1 == 0 or modulo2 ==0:
               print("nao se pode calcular angulo de vetores nulos")
               return
            prod_escalar: float = self % outro_vetor
            return acos(prod_escalar/(modulo1*modulo2))       
      else:
         print("calcular angulo requer 2 vetores da mesma classe")
   

   

         

      
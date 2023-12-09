

"""d1: dict = {"aluno": "haha", "nota": 9}
d2: dict = {"aluno": "hghfha", "nota": 43}
d3: dict = {"aluno": "hsadsaha", "nota": 3}
lista_dict: list[dict] = [d1,d2,d3]

def nota_func(dict_in:dict)->int:
   return dict_in["nota"]
nota_fn  = lambda x : x["nota"] 


lista_dict.sort(key=nota_fn)"""
lista: list = [1,2,971,17828,1892,1082]
lista2 = [8,98,283]

lista.extend(lista2)

lista2[0] = -18928


print(lista )


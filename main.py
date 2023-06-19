from numpy.random import random as rand
import numpy

def get_random_int(max: int) -> int:
    return int(rand() * max)

def get_random_item(items:list[str])->str:
    return items[get_random_int(len(items))]

if __name__ == '__main__':
    estudantes : list[str] = [
        "Delfina Langa",
        "Gelson Matavela",
        "Daniela da Piedade",
        "Geraldo Nuvunga",
        "Murade Bin Lobo",
        "Valter Joaquim",
        "Leonilde Uisse",
        "Fausia Hleco",
        "Antonio Nhanombe",
        "Lucas Lucas",
        "Guift Jossene",
        "Constantino Jose",
        "Eduardo da Silva",
        "Felton Joaquim",
        "Djavs Tivane",
        "Amancio Mbahane",
        "Paulo Tivane",
        "Venildo Mesa",
        "Clayton Chilaule",
        "Eton Manhique"
    ]

    estudantes_escolhidos : list[str] = []

    while len(estudantes_escolhidos) < 9:
        # obter estudante
        estudante_escolhido : str = get_random_item(estudantes)
        # adicionar aos escolhidos
        estudantes_escolhidos.append(estudante_escolhido)
        # remover estudante dos estudantes
        estudantes.remove(estudante_escolhido)
        # reordenar a lista aleatoriamente
        numpy.random.shuffle(estudantes)
        
    print(estudantes_escolhidos)

# 1 - A pista apenas comporta 5 carros
# 2 - temsos 7 equipes com cada um possuindo dois carros, totalizando 14 carros
# 3 - Se o 1° carro da equipe ainda estiver na pista o 2° não pode entrar até que ele termine
# 4 - Cada pilote de carro deve dar 3 voltas pela pista
# 5 - Marcar quanto tempo cada volta foi concluida

import multiprocessing
import time
import random

posicoesPista: int = [0]*5
semaforo = None

def init(pistaFila, s):
    global posicoesPista
    global semaforo
    posicoesPista = pistaFila
    semaforo = s

def op(id):
    i: int = 0
    j: int = 0
    distanciaPercorrida: int = 0
    tempo: int = 0
    distancia: int = 200 # 200 metros
    # 5-25 m/s

    with semaforo:
        for i in range (2):
            posicoesPista[id] = id
            print('Carro', i+1, '/ Equipe',id+1, 'entrou na pista')
            for j in range (3):
                while (distanciaPercorrida <= distancia):
                    distanciaPercorrida += random.randint(5,25)
                    tempo += 1
                    time.sleep(1)
                print('Carro', i+1, '/ Equipe' ,id+1, 'fez', j+1, '° volta!')
                print('Tempo de volta do carro', i+1, '/ Equipe', id+1, '-', tempo, 's')
                distanciaPercorrida = 0
                tempo = 0
        print('Carro', i+1,'Equipe', id+1, 'saiu da pista')
            
def main():
    i: int = 0
    vetor_inical: int = [0]*7
    params: int = [0]*7

    for i in range (7):
        params[i] = i

    posicoesPista = multiprocessing.Array('i', vetor_inical)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(5)

        with multiprocessing.Pool(processes=7, initializer=init, initargs=(posicoesPista, semaforo)) as pool:
            pool.map(op, params)

if __name__ == '__main__':
    main()
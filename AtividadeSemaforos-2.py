#Quatro pessoas caminham, cada uma em um corredor diferente. Os 4 corredores terminam
#em uma única porta. Apenas 1 pessoa pode cruzar a porta, por vez. Considere que cada
#corredor tem 200m. e cada pessoa anda de 4 a 6 m/s. Cada pessoa leva de 1 a 2 segundos
#para abrir e cruzar a porta. Faça uma aplicação que simule essa situação.

import multiprocessing
import time
import random

semaforo: None
cruzarPorta: int = 0

def init(porta, s):
    global semaforo
    global cruzarPorta
    cruzarPorta = porta
    semaforo = s

def op(id):
    distanciaThread: int = 0
    distanciaTotal: int = 100

    while (distanciaThread < distanciaTotal):
        time.sleep(1)
        distanciaThread += random.randint(4, 6)
        print("Pessoa", id, "percorre: ",distanciaThread)
    print("Pessoa", id, "chegou a porta")

    with semaforo:
        cruzarPorta.value = id
        time.sleep(random.randint(1,2))
        print(("Pessoa", id, "cruzou a porta"))

def main ():
    params: int = [0]*4

    for i in range (4):
        params[i] = i
    print(params)

    acessoPorta = multiprocessing.Value('i', 0)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(acessoPorta, semaforo)) as pool:
            pool.map(op, params)
if __name__ == '__main__':
    main()
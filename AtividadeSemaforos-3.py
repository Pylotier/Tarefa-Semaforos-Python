import multiprocessing
import random

chegadaSapo: int = 0
sem = None

def init(posicaoSapo, s):
    global chegadaSapo
    global sem
    chegadaSapo = posicaoSapo
    sem = s

def main():
    i: int = 0
    num_threads: int = 0
    num_threads = 5
    param: int = [0]*5

    for i in range (5):
        param[i] = i

    chegadaSapo = multiprocessing.Value('i', 0)
    
    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)
        with multiprocessing.Pool(processes=num_threads, initializer=init, initargs=(chegadaSapo, semaforo)) as pool:
            pool.map(operacao, param)

def operacao(param):
    distanciaPercorrida: int = 0
    distanciaTotal: int = 45
    distaciaPulo: int = 0

    while (distanciaPercorrida < distanciaTotal):
        distaciaPulo = random.randint(0, 5)
        distanciaPercorrida += distaciaPulo
        print('Sapo', param+1, 'pulou', distaciaPulo, 'cm', '/// Distância percorrida:', distanciaPercorrida)
        
    with sem:
        chegadaSapo.value += 1
        print('Sapo', param+1, 'chegou em', chegadaSapo.value,'lugar')

        
if __name__ == '__main__':
    main()
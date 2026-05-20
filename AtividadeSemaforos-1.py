import multiprocessing
import time

sentidoCarro: int = 0
sem = None

def init(sen,s):
    global sentidoCarro
    global sem
    sentidoCarro = sen
    sem = s


def op(params):
    global sentidoCarro
    global sem

    with sem:
        sentidoCarro.value = params

        time.sleep(0.5)
        if (sentidoCarro.value == 0):
            print("Carro", params, "se movimenta para o SUL")
            time.sleep(0.5)
        elif(sentidoCarro.value == 1):
            print("Carro", params, "se movimenta para o NORTE")
            time.sleep(0.5)
        elif(sentidoCarro.value == 2):
            print("Carro", params, "se movimenta para o LESTE")
            time.sleep(0.5)
        else:
            print("Carro", params, "se movimenta para o OESTE")
            time.sleep(0.5)


def main():
    i = 0
    params: str = [0]*4
    semaforo: None

    for i in range(4):
        params[i] = i
    print(params)

    sentido = multiprocessing.Value('i', 0)

    with multiprocessing.Manager() as manager:
        semaforo = manager.Semaphore(1)

        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sentido, semaforo)) as pool:
            pool.map(op, params)



if __name__ == '__main__':
    main()

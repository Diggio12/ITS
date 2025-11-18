def cronometro(fun):
    def wrapper():
        import time
        start = time.time()
        fun()
        print(time.time()-start)

    return wrapper


def prova():
    print ('Ciao!')


def prova_2():
    print ('Ciao!')

prova = cronometro(prova)
prova_2 = cronometro(prova_2)

prova()
prova_2()
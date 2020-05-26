#Балыков А.Г
import matplotlib.pyplot as plt
import random

def Model():
    #Заполняем значения по умолчанию
    RazBuf = 1000
    N = 15
    P = 0
    MassVer = []
    SredVrem = []

    while P <= 1/N:

        Q = []
        m = 0
        MassVer.append(P)

        while m <= RazBuf:

            SumMessage = message(P, N)
            if len(Q) == 0:
                Q.append(0)
            elif Q[-1] <= 0:
                Q.append(SumMessage)
            else:
                Q.append(Q[-1] - 1 + SumMessage)
            m += 1

        VremOjid = sum(Q)
        SredVrem.append(0 if P == 0 else int(VremOjid/P))
        P += 0.01

    plt.plot(MassVer, SredVrem, color='g')
    plt.xlabel("Вероятность")
    plt.ylabel("Среднее время")
    plt.show()

def message(P, N):

    summa = 0
    for n in range(N):
        summa += random.choices([1, 0], [float(P), float(1 - P)])[0]

    return summa


if __name__ == '__main__':
    Model()

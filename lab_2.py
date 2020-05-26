#Балыков А.Г
import matplotlib.pyplot as plt
import random

def Model():
    #Заполняем значения по умолчанию
    RazBuf = 500
    N = 11
    P = 0.005
    MassVer = []
    SredVrem = []

    while P <= 1/N:

        m = 0
        collision = 0
        SumVremOjid = 0
        MassVer.append(P)

        while m <= RazBuf:
            messages_sum = message(P, N)
            #При отправке двух сообщений случаеются коллизии
            if messages_sum > 1:
                collision += messages_sum
            SumVremOjid += messages_sum
            m += 1

        SredVrem.append(float(collision / SumVremOjid))
        P += 0.005

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

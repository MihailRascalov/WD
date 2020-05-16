import numpy as np
import matplotlib.pyplot as plt

class Kostka_wyjatki(Exception):
    pass

def rzuc_kostka(n):
    try:
        if(n<=0):
            raise Kostka_wyjatki
        
        lista_sum = []
        while(n>0):
            x = np.random.randint(1, 7)
            y = np.random.randint(1, 7)
            lista_sum.append(x + y)
            n -= 1

        plt.hist(lista_sum, bins=11, facecolor='r', alpha=0.75, density=True)
        plt.xlabel('Suma wyrzuconych oczek')
        plt.ylabel('Prawdopodobieństwo')
        plt.title('Rzut dwoma kostkami przy n rzutach')
        plt.grid(True)
        plt.show()
    except Kostka_wyjatki:
        print("Nieodpowiednia wartość rzutu, musisz rzucić przynajmniej jeden raz.")
    except Exception as e:
        print(e)

rzuc_kostka(550)
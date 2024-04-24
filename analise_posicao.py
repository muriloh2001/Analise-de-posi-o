import seaborn as sns 
import matplotlib.pyplot as plt

import random
import numpy as np

serie = [] 

#serie aleatoria de 100 valores entre 7 e 500
serie = random.sample(range(7,5000000), 1000000)

#converter a list em nd.array ( vetor de números)
serie = np.array(serie)
print(type(serie))
print(serie.mean())
print(serie.std())
print(np.median(serie))

#Gráfrico de densidade
sns.kdeplot(serie)
plt.show()

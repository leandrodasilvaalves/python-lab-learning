# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
# https://chatgpt.com/c/68d524e3-fe90-8328-8a8c-15b0dfb1dd0c

"""
às vezes os dados não seguem em linha reta.
no exemplo dos carros, sua velocidade média varia em diferentes horas do dia
é um jeito matemátido de dizer "vamos usar mais curvas para melhor acompanhar os dados"
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [100, 90, 80, 60, 60, 70, 80, 100, 110, 120, 130, 150, 160, 170, 170, 180, 190, 200, 210]

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 20, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()


for grau in [2, 3, 4, 5]:
    modelo = np.poly1d(np.polyfit(x, y, grau))
    r2 = r2_score(y, modelo(x))
    print(f"Grau {grau} → R² = {r2:.4f}")


print(mymodel(17))
print(mymodel(21))
print(mymodel(22))
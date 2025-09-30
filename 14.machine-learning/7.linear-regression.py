# https://www.w3schools.com/python/python_ml_linear_regression.asp

import matplotlib.pyplot as plt
from scipy import stats


def calculdate(x, y):
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    ten_years_car_speed = myfunc(10)
    print("ten years", ten_years_car_speed)

    mymodel = list(map(myfunc, x))

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()


def example_one():
    x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    calculdate(x, y)


def example_two():
    x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
    y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

    calculdate(x, y)


# example_one()
# example_two()

# Revisão com Chat GPT
# https://chatgpt.com/g/g-p-68d077b84a3081919dd07e780b8c35a0/c/68d3cf32-5d60-832c-8620-4913c31619a6


def example_chat():
    pessoas = [2, 3, 4, 5]
    gastos = [1200, 1600, 2000, 2400]

    slope, intercept, r, p, std_err = stats.linregress(pessoas, gastos)

    def gasto_previsto(x):
        return slope * x + intercept

    x_vals = range(1, 7)
    y_vals = [gasto_previsto(x) for x in x_vals]

    plt.scatter(pessoas, gastos, color="blue", label="Dados reais")

    plt.plot(x_vals, y_vals, color="red", label="Regressão linear")

    plt.xlabel("Pessoas em casa")
    plt.ylabel("Gasto mensal (R$)")
    plt.title("Regressão Linear - Orçamento Doméstico")
    plt.legend()
    plt.show()

    print(f"Inclinação (quanto aumenta por pessoa): {slope}")
    print(f"Intercepto (gasto fixo): {intercept}")
    print(f"R² (qualidade do ajuste): {r**2}")


example_chat()
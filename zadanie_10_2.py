# manipulacja danymi
import numpy as np
import pandas as pd

# wizualizacja danych
import matplotlib.pyplot as plt
import seaborn as sns

# statystyczna analiza danych
from scipy import stats

# przygotowanie danych
from sklearn.preprocessing import StandardScaler, MinMaxScaler
dataset = pd.read_csv('titanic.csv')
fare_values = dataset.loc[dataset['Fare'].notnull(), 'Fare'].values

#obliczenie średniej
mean_fare = np.round(np.mean(fare_values))

#obliczenie kwartyli
q0 = np.round(np.quantile(fare_values, 0.00))
q1 = np.round(np.quantile(fare_values, 0.25))
q2 = np.round(np.quantile(fare_values, 0.50))
q3 = np.round(np.quantile(fare_values, 0.75))
q4 = np.round(np.quantile(fare_values, 1.00))

#wykres pudełkowy
plt.boxplot(fare_values, tick_labels=[''])
plt.ylabel('Cena biletu')  

#prezentacja wyników
result = f"""Średnia cena biletu: {mean_fare}
Najniższa cena: {q0}
Pierwszy kwartyl: {q1}
Mediana: {q2}
Trzeci kwartyl: {q3}
Najwyższa cena: {q4}"""
print(result)
plt.show()
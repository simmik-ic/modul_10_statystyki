import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

#funkcja tworzydo tworzenia słownika statystyk opisowych
def descriptive_stats(data):
    return {
        'Średnia': np.mean(data),
        'Mediana': np.median(data),
        'Moda': stats.mode(data),
        '1. kwartyl (Q1)': np.percentile(data, 25),
        '3. kwartyl (Q3)': np.percentile(data, 75),
        'Zakres': np.max(data) - np.min(data),
        'Rozstęp międzykwartylowy': np.percentile(data, 75) - np.percentile(data, 25),
        'Wariancja': np.var(data, ddof=1),
        'Odchylenie standardowe': np.std(data, ddof=1),       
    }


data_100 = np.random.normal(3, 1, 100)
data_10000 = np.random.normal(3, 1, 10000)

stats_100 = descriptive_stats(data_100)
stats_10000 = descriptive_stats(data_10000)

comparison = pd.DataFrame({
    'n=100': stats_100,
    'n=10000': stats_10000
})

plt.figure(figsize=(13, 7))

plt.subplot(1, 2, 1)
sns.histplot(data_100, bins=15, color='darkblue')
plt.title("n=100")

plt.subplot(1, 2, 2)
sns.histplot(data_10000, bins=15, color='green')
plt.title("n=10000")
plt.tight_layout()

result = f"""Choć wartości statystyk dla obu zbiorów danych są zbliżone, to jednak na histogramach widać, 
że większa próba lepiej odwzorowuje rozkład normalny. Na histogramie mniejszej próby widzoczne są spore odchylenia
w poszczególnych przedziałach, podczas gdy rozkład danych większej próby bardzo dobrze oddaje kształt krzywej dzwonowej."""

print(comparison)
print(result)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv', sep=';')
data.info()
data.head()
data.describe()
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

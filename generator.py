import pandas as pd
from faker import Faker
import random

# Crear una instancia de Faker
faker = Faker()

# Listas para almacenar los datos
ids = []
nombres = []
edades = []
dineros_ahorrados = []

# Generar 100,000 registros
for i in range(1, 100001):
    ids.append(i)
    nombres.append(faker.name())
    edades.append(random.randint(18, 80))
    dineros_ahorrados.append(round(random.uniform(100.0, 10000.0), 2))

# Crear un DataFrame
data = {
    'ID': ids,
    'Nombre': nombres,
    'Edad': edades,
    'Dinero Ahorrado': dineros_ahorrados
}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel('registros_100000.xlsx', index=False)

print("Archivo Excel generado exitosamente.")

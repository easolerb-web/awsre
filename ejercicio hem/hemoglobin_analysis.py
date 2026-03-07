"""
hemoglobin_analysis.py

Script para analizar la secuencia de la hemoglobina beta humana.
El programa:
- Lee la secuencia de aminoácidos
- Calcula composición de aminoácidos
- Calcula peso molecular
- Calcula porcentaje de aminoácidos hidrofóbicos
- Guarda los resultados en formato JSON
"""

import json

# Leer la secuencia desde el archivo
with open("hemoglobin_clean.txt", "r") as file:
    sequence = file.read().strip()

# Información básica
print("Nombre de la proteína: Hemoglobina beta humana")
print("Longitud de la secuencia:", len(sequence))

# Lista de aminoácidos
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# Conteo de aminoácidos
aa_count = {}

for aa in amino_acids:
    aa_count[aa] = sequence.count(aa)

print("\nConteo de aminoácidos:")
for aa, count in aa_count.items():
    print(aa, ":", count)

# Diccionario de pesos moleculares
aa_weights = {
"A": 89.1, "R": 174.2, "N": 132.1, "D": 133.1,
"C": 121.2, "E": 147.1, "Q": 146.2, "G": 75.1,
"H": 155.2, "I": 131.2, "L": 131.2, "K": 146.2,
"M": 149.2, "F": 165.2, "P": 115.1, "S": 105.1,
"T": 119.1, "W": 204.2, "Y": 181.2, "V": 117.1
}

# Función para calcular peso molecular
def calcular_peso_molecular(seq):

    peso_total = 0

    for aa in seq:
        peso_total += aa_weights.get(aa, 0)

    return peso_total

peso = calcular_peso_molecular(sequence)

print("\nPeso molecular aproximado:", peso)

# Aminoácidos hidrofóbicos
hidrofobicos = ["A", "V", "I", "L", "M", "F", "W", "Y"]

hidrofobicos_count = 0

for aa in sequence:
    if aa in hidrofobicos:
        hidrofobicos_count += 1

porcentaje_hidrofobico = (hidrofobicos_count / len(sequence)) * 100

print("Porcentaje de aminoácidos hidrofóbicos:", porcentaje_hidrofobico)

# Guardar resultados en JSON
resultados = {
"protein_name": "Hemoglobin beta (Homo sapiens)",
"sequence_length": len(sequence),
"amino_acid_count": aa_count,
"molecular_weight": peso,
"hydrophobic_percentage": porcentaje_hidrofobico
}

with open("hemoglobin_results.json", "w") as file:
    json.dump(resultados, file, indent=4)

print("\nResultados guardados en hemoglobin_results.json")
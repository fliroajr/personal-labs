import pandas as pd

# lista de frutas
frutas = ['abacate','maçã', 'pêra', 'abacaxi', 'goiaba']
frutas_novas = []

for fruta in frutas:
    frutanova = fruta + '_new'
    frutas_novas.append(frutanova)

print(frutas_novas)
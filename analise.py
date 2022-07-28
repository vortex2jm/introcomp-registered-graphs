#Análise das inscrições e matrículas do introcomp por série
#Desenvolvido por João Paulo Moura Clevelares
import pandas as pd
import matplotlib.pyplot as plt

#Análise de todos os inscritos===================================#
serie_column  = pd.read_csv('./inscricoes_2022.csv', usecols=[9])

insc_serie_list = []
aux = "Ensino Médio)"

for i in serie_column.itertuples():
    content = str(i[1]).split("(")
    if content[1] == aux:
        insc_serie_list.append(content[0])
print("quantidade de inscritos do ensino médio ->",len(insc_serie_list))
insc_serie_list.sort()
plt.hist(insc_serie_list, bins=20)
plt.show()

#Análise dos matriculados=========================================#

matriculados = pd.read_csv('./matriculas_2022.csv', usecols=[2,5])

mat_serie_list = []
n_mat_serie_list = []

for i in matriculados.itertuples():
    content = str(i[2]).split("(")
    if not pd.isnull(i[1]):
        if content[1] == aux:
            mat_serie_list.append(content[0])
    else:
        if content[1] == aux:
            n_mat_serie_list.append(content[0])

print("quantidade de matriculados do ensino médio ->",len(mat_serie_list))
mat_serie_list.sort()
plt.hist(mat_serie_list,bins=20)
plt.show()


#Análise dos não matriculados======================================#
print("quantidade de não matriculados do ensino médio -> ", len(n_mat_serie_list))
n_mat_serie_list.sort()
plt.hist(n_mat_serie_list, bins=20)
plt.show()

import re
regextel= re.compile(r'^(0?[1-9]{2}[- ]?|\(0?[0-9]{2}\) ?)[2-9]?[0-9]{4}[- ]?[0-9]{4}$')
numtelefone=input("Coloque um número de telefone válido: ")
dados=regextel.search(numtelefone)
if dados:
    print("Número de telefone válido:",numtelefone)
else:
    print("Número de telefone não encontrado:",numtelefone)
print(dados)
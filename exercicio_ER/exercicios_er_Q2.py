import re
regextel= re.compile(r'^(0?[1-9]{2}[- ]?|\(0?[0-9]{2}\) ?)[2-9]?[0-9]{4}[- ]?[0-9]{4}$')
numtelefone=input("Coloque um número de telefone válido: ")
dados=regextel.search(numtelefone)
if dados:
    print("Número de telefone válido:",numtelefone)
else:
    print("Número de telefone não encontrado:",numtelefone)

if dados:
    print("t")
    grupotel=r'^0?([0-9]{2})([0-9]{4,5})([0-9]{4})$'
    limpatel=re.sub(r'[^0-9]', "", numtelefone)
    telefoneresult=re.sub(grupotel,r'(\1) \2 \3',limpatel)
    print(telefoneresult)
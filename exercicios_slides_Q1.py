dimensao=int(input("Insira a dimensão da matriz A e B: "))
mat=[[] for i in range(dimensao)]
for i in range(dimensao):
    for j in range(dimensao):
        num=int(input("("+str(i+1)+","+str(j+1)+"): "))
        mat[i].append(num)
print("Matriz B: ")
mat2=[[] for i in range(dimensao)]
for i in range(dimensao):
    for j in range(dimensao):
        num2=int(input("("+str(i+1)+","+str(j+1)+"): "))
        mat2[i].append(num2)

matT=[[] for i in range(dimensao)]
for i in range(dimensao):
    for j in range(dimensao):
        matT[i].append(0)

matT2=[[] for i in range(dimensao)]
for i in range(dimensao):
    for j in range(dimensao):
        matT2[i].append(0)

print()
print(f"Matriz A ({dimensao} x {dimensao}): ")
for linha in mat:
    for numero in linha:
        print(numero, end=" ")
    print()
print()
print(f"Matriz B ({dimensao} x {dimensao}): ")
for linha in mat2:
    for numero in linha:
        print(numero, end=" ")
    print()

print("Subtração: ")
tam=len(mat)
mat3=[[0 for j in range(tam)] for i in range(tam)]
for i in range(tam):
    for j in range(tam):
        mat3[i][j]=mat[i][j]-mat2[i][j]

for linha in mat3:
    for numero in linha:
        print(numero, end=" ")
    print()

print("Transposta da Matriz A: ")
for i in range(dimensao):
    for j in range(dimensao):
        matT[i][j]=mat[j][i]

for linha in matT:
    for numero in linha:
        print(numero, end=" ")
    print()

print("Transposta da Matriz B: ")
for i in range(dimensao):
    for j in range(dimensao):
        matT2[i][j]=mat2[j][i]

for linha in matT2:
    for numero in linha:
        print(numero, end=" ")
    print()
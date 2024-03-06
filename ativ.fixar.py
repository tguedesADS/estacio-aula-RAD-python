# 1. Escreva uma função que recebe uma frase e uma palavra antiga e uma palavra nova. 
# A função deve retornar uma string contendo a frase original, mas com a última ocorrência 
# da palavra antiga substituída pela palavra nova. A entrada e saída de dados deve ser feita no programa principal.
def trocar_ultima_palavra(frase, palavra_antiga, palavra_nova):
    palavras = frase.split()

    ultima_palavra = None
    for i in range(len(palavras) - 1, -1, -1):
        if palavras[i] == palavra_antiga:
            ultima_palavra = i
            break

    if ultima_palavra is not None:
        palavras[ultima_palavra] = palavra_nova

    nova_frase = ' '.join(palavras)
    return nova_frase

frase = input("Digite a frase: ")
palavra_antiga = input("Digite a palavra antiga: ")
palavra_nova = input("Digite a palavra nova: ")

resultado = trocar_ultima_palavra(frase, palavra_antiga, palavra_nova)
print("Nova frase:", resultado)

# 2. Faça uma função que recebe uma frase e retorna o número de palavras que a frase contém. 
# Considere que a palavra pode começar e/ou terminar por espaços. A entrada e saída de dados deve ser feita no programa principal.
def contar_palavras(frase):
    frase = frase.strip()

    if not frase:
        return 0

    palavras = frase.split()

    return len(palavras)

frase = input("Digite uma frase: ")
numero_palavras = contar_palavras(frase)

print(f"A frase possui {numero_palavras} {'palavra' if numero_palavras == 1 else 'palavras'}.")

# 3. Faça uma função que recebe uma frase e substitui todas as ocorrências de espaço por “#”. 
# Faça também uma função para realizar a entrada de dados. A saída de dados deve ser feita no programa principal.
def substituir_espacos(frase):
    frase_modificada = frase.replace(' ', '#')
    return frase_modificada

def entrada_de_dados():
    frase = input("Digite uma frase: ")
    return frase

frase_original = entrada_de_dados()
frase_modificada = substituir_espacos(frase_original)

print("Frase original:", frase_original)
print("Frase modificada:", frase_modificada)

# 4. Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual 
# à outra quando lida de traz para frente.
def palindromas(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return str1 == str2[::-1]

string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")

if palindromas(string1, string2):
    print("As palavras são palíndromas mútuas.")
else:
    print("As palavras não são palíndromas mútuas.")

# 5. Faça um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas.
nome_usuario = input("Digite seu nome: ")
nome_invertido = nome_usuario.upper()[::-1]

print(f"Nome invertido:", {nome_invertido})

# 6. Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.

nome_usuario = input("Digite seu nome: ")

for i in range(1, len(nome_usuario) + 1):
    print(nome_usuario[:i].upper())




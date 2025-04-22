from itertools import permutations

# Essa é uma implementação simples de cifra de César. Não lida com caracteres especiais.
# Para facilitar a leittura, os espaços entre palavras não foram cifrados.
def encrypt_shift_cipher(plain_text: str, key: int) -> str:
    new_key = key % 26  # Reduz a chave para um intervalo de 0 a 25
    cipher_text = [] 

    for plain_char in plain_text:   # percorre todo o texto
        char_ascii = ord(plain_char)    # pega o valor ascii do caractere

        if plain_char.isupper():        # verifica se é maiúscula
            cipher_char_ascii = ((char_ascii + new_key - 65) % 26) # 65 é o valor ascii de 'A'
            cipher_text.append(chr(cipher_char_ascii + 65)) # converte o valor ascii de volta para caractere e o adiciona a lista
        
        elif plain_char.islower():       # verifica se é minúscula
            cipher_char_ascii = ((char_ascii + new_key - 97) % 26) # 97 é o valor ascii de 'a'
            cipher_text.append(chr(cipher_char_ascii + 97)) # converte o valor ascii de volta para caractere e o adiciona a lista

        elif plain_char == ' ':
            cipher_text.append(' ')

    return ''.join(cipher_text) # junta todos os caracteres da lista em uma string e retorna

print(encrypt_shift_cipher("Este e um exemplo", 3))


# Essa é uma implementação simples de decriptografia de cifra de César por força bruta. Não lida com caracteres especiais.
def decrypt_shift_cipher_Brute(cipher_text: str) -> None:
    for key in range(26):   # percorre todas as chaves de 0 a 25
        cipher_text_decrypted = encrypt_shift_cipher(cipher_text, key) # chama a função de cifragem com a chave
        print(f"Chave de criptografia: {(26 - key) % 26} - Chave de descriptografia {key} - Suposto texto decifrado: {cipher_text_decrypted}")
    return

# Essa é uma implementação simples de criptografia por transposição 
def encrypt_transposition_cipher(plain_text: str, key: list[int]) -> str:
    # pass
    columns = len(key) # número de colunas da matriz
    rows = len(plain_text) // columns + (len(plain_text) % columns > 0) # número de linhas da matriz

    matrix = [['' for _ in range(columns)] for _ in range(rows)] # cria uma matriz vazia com o número de linhas e colunas especificado

    index = 0
    # preenche a matriz com os caracteres do texto original
    for i in range(rows):
        for j in range(columns):
            if index < len(plain_text):
                matrix[i][j] = plain_text[index]
                index += 1
            else:   
                # preenche o restante da matriz com espaços em branco
                matrix[i][j] = ' '
    print(matrix)
    cipher_text = []
    # percorre a matriz de acordo com a chave e adiciona os caracteres na lista cipher_text
    for i in range(len(key)):
        for j in range(rows):
            if matrix[j][key[i] - 1] != ' ':
                # verifica se o caractere não é um espaço em branco
                cipher_text.append(matrix[j][key[i] - 1])
            else:
                # se for um espaço em branco, adiciona o caractere ' ' para indicar que o caractere foi pulado
                cipher_text.append(' ')
    cipher_text = ''.join(cipher_text)
    print(cipher_text)
    return cipher_text

def decrypt_transposition_cipher(cipher_text: str) -> None:
    # pass
    key_len = 1  # não sabemos o tamanho da chave usada, então testaremos todas as chaves até achar um resultado aceitável
    while True:
        # cria uma lista de 1 até a chave
        key_elements = [] 

        # key_elements = [i for i in range(1, key_len + 1)]
        for i in range(key_len):
            key_elements.append(i + 1)
        print(f'Elementos da chave {key_elements}')
        print("Testes: ")

        # cria uma lista com todas as possibilidades de permutação entre os elementos da chave 
        allKeys = list(permutations(key_elements))
        
        # cria uma matriz que irá armazenar cada caracter do texto cifrado 
        columns = key_len
        rows = len(cipher_text) // columns + (len(cipher_text) % columns > 0)
        matrix = [['' for _ in range(columns)] for _ in range(rows)]
        i = 0 
        # preenche a matriz com os caracteres do texto cifrado
        for j in range(columns):
            for k in range(rows):
                if i < len(cipher_text):
                    matrix[k][j] = cipher_text[i]
                else: 
                    matrix[k][j] = ' '
                i += 1
        

        # Faz o processo inverso da cifra por transposição 
        teste = 1
        # percorre todas as chaves possíveis
        for key in allKeys:
            plain_text = []
            for i in range(rows):
                for j in range(columns):
                    plain_text.append(matrix[i][key[j] - 1])
            
            result = ''.join(plain_text) # junta todos os caracteres da lista em uma string e retorna
            print(f'Teste {teste} - Resultado: {result}')
            teste += 1

        # pergunta se o usuário quer continuar testando outras chaves
        if input("Continuar? ") == 'NAO':
            print("Processo interrompido.")
            break

        key_len += 1
    return 
    



# print(encrypt_transposition_cipher("Meu nome e Lucas SR", [3,1,2,4]))
encrypt_transposition_cipher("Esse e um teste", [3,1,2,4])
# encrypt_transposition_cipher("Este é um Teste", [3,1,2])

# decrypt_transposition_cipher("témeeEe  ss uTt")





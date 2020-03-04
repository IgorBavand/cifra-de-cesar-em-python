alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
print('Digite a chave da cifra: ',end='')
chave = int(input())
print('Digite a palavra a ser criptografada: ',end='')
palavra = input()
posi = 0
i = 0
l = 0
palavra_criptografada = list(palavra)
while i < len(palavra):
    l = 0
    while l < 26:
        if palavra[i] == ' ':
            palavra_criptografada[i] = ' '
        else:     
            if palavra[i] == alfabeto[l]:
                k = 0
                posi = l+1
                while k < chave:
                    posi+=1
                    if posi > 26:
                        posi = 0 
                    k+=1
                if posi > l:
                    posi = posi - 1
            palavra_criptografada[i] = alfabeto[posi]
        l+=1
    i+=1
for imprimir in range(len(palavra_criptografada)):
    print(palavra_criptografada[imprimir],end='')
print()
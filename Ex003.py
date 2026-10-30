n1=int(input("Escolha um número: "))
n2=int(input("Escolha outro número: "))

s=(n1 + n2)

print("A soma vale {}".format(s))

#OU

print("A soma etre {} e {} vale {}".format(n1,n2,s))

#print("A soma entre {} e {}".format(n1, n2),"é igual a {}".format(s))

#O .format() é um método de formatação de strings que permite inserir valores em uma string de forma mais legível e flexível. Ele substitui os placeholders {} na string pelo valor fornecido como argumento do método format().
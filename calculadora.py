

def calcular_multiusuario(operacao,*numeros):
    if not numeros:
        return "Nenhum números foi informado"
    #Começamos o resultado com o primeiro número da lista
    resultado = numeros[0]
    #Percorremos os números restantes aplicando a operação escolhida
    for num in numeros[1:]:
        if operacao =="+":
            resultado += num
        elif operacao =="-":
            resultado -=num
        elif operacao == "*":
            resultado *= num
        elif operacao =="/":
            if num!=0:
                resultado /= num
            else:
                return "Erro: Divisão por zero!"
        else:
            return "Operação inválida!"
    return resultado

#---Fluxo Principal interativo---
print("---Calculadora Avançada---")
# O usuário escolhe a operação primeiro
op= input("Escolha a operação(+,-,*,/):")
#O usuário digita quantos números quiser
print("Digite os números um por um.Digite 'fim para encerrar.")
lista_de_numeros=[]
while True:
   entrada= input("Digite um número ( ou'fim'):")
   if entrada.lower() == 'fim':
       break
   try:
       lista_de_numeros.append(float(entrada))
   except ValueError:
       print("Valor inválido!Digite apenas numeros ou 'fim'.")

    #Chamamos a função passando o operador e a lista de números descompactada com  '*'
if lista_de_numeros:
    resultado_final = calcular_multiusuario(op,*lista_de_numeros)
    print(f"Oresultado da operação é:{resultado_final}")
else:
    print("Nenhum número foi inserido para calcular.")







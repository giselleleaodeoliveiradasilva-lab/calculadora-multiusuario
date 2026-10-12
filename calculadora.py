

# def calcular_multiusuario(operacao,*numeros):
#     if not numeros:
#         return "Nenhum número foi informado"
#     #Começamos o resultado com o primeiro número da lista
#     resultado = numeros[0]
#     #Percorremos os números restantes aplicando a operação escolhida
#     for num in numeros[1:]:
#         if operacao =="+":
#             resultado += num
#         elif operacao =="-":
#             resultado -=num
#         elif operacao == "*":
#             resultado *= num
#         elif operacao =="/":
#             if num!=0:
#                 resultado /= num
#             else:
#                 return "Erro: Divisão por zero!"
#         else:
#             return "Operação inválida!"
#     return resultado
#
# #---Fluxo Principal interativo---
# print("---Calculadora Avançada---")
# # O usuário escolhe a operação primeiro
# op= input("Escolha a operação(+,-,*,/):")
# #O usuário digita quantos números quiser
# print("Digite os números um por um.Digite 'fim para encerrar.")
# lista_de_numeros=[]
# while True:
#    entrada= input("Digite um número ( ou'fim'):")
#    if entrada.lower() == 'fim':
#        break
#    try:
#        lista_de_numeros.append(float(entrada))
#    except ValueError:
#        print("Valor inválido!Digite apenas numeros ou 'fim'.")
#
#     #Chamamos a função passando o operador e a lista de números descompactada com  '*'
# if lista_de_numeros:
#     resultado_final = calcular_multiusuario(op,*lista_de_numeros)
#     print(f"O resultado da operação é: {resultado_final}")
# else:
#     print("Nenhum número foi inserido para calcular.")



import tkinter as tk
from tkinter import messagebox


# --- 1. Função Core (Lógica de cálculo multiusuário) ---
def calcular_multiusuario(operacao, *numeros):
    if not numeros:
        return "Nenhum número foi informado"

    resultado = numeros[0]
    for num in numeros[1:]:
        if operacao == "+":
            resultado += num
        elif operacao == "-":
            resultado -= num
        elif operacao == "*":
            resultado *= num
        elif operacao == "/":
            if num != 0:
                resultado /= num
            else:
                return "Erro: Divisão por zero!"
        else:
            return "Operação inválida!"
    return resultado


# --- 2. Funções de Ação da Interface com Validações Rigorosas ---
def executar_calculo():
    operacao = entrada_op.get().strip()
    texto_numeros = entrada_numeros.get().strip()

    # Valida se os campos estão preenchidos
    if not operacao or not texto_numeros:
        messagebox.showwarning("Atenção", "Por favor, preencha a operação e os números.")
        return

    # Valida se o operador é estritamente um dos permitidos
    if operacao not in ["+", "-", "*", "/"]:
        messagebox.showerror(
            "Operação Inválida",
            "O campo de operação deve conter apenas um dos símbolos válidos: +, -, * ou /."
        )
        return

    # Normaliza a entrada substituindo vírgulas por espaços
    texto_formatado = texto_numeros.replace(",", " ")
    partes = texto_formatado.split()

    lista_de_numeros = []
    try:
        for parte in partes:
            lista_de_numeros.append(float(parte))
    except ValueError:
        messagebox.showerror(
            "Erro de Formato",
            "Formato inválido!\nCertifique-se de digitar apenas números separados por espaços ou vírgulas."
        )
        return

    # Exige pelo menos 2 números para realizar o cálculo
    if len(lista_de_numeros) < 2:
        messagebox.showerror(
            "Quantidade Insuficiente",
            "Insira pelo menos dois números separados por espaço ou vírgula para calcular!"
        )
        return

    # Chama a função original descompactando a lista com '*'
    resultado_final = calcular_multiusuario(operacao, *lista_de_numeros)

    # Exibe o resultado ou mensagem de erro na tela
    if isinstance(resultado_final, str):
        messagebox.showerror("Erro na Operação", resultado_final)
        label_resultado.config(text=f"Resultado: {resultado_final}", fg="#ef4444")
    else:
        label_resultado.config(text=f"Resultado: {resultado_final}", fg="#34d399")


def limpar_campos():
    """Limpa todos os campos de entrada e reseta o resultado na tela."""
    entrada_op.delete(0, tk.END)
    entrada_numeros.delete(0, tk.END)
    label_resultado.config(text="Resultado: -", fg="#34d399")
    entrada_op.focus()


# --- 3. Construção da Interface Gráfica (Tkinter) ---
janela = tk.Tk()
janela.title("Calculadora Multiusuário - v2.2 GUI")
janela.geometry("400x500")
janela.config(bg="#0f172a")
janela.resizable(False, False)

# Cabeçalho
titulo = tk.Label(janela, text="Calculadora Multiusuário", font=("Arial", 16, "bold"), bg="#0f172a", fg="#ffffff")
titulo.pack(pady=15)

subtitulo = tk.Label(janela, text="Versão 2.2 (Com Validações Avançadas)", font=("Arial", 9, "italic"), bg="#0f172a",
                     fg="#94a3b8")
subtitulo.pack(pady=(0, 15))

# Campo de Operação
label_op = tk.Label(janela, text="Escolha a operação (+, -, *, /):", bg="#0f172a", fg="#e2e8f0", font=("Arial", 10))
label_op.pack(anchor="w", padx=40)
entrada_op = tk.Entry(janela, font=("Arial", 12), justify="center", width=8)
entrada_op.pack(pady=(5, 15))

# Campo para Números
label_num = tk.Label(janela, text="Digite os números (separados por espaço ou vírgula):", bg="#0f172a", fg="#e2e8f0",
                     font=("Arial", 10))
label_num.pack(anchor="w", padx=40)
entrada_numeros = tk.Entry(janela, font=("Arial", 12), justify="center", width=28)
entrada_numeros.pack(pady=(5, 20))

# Frame para os botões
frame_botoes = tk.Frame(janela, bg="#0f172a")
frame_botoes.pack(pady=10)

botao_calcular = tk.Button(
    frame_botoes,
    text="Calcular",
    font=("Arial", 11, "bold"),
    bg="#38bdf8",
    fg="#0f172a",
    activebackground="#0284c7",
    width=12,
    cursor="hand2",
    command=executar_calculo
)
botao_calcular.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    font=("Arial", 11, "bold"),
    bg="#94a3b8",
    fg="#0f172a",
    activebackground="#64748b",
    width=12,
    cursor="hand2",
    command=limpar_campos
)
botao_limpar.pack(side=tk.LEFT, padx=5)

# Exibição do Resultado
label_resultado = tk.Label(janela, text="Resultado: -", font=("Arial", 13, "bold"), bg="#0f172a", fg="#34d399")
label_resultado.pack(pady=25)

# Loop Principal
janela.mainloop()


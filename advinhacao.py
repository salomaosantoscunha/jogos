import tkinter as tk
import random

# Função para verificar o chute do jogador
def verificar_chute():
    global pontos
    global total_de_tentativas

    chute_str = entrada_chute.get()
    try:
        chute = int(chute_str)
    except ValueError:
        resultado.config(text="Digite um número válido entre 1 e 100!")
        return

    if 1 <= chute <= 100:
        total_de_tentativas -= 1
        tentativas_label.config(text=f'Tentativas: {total_de_tentativas}')

        if chute == numero_secreto:
            resultado.config(text=f"Parabéns! Você acertou e fez {pontos} pontos!")
            btn_chutar.config(state=tk.DISABLED)
        else:
            if chute < numero_secreto:
                resultado.config(text="Você errou. Tente um número maior.")
            else:
                resultado.config(text="Você errou. Tente um número menor.")
            pontos -= abs(numero_secreto - chute)
            pontos_label.config(text=f'Pontos: {pontos}')

        if total_de_tentativas == 0:
            resultado.config(text=f"Fim do jogo. O número secreto era {numero_secreto}.")
            btn_chutar.config(state=tk.DISABLED)
    else:
        resultado.config(text="Digite um número válido entre 1 e 100!")

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo Python")
janela.geometry("300x200")

# Variáveis globais
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

# Escolha de nível de dificuldade
def definir_nivel(nivel):
    global total_de_tentativas
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 2
    nivel_frame.destroy()  # Remove o frame de seleção de nível
    btn_chutar.config(state=tk.NORMAL)  # Ativa o botão de chute
    tentativas_label.config(text=f'Tentativas: {total_de_tentativas}')

nivel_frame = tk.Frame(janela)
nivel_frame.pack()

nivel_label = tk.Label(nivel_frame, text="Qual nível de dificuldade?")
nivel_label.pack()

btn_facil = tk.Button(nivel_frame, text="Fácil", command=lambda: definir_nivel(1))
btn_medio = tk.Button(nivel_frame, text="Médio", command=lambda: definir_nivel(2))
btn_dificil = tk.Button(nivel_frame, text="Difícil", command=lambda: definir_nivel(3))

btn_facil.pack()
btn_medio.pack()
btn_dificil.pack()

# Interface principal
tentativas_label = tk.Label(janela, text=f'Tentativas: {total_de_tentativas}')
tentativas_label.pack()

entrada_chute = tk.Entry(janela)
entrada_chute.pack()

btn_chutar = tk.Button(janela, text="Chutar", command=verificar_chute)
btn_chutar.pack()

pontos_label = tk.Label(janela, text=f'Pontos: {pontos}')
pontos_label.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()

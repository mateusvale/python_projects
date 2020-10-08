from tkinter import *
from functools import partial
import random
from tkinter import messagebox
count = 0 #número de jogadas
lista_de_jogadas = [] # Será usado para colocar os valores digitados
botoes_jogador = []
botoes_maquina = []
def aperta_botao(y):
        def verificacao(lista_do_jogador):
                if lista_do_jogador.count(0) == True and lista_do_jogador.count(1) == True and lista_do_jogador.count(2) == True:
                        botoes[0]['bg'] = 'red'
                        botoes[1]['bg'] = 'red'
                        botoes[2]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(3) == True and lista_do_jogador.count(6) == True:
                        botoes[0]['bg'] = 'red'
                        botoes[3]['bg'] = 'red'
                        botoes[6]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(8) == True:
                        botoes[0]['bg'] = 'red'
                        botoes[4]['bg'] = 'red'
                        botoes[8]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(1) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(7) == True:
                        botoes[1]['bg'] = 'red'
                        botoes[4]['bg'] = 'red'
                        botoes[7]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(2) == True and lista_do_jogador.count(5) == True and lista_do_jogador.count(8) == True:
                        botoes[2]['bg'] = 'red'
                        botoes[5]['bg'] = 'red'
                        botoes[8]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(3) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(5) == True:
                        botoes[3]['bg'] = 'red'
                        botoes[4]['bg'] = 'red'
                        botoes[5]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(7) == True and lista_do_jogador.count(8) == True:
                        botoes[6]['bg'] = 'red'
                        botoes[7]['bg'] = 'red'
                        botoes[8]['bg'] = 'red'
                        return 'ganhou'
                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(2) == True:
                        botoes[6]['bg'] = 'red'
                        botoes[4]['bg'] = 'red'
                        botoes[2]['bg'] = 'red'
                        return 'ganhou'
                else: return 'não'
        global count
        global vez
        if vez == 0:
                botoes[y]['text'] = 'O'
                lista_de_jogadas.append(y)
                botoes_jogador.append(y)
                if verificacao(botoes_jogador) == 'ganhou':
                        messagebox.showinfo("", "Você ganhou!!!!!")
                        i.destroy()
                elif len(lista_de_jogadas) == 9:
                        messagebox.showinfo("", "Deu velha!!!!!")
                        i.destroy()
                vez = 1
                count += 1
        if vez == 1:
                while count <=8:
                        numero = random.randrange(0,8)
                        if lista_de_jogadas.count(numero) == False:
                                botoes[numero]['text'] = 'X'
                                botoes[numero].configure(state = 'disable')
                                lista_de_jogadas.append(numero)
                                botoes_maquina.append(numero)
                                if verificacao(botoes_maquina) == 'ganhou':
                                        messagebox.showinfo("", "A máquina ganhou!!!!!")
                                        i.destroy()
                                elif len(lista_de_jogadas) == 9:
                                        messagebox.showinfo("", "Deu velha!!!!!")
                                        i.destroy()
                                count +=1
                                break
                vez = 0
                botoes[y].configure(state = 'disable')
i = Tk()
i.title('Jogo da Velha')
i['bg'] = 'lightgray'
titulo = Label (i, text = 'JOGO DA VELHA', fg = 'black', width = 15, bg = 'lightgray', font=("Comic Sans MS", "25", "bold"))
titulo.grid(columnspan=3)

btn_11 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 0))
btn_11.grid(row = 1, column = 0, sticky=W)
btn_12 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 1))
btn_12.grid(row = 1, column = 1, sticky=W)
btn_13 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 2))
btn_13.grid(row = 1, column = 2, sticky=W)

btn_21 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 3))
btn_21.grid(row = 2, column = 0, sticky=W)
btn_22 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 4))
btn_22.grid(row = 2, column = 1, sticky=W)
btn_23 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 5))
btn_23.grid(row = 2, column = 2, sticky=W)

btn_31 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 6))
btn_31.grid(row = 3, column = 0, sticky=W)
btn_32 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 7))
btn_32.grid(row = 3, column = 1, sticky=W)
btn_33 = Button (i,font=("Comic Sans MS", "25", "bold"), bg = 'white', bd = 10, pady = 28, padx = 18, width = 15, command = partial( aperta_botao, 8))
btn_33.grid(row = 3, column = 2, sticky=W)

botoes = [btn_11,btn_12,btn_13,btn_21,btn_22,btn_23,btn_31,btn_32,btn_33]

label = Label (i, text = 'NIVEL 1', font=("Comic Sans MS", "25", "bold"), fg = 'black',bg = 'lightgray').grid(row = 4, columnspan = 3)

mensagem = messagebox.askyesno("", "                    JOGO DO VELHA\n► Nível 1\n► Objetivo da máquina: Apenas jogar (jogadas aleatórias)\nVocê gostaria de ser o primeiro no jogo?")
if mensagem == True:
        vez = 0
else:
        vez = 1
        aperta_botao(10)

i.resizable(width = False, height = False)
i.mainloop()

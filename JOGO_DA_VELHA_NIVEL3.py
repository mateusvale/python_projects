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

        def proxima_jogada(lista_do_jogador):
                if lista_do_jogador.count(0) == True and lista_do_jogador.count(1) == True and lista_do_jogador.count(2) == False and lista_de_jogadas.count(2) == False:
                        return 2

                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(1) == False and lista_do_jogador.count(2) == True and lista_de_jogadas.count(1) == False:
                        return 1

                elif lista_do_jogador.count(0) == False and lista_do_jogador.count(1) == True and lista_do_jogador.count(2) == True and lista_de_jogadas.count(0) == False:
                        return 0
                        

                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(3) == True and lista_do_jogador.count(6) == False and lista_de_jogadas.count(6) == False:
                        return 6

                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(3) == False and lista_do_jogador.count(6) == True and lista_de_jogadas.count(3) == False:
                        return 3

                elif lista_do_jogador.count(0) == False and lista_do_jogador.count(3) == True and lista_do_jogador.count(6) == True and lista_de_jogadas.count(0) == False:
                        return 0
                        

                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(8) == False and lista_de_jogadas.count(8) == False:
                        return 8

                elif lista_do_jogador.count(0) == True and lista_do_jogador.count(4) == False and lista_do_jogador.count(8) == True and lista_de_jogadas.count(4) == False:
                        return 4

                elif lista_do_jogador.count(0) == False and lista_do_jogador.count(4) == True and lista_do_jogador.count(8) == True and lista_de_jogadas.count(0) == False:
                        return 0
                

                elif lista_do_jogador.count(1) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(7) == False and lista_de_jogadas.count(7) == False:
                        return 7

                elif lista_do_jogador.count(1) == True and lista_do_jogador.count(4) == False and lista_do_jogador.count(7) == True and lista_de_jogadas.count(4) == False:
                        return 4

                elif lista_do_jogador.count(1) == False and lista_do_jogador.count(4) == True and lista_do_jogador.count(7) == True and lista_de_jogadas.count(1) == False:
                        return 1


                elif lista_do_jogador.count(2) == True and lista_do_jogador.count(5) == True and lista_do_jogador.count(8) == False and lista_de_jogadas.count(8) == False:
                        return 8

                elif lista_do_jogador.count(2) == True and lista_do_jogador.count(5) == False and lista_do_jogador.count(8) == True and lista_de_jogadas.count(5) == False:
                        return 5

                elif lista_do_jogador.count(2) == False and lista_do_jogador.count(5) == True and lista_do_jogador.count(8) == True and lista_de_jogadas.count(2) == False:
                        return 2
                

                elif lista_do_jogador.count(3) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(5) == False and lista_de_jogadas.count(5) == False:
                        return 5

                elif lista_do_jogador.count(3) == True and lista_do_jogador.count(4) == False and lista_do_jogador.count(5) == True and lista_de_jogadas.count(4) == False:
                        return 4

                elif lista_do_jogador.count(3) == False and lista_do_jogador.count(4) == True and lista_do_jogador.count(5) == True and lista_de_jogadas.count(3) == False:
                        return 3


                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(7) == True and lista_do_jogador.count(8) == False and lista_de_jogadas.count(8) == False:
                        return 8

                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(7) == False and lista_do_jogador.count(8) == True and lista_de_jogadas.count(7) == False:
                        return 7

                elif lista_do_jogador.count(6) == False and lista_do_jogador.count(7) == True and lista_do_jogador.count(8) == True and lista_de_jogadas.count(6) == False:
                        return 6
                

                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(4) == True and lista_do_jogador.count(2) == False and lista_de_jogadas.count(2) == False:
                        return 2

                elif lista_do_jogador.count(6) == True and lista_do_jogador.count(4) == False and lista_do_jogador.count(2) == True and lista_de_jogadas.count(4) == False:
                        return 4

                elif lista_do_jogador.count(6) == False and lista_do_jogador.count(4) == True and lista_do_jogador.count(2) == True and lista_de_jogadas.count(6) == False:
                        return 6
                
                else: return 'none'


        def ganhador(vez):
                if vez == 0:
                        messagebox.showinfo("", "Você ganhou!!!!!")
                        i.destroy()
                else:
                        messagebox.showinfo("", "A máquina ganhou!!!!!")
                        i.destroy()

        def velha (jogadas):
                if jogadas == 9:
                        messagebox.showinfo("", "Deu velha!!!!!")
                        i.destroy()
                else: pass


        def preenche_quadrado(dados,vez):
                if vez == 0:                                            #Vez do jogador
                        botoes[dados]['text'] = 'O'
                        botoes[dados].configure(state = 'disable')
                        botoes_jogador.append(dados)
                        lista_de_jogadas.append(dados)
                else:                                                   #Vez da máquina
                        botoes[dados]['text'] = 'X'
                        botoes[dados].configure(state = 'disable')
                        botoes_maquina.append(dados)
                        lista_de_jogadas.append(dados)

#----------------------------------------------------------------------------------------------------------------------------------#
                
        global count                    #Serve para contar as jogadas
        global vez                      #Serve para verificar a vez do jogador ou da máquina
        jogadas_boas = [0,2,6,8]        #Boas jogadas para a máquina fazer

        

#----------------------------------Vez da Jogador----------------------------------------------------------------------------------#
        
        
        if vez == 0:
                preenche_quadrado(y,vez)
                if verificacao(botoes_jogador) == 'ganhou': #Verifica se ganhou
                        ganhador(vez)
                velha (len(lista_de_jogadas))
                vez = 1 #Joga pra vez da máquina
                count += 1

#----------------------------------Vez da Máquina----------------------------------------------------------------------------------#
        
        if vez == 1:    #Vez da máquina
                while count <=8: #Se for acima de 9, acabou as jogadas 
                        if proxima_jogada(botoes_maquina) != 'none': #Ver se tem uma lacuna para ganhar
                                preenche_quadrado(proxima_jogada(botoes_maquina),vez)
                                if verificacao(botoes_maquina) == 'ganhou':
                                        ganhador(vez)
                                velha (len(lista_de_jogadas))
                                count +=1
                                break
                                
                        elif proxima_jogada(botoes_jogador) != 'none':    #Vai tentar acabar com a felicidade do jogador
                                preenche_quadrado(proxima_jogada(botoes_jogador),vez)
                                if verificacao(botoes_maquina) == 'ganhou':
                                        ganhador(vez)
                                velha (len(lista_de_jogadas))
                                count +=1
                                break
                        else:
                                aux = 0
                                saindo_do_primeiro_loop = 0
                                while True:
                                        if lista_de_jogadas.count(jogadas_boas[aux]) == False:  #Vai tentar pegas os quadrados dos cantos
                                                preenche_quadrado(jogadas_boas[aux],vez)
                                                if verificacao(botoes_maquina) == 'ganhou':
                                                        ganhador(vez)
                                                velha (len(lista_de_jogadas))
                                                count +=1
                                                saindo_do_primeiro_loop = 1
                                                break
                                        else:
                                                aux+=1
                                                if aux == 4:
                                                        break
                                if saindo_do_primeiro_loop == 1:
                                        break
                                numero = random.randrange(0,8)
                                if lista_de_jogadas.count(numero) == False:
                                        preenche_quadrado(numero,vez)
                                        if verificacao(botoes_maquina) == 'ganhou':
                                                ganhador(vez)
                                        velha (len(lista_de_jogadas))
                                        count +=1
                                        break
                vez = 0
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

label = Label (i, text = 'NIVEL 3', font=("Comic Sans MS", "25", "bold"), fg = 'black',bg = 'lightgray').grid(row = 4, columnspan = 3)

mensagem = messagebox.askyesno("", "                    JOGO DO VELHA\n► Nível 3\n► Objetivo da máquina: Tentar ganhar e também \nnão deixar você ganhar.\nVocê gostaria de ser o primeiro no jogo?")
if mensagem == True:
        vez = 0
else:
        vez = 1
        aperta_botao(10)
i.resizable(width = False, height = False)
i.mainloop()

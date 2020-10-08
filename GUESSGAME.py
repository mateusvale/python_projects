from tkinter import *
from functools import partial
import random
from tkinter import messagebox

numero = random.randrange(1,101)
#print('O valor randômico é ',numero)
count = 0
num_teclados = []
lista_verificações = []         #Para verificar a dica anterior e colocar um dica melhor


def aperta_botao(j):
    global botao    #Para poder utilizar o botão que apertei
    global numero   #Número randômico
    global count    #Para contar quantas vezes apertei o botão
    global num_teclados #Para colocar numa lista todos os números clicados
    global lista_verificações
    
    def verificacao(valor):
        if valor == 1:
            return 'FV'
        if valor <= 3:
            return 'MQ'
        if valor <= 6:
            return 'QT'
        if valor <= 8:
            return 'MN'
        if valor <= 9:
            return 'FR'
        if valor <= 29:
            return 'MF'
        else:   return 'CG'

    def dica1 (x):
        if x == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Está fervendo' 
        if x == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Está muito quente'
        if x == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Está quente'
        if x == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Está morno'
        if x == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Está frio'
        if x == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Está muito frio'
        if x == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Está congelando'

    def dica2 (nova,anterior):
        if anterior == 'FV' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Quase, seu palpite ainda está fervendo!'
        if anterior == 'FV' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Oops, seu deu uma esfriada mas ainda está muito quente.'
        if anterior == 'FV' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Oops, seu deu uma esfriada mas ainda está quente.'
        if anterior == 'FV' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Oops, seu deu uma esfriada e agora está morno.'
        if anterior == 'FV' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Estava fervendo, porém agora ficou frio.'
        if anterior == 'FV' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Estava fervendo, porém agora ficou muito frio.'
        if anterior == 'FV' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Caramba!!! Estava fervendo porém agora congelou.'


        if anterior == 'MQ' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Melhorou hein! está fervendo agora.'
        if anterior == 'MQ' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Opa, seu palpite continua muito quente!'
        if anterior == 'MQ' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Oops, estava muito quente porém agora ficou só quente.'
        if anterior == 'MQ' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Oops, estava muito quente porém agora ficou morno.'
        if anterior == 'MQ' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Ihhhh, estava muito quente porém agora ficou frio.'
        if anterior == 'MQ' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Ihhhh, estava muito quente porém agora ficou muito frio.'
        if anterior == 'MQ' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Caramba!!! Estava muito quente porém agora congelou.'


        if anterior == 'QT' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Por pouco!!!! Está fervendo agora.'
        if anterior == 'QT' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Boa!!!! Está muito quente agora.'
        if anterior == 'QT' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Seu palpite continua quente.' 
        if anterior == 'QT' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Seu palpite esfriou um pouco e ficou morno.'
        if anterior == 'QT' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Então... ficou frio agora.'
        if anterior == 'QT' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Oops, estava quente porém agora ficou muito frio.'
        if anterior == 'QT' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return '... congelou.'


        if anterior == 'MN' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Por pouco!!!! Está fervendo agora.'
        if anterior == 'MN' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Boa!!!! Está muito quente agora.'
        if anterior == 'MN' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Melhorou um pouco. Estava morno e agora está quente.'
        if anterior == 'MN' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Seu palpite continua morno.' 
        if anterior == 'MN' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Ficou frio agora. Na próxima você melhora.'
        if anterior == 'MN' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Passou uma frente fria e agora ficou muito frio.'
        if anterior == 'MN' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Oops, estava morno porém agora congelou.'


        if anterior == 'FR' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Por pouco!!!! Está fervendo agora.'
        if anterior == 'FR' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Boa, melhorou bastante!!!! Está muito quente agora.'
        if anterior == 'FR' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Boa!!!! Está quente agora.'
        if anterior == 'FR' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Esquentou um pouco. Agora está morno.'
        if anterior == 'FR' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'OOps, seu palpite continua frio.'
        if anterior == 'FR' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Ihhhh, esfriou ainda mais e ficou muito frio.'
        if anterior == 'FR' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Oops, estava frio porém agora congelou.'


        if anterior == 'MF' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Por pouco!!!! Está fervendo agora.'
        if anterior == 'MF' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Opa, ficou muito quente agora, vamos lá!'
        if anterior == 'MF' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Opa, ficou quente agora, vamos lá, vc consegue!'
        if anterior == 'MF' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Bommmm. Estava muito frio e agora ficou morno.'
        if anterior == 'MF' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Oops, estava muito frio porém agora ficou frio somente.'
        if anterior == 'MF' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Seu palpite continua muito frio.'
        if anterior == 'MF' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Oops, estava muito frio porém agora congelou.'


        if anterior == 'CG' and nova == 'FV':
            botao[j-1]['bg'] = '#FF0000'
            return 'Rapaz, esquentou tanto seu palpite que agora está fervendo!'
        if anterior == 'CG' and nova == 'MQ':
            botao[j-1]['bg'] = '#FF6666'
            return 'Opa, esquentou tanto seu palpite que agora está muito quente!'
        if anterior == 'CG' and nova == 'QT':
            botao[j-1]['bg'] = '#FFB266'
            return 'Opa, ficou quente agora, vamos lá!'
        if anterior == 'CG' and nova == 'MN':
            botao[j-1]['bg'] = '#FFFF99'
            return 'Opa, ficou morno agora, vamos lá, vc consegue!'
        if anterior == 'CG' and nova == 'FR':
            botao[j-1]['bg'] = '#3333FF'
            return 'Seu palpite deu uma esquentadinha e ficou frio.'
        if anterior == 'CG' and nova == 'MF':
            botao[j-1]['bg'] = '#000099'
            return 'Seu palpite deu uma esquentadinha de leve e ficou muito frio.'
        if anterior == 'CG' and nova == 'CG':
            botao[j-1]['bg'] = '#FFFFFF'
            return 'Seu palpite continua congelado!'
        

        
    botao[j-1].configure(state = 'disable')     #Irá desabilitar o botão para não poder apertar mais
    count += 1                      #Para contar o numero de vezes apertadas
    #tentativas = ['NUMERO DE TENTATIVAS: %i' %(10-count)]
    numero_tentativas['text']= 'NUMERO DE TENTATIVAS: %i de 10' %(10-count)
    valor = abs(int(botao[j-1]['text']) - numero)   #Valor irá receber o módulo da subtração do valor teclado com o valor randômico
    if valor == 0:
        messagebox.showinfo("", "VC ACERTOU!!!!!!!!!")
        i.destroy()
        # Aparecer a caixa de mensagem dizendo que ganhou
    else:
        #primeira verificacao
        if count == 1:
            dica['text'] = dica1(verificacao(valor))
            lista_verificações.append(verificacao(valor))
        # A partir da segunda verificação
        else:
            dica['text'] = dica2(verificacao(valor),lista_verificações[count-2])        #na função, o primeiro elemento é a dica atual e o segundo elemento é a dica anterior
            lista_verificações.append(verificacao(valor))
        
        if count == 10:
            messagebox.showinfo("", "Você perdeu!!!!!")
            i.destroy()
    
    
    

i = Tk()
i.title('GuessGame')
i['bg'] = 'gray'
resp = messagebox.askyesno("","GUESSGAME!!\nVocê ganhará o jogo se acertar o número que irei pensar:\n\n \
► O valor que estarei pensando estará entre 1 e 100 e você terá 10 chances para acertá-lo.\n \
► A cada tentativa, eu lhe darei uma pista sobre o quão próximo foi o seu palpite em relação ao alvo que estabeleci.\n \
Gostaria de jogar?")
if resp == True:        
    frame1 = Frame(i)
    #frame2 = Frame (i)
    frame1.grid(row=0, column=0)
    lista = []
    botao = []
    for j in range(1,101):
        lista.append(j)
    for j in range(len(lista)):
        if j % 10 == 0:
            subframe = Frame(frame1)
            subframe.pack()
        a = Button (subframe, text = lista[j], bg = 'lightgray',font=("Comic Sans MS", "10", "bold"), bd = 5, pady = 15, padx = 15, width = 5, command = partial (aperta_botao, lista[j]))
        botao.append(a)
        a.pack(side = LEFT)

    dica = Label (i, text = '[DICAS]', fg = 'white', bg = 'gray', font=("Comic Sans MS", "15", "bold"))
    dica.grid(row=1, column=0)

    numero_tentativas = Label (i, text = 'NUMERO DE TENTATIVAS: 10', fg = 'white', bg = 'gray', font=("Comic Sans MS", "15", "bold"))
    numero_tentativas.grid(row=2, column=0)
    
else:
    i.destroy()

i.resizable(width = False, height = False)    
i.mainloop()

import random as rd
import PySimpleGUI as sg
import sys
import time

class EscolhaUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.jogar_novamente = True
        
        
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu chute', size=(40,0))],
            [sg.Input(size=(12,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(38,10))]
        ]
        
        # criar uma janela
        self.janela = sg.Window('Chute o Número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while self.jogar_novamente == True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # fazer algo com eles
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute'] 
                    while self.jogar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais Alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.jogar_novamente = False
                            print('PARABÉNS, VOCE ACERTOU!!')
                            time.sleep(1)
                            print('PARABÉNS, VOCE ACERTOoooooooOU!!')
                            time.sleep(1)
                            print('Aí sim 😎')
                            time.sleep(2)
                            break   
        except:
            print('FAVOR DIGITAR UM VALOR VÁLIDO')
            self.Iniciar()
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = rd.randint(self.valor_minimo, self.valor_maximo)
        
    
Jogo = EscolhaUmNumero()
Jogo.Iniciar()

# Projeto 1: Criar um programa que simule a ação de jogar um dado e obter
# um número aleatório de 1 à 6.
# Projeto 2: Criar uma tela pra ele.
import random as rd
import PySimpleGUI as sg
import time

# classe do nosso dado
class SimuladorDado():
    def __init__(self):
        # definir constantes
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Quer jogar o dado?'
        sg.theme('DarkGrey12')
        self.layout = [
            [sg.Text(self.mensagem,font='bold')],
            [sg.Output(size=(50,10), text_color='white')],
            [sg.Button('SIM',key='s'), sg.Button('NÃO',key='n')]
        ]
    
    # função iniciar    
    def Iniciar(self):
        # criar janela
        self.janela = sg.Window('Gerador de Dado', layout=self.layout, use_default_focus=False)
        while True:
            # ler valores
            self.eventos, self.valores = self.janela.Read()
            # tomada de decisões
            if self.eventos == 's':
                self.GirarDado()
            if self.eventos == 'n' or self.eventos == sg.WIN_CLOSED:
                print('Obrigador! Tchau!')
                time.sleep(2)
                self.janela.close()
                break
                
    def GirarDado(self):
        valor = rd.randint(self.valor_minimo,self.valor_maximo)
        self.DadoImagem(valor)
        
    def DadoImagem(self, numero):
        if numero == 1:
            print(' _______')
            print('|            |')
            print('|     O     |')
            print('|_______|')
            print('Um ás solitário!')
        elif numero == 2:
            print(' _______')
            print('|          O|')
            print('|            |')
            print('|O_____ |')
            print('Um duque! Dose dupla!')
        elif numero == 3:
            print(' _______')
            print('|          O|')
            print('|     O     |')
            print('|O_____ |')
            print('Uma trinca! Yeah!')
        elif numero == 4:
            print(' _______')
            print('|O       O|')
            print('|            |')
            print('|O____O|')
            print('Uma quadra estilosa!')
        elif numero == 5:
            print(' _______')
            print('|O       O|')
            print('|     O     |')
            print('|O____O|')
            print('Uma quina magnífica!')  
        elif numero == 6:
            print(' _______ ')
            print('|O       O|')
            print('|O       O|')
            print('|O____O|')
            print('Uaaaau, uma sena completa!')
               
        
dado = SimuladorDado()
dado.Iniciar()
        
# Projeto 3: Criar um game de adivinhação de números
# Projeto 4: Criar uma tela para ele

# libs necessárias
import random as rd
import PySimpleGUI as sg
import time

# Criar a classe do game
class EscolhaUmNumero:
    # Definições iniciais
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.jogar_novamente = True
        
    # escopo do programa    
    def Iniciar(self):
        # layout da tela
        layout = [
            [sg.Text('Seu chute', size=(40,0))],
            [sg.Input(size=(12,0),key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(38,10))]
        ]
        
        # criar uma janela
        self.janela = sg.Window('Chute o Número!', layout=layout)
        
        # chamar função randint
        self.GerarNumeroAleatorio()
        try:
            while self.jogar_novamente == True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # definiçãode fluxo
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute'] 
                    while self.jogar_novamente == True:
                        # dicas s2
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
                            # finalizar caso acerte
                            break
                elif self.evento == sg.WIN_CLOSED:
                    self.janela.close()
                    break
        except:
            print('FAVOR DIGITAR UM VALOR VÁLIDO')
            self.Iniciar()
    
    # função por trás do número     
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = rd.randint(self.valor_minimo, self.valor_maximo)

# instanciar nossa classe        
Jogo = EscolhaUmNumero()
Jogo.Iniciar()

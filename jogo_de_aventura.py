# Projeto 7: Criar um Jogo de Aventura com finais diferentes
# Projeto 8: Criar uma tela para ele.

 
# Primeiro vou definir uma história.
"""
Vamos começar com uma introdução: 
ATENÇÃO!!!
Você estava em uma missão dupla até Saturno...
Sua nave bateu em um asteróide está perdendo pressão aos poucos...
Como impacto você bateu a cabeça e perdeu a memória... não temos muito tempo...
As chances de sobrevivência são quase nulas...
Com sorte a outra nave da missão estava intacta...
Tome as melhores decisões ou JÁ ERA!!! Irá acontecer o pior!!!
"""
# Início definido, agora vamos pensar nos finais possíveis e definir caminhos para eles:
# O primeiro final é o melhor, com base nele vamos pensar nos 'erros da missão'.
# Conseguir se salvar e retornar para a terra.
    # Se conseguir destravar a porta do cockpit, vai chegar no painel de controle.
    # Se souber qual botão apertar consegue usar o rádio.
    # Se virar a nave para o lado certo o sinal chega mais rapido e consegue avisar outra nave a tempo.
# Ficar sem oxigênio e 'ja era'.
    # Se não destravar a porta, não consegue chegar ao painel de controle e tudo está perdido.
# Quase conseguir se salvar, porém, não conseguiu a tempo.
    # Se não apertar o botão certo, o sistema desliga automaticamente e JÁ ERA!!!
    # Se virar a nave pro lado errado, ela bate em outro asteróide e o fim chega do mesmo jeito!

# Agora sim vamos lá.

# libs necessárias
import PySimpleGUI as sg
import sys
import time

# Primeiro vamos criar uma classe para o game
class SpaceAdventure:
    def __init__(self):
        # definir algumas constantes, a história inicial, as opções possíveis e o layout da janela
        self.historia = 'ATENÇÃO!!!\nVocê estava em uma missão dupla até Saturno...\nSua nave bateu em um asteróide está perdendo pressão aos poucos...\nVocê não tem muito tempo e...\nAs chances de sobrevivência são quase nulas...\nSe tiver sorte a outra nave da missão poderá receber seu sinal...\nTome as melhores decisões ou JÁ ERA!!! Irá acontecer o pior!!!'
        # aqui vamos fazer uma tupla para usar o mínimo de variáveis possível
        self.opcoesPossiveis = (
            'Para destravar a porta, escolha a senha CERTA:\nrES703r4d4 [1]     teRr2sATurn [2]',
            'Aperte o botão CORRETO para usar o rádio:\nMHZ(GMArconi) [1]     StrongBye[2]', 
            'Redirecione a nave para enviar o sinal para a outra missão:\n194°FahrRadians [1]     100N°toStone [2]',  
        )
        sg.theme('DarkBlue8')
        self.layout = [
            [sg.Output(size=(60,15))],
            [sg.Button('Iniciar',key=5,size=(11,2),button_color=('white','green'),font='bold'),
            sg.Button('1',key=1,size=(11,2),button_color=('white','black'),font='bold'),
            sg.Button('2',key=2,size=(11,2),button_color=('white','black'),font='bold'),
            sg.Button('Desistir',key=0,size=(11,2),button_color=('white', 'red'),font='bold')],
        ]
        
    # Função iniciar
    def Iniciar(self):
        # criar a janela primeiro e as funções de decisão após
        self.janela = sg.Window('Space Adventure', layout=self.layout)
        # ler os valores
        self.eventos, self.valores = self.janela.Read()
        while True:
            # tratar os cancelamentos primeiro
            if self.eventos == 0 or self.eventos == sg.WIN_CLOSED:
                break
            elif self.eventos == 5:
                # simular a digitação 
                self.DigitarMensagem(self.historia)
                # as estruturas de decisão ficam mais facil se pensar "qaundo completar 3 decisões certas ganha"
                # então precisamos de 3 if aninhados, e 2 elifs apenas
                # Vamos começão o game!
                print('\nVAMOS LÁ!!!')
                print(self.opcoesPossiveis[0])
                #vamos ler os valores a cada opção para não seguir direto pra outra
                self.eventos, self.valores = self.janela.Read()
                if self.eventos == 2:
                    print('OK, agora...')
                    print(self.opcoesPossiveis[1])
                    self.eventos, self.valores = self.janela.Read()
                    if self.eventos == 1:
                        print('OK, então...')
                        print(self.opcoesPossiveis[2])
                        self.eventos, self.valores = self.janela.Read()
                        if self.eventos == 1:
                            print('VAMOS SOBREVIVER HOUSTON!!!')
                            time.sleep(1)
                            print('PARABÉNS, VOCÊ ESCOLHEU O MELHOR CAMINHO!')
                            time.sleep(1)
                            print('A AJUDA ESTÁ VINDO!')
                            time.sleep(5)
                            self.eventos = 0
                            break
                    elif self.eventos == 2:                     
                        print('O sistema está sendo desligado...')
                        time.sleep(1)
                        print('Não vamos conseguir...')
                        print('É o fim.') 
                        time.sleep(5)
                        self.janela.close()
                        break               # no caso de dar errado 'a missão', o jogo quita
                elif self.eventos == 1:
                    time.sleep(1)
                    print('Não vamos conseguir...')
                    print('É o fim.')
                    time.sleep(5)
                    self.janela.close()
                    break
                
    #função pra simular digitação        
    def DigitarMensagem(self,mensagem):
        for letter in mensagem:
            sys.stdout.write(letter)
            #time.sleep(0.05)
            if letter == "\n":
                time.sleep(0.7)
             
            
# por último vamos instanciar nossa classe
game = SpaceAdventure()
game.Iniciar()

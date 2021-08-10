# Projeto 5: Game Decida por Mim, onde você pergunta pro programa e ele te responde
# Projeto 6: Criar uma tela para ele
import random as rd
import PySimpleGUI as sg

# cirar classe do game
class DecidaPorMim:
    def __init__(self):
        # colocar algymas respotas predefinidas
        self.respostas = [
            'É...Acho que é a coisa certa a se fazer!',
            'Nossa... Você tá com neurônios faltando...kkk',
            'Levando em conta os fatos, isso seria horrível!',
            'Claro, por que não?',
            'Justo agora? Sério?',
            'Bom, faz o que você quiser...',
        ]
    # função iniciar    
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça sua pergunta:',auto_size_text=True,text_color='black',font='bold')],
            [sg.Text('(conselhos duvidosos)', text_color='grey')],
            [sg.Input()],
            [sg.Output(size=(45,13))],
            [sg.Button('DECIDA POR MIM')],
        ]
        # criar janela
        self.janela = sg.Window('Decida por mim1', size=(350,340), layout=layout)
        while True:
            # ler valores
            self.eventos, self.valores = self.janela.Read()
            # tomar decisão
            if self.eventos == 'DECIDA POR MIM':
                print(rd.choice(self.respostas))
            else:
                break
        
decida = DecidaPorMim()
decida.Iniciar()
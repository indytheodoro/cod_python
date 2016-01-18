# -*- coding: utf-8 -*- 
from Tkinter import *

class FilmeMaisVotado (Frame):
    
    listaNomeFilmes=[]
    arq=open('FILMESvsNOTAS_.csv','r')
          
    def procuraMaisVotado(self):
        voto = 0
        filme = None
        for linha in self.arq:
            lista=linha.split('|')
            if lista[0][0]!="\"":
                if int(lista[2]) > voto:
                    voto=int(lista[2])
                    filme = lista[0]
        self.etiqueta['text'] = filme
        self.arq.close()


    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Filme mais votado')
        Frame.__init__(self,framePai)
        self.etiqueta = Label(self.janela)
        self.etiqueta['text']=""
        self.etiqueta.pack()
        self.pack()

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'

        
    




# -*- coding: utf-8 -*- 
from Tkinter import *
from random import *

class QtdFilmesAno (Frame):
    
    
          
    def procuraFilmesAno(self):
        anoINICIAL=int(self.anoinicial.get().strip('\n'))
        anoFIM=int(self.anofim.get().strip('\n'))
        qtt=0
        arq=open('FILMESvsNOTAS_.csv','r')
        for linha in arq:
            lista=linha.split('|')
            if lista[0][0]!="\"" and int(lista[3])>=anoINICIAL and int(lista[3])<=anoFIM:
                qtt+=1
        self.etiqueta['text'] = str(qtt)
        arq.close()

    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Quantidade Filmes_Período')
        Frame.__init__(self,framePai)
        self.linicial = Label(self.janela,text="Ano Inicial")
        self.linicial.grid(row=0,column=0)
        self.anoinicial = Entry(self.janela)
        self.anoinicial.grid(row=0,column=1)
        self.anofim = Entry(self.janela)
        self.anofim.grid(row=1,column=1)
        self.lfim = Label(self.janela,text="Ano Final")
        self.lfim.grid(row=1,column=0)
        self.botao = Button(self.janela,text="Mostrar",command=self.procuraFilmesAno).grid(row=1,column=2)
        self.etiqueta = Label(self.janela)
        self.etiqueta['text']=""
        self.etiqueta.grid(row=2,column=0,columnspan=2)

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'

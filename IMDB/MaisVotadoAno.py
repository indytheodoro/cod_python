# -*- coding: utf-8 -*- 
from Tkinter import *

class FilmeMaisVotadoAno (Frame):
           
    def procuraMaisVotado(self):  
        voto = 0
        ano=int(self.anoinicial.get().strip('\n'))
        arq=open('FILMESvsNOTAS_.csv','r')
        for linha in arq:
            lista=linha.split('|')
            if lista[0][0]!="\"" and int(lista[3])==ano and int(lista[2]) > voto:
                voto=int(lista[2])
                filme = lista[0]
        self.etiqueta['text'] = filme + " - " + str(voto)
        arq.close()

    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Mais Votado Ano')
        Frame.__init__(self,framePai)
        self.linicial = Label(self.janela,text="Ano Inicial")
        self.linicial.grid(row=0,column=0)
        self.anoinicial = Entry(self.janela)
        self.anoinicial.grid(row=0,column=1)
        self.botao = Button(self.janela,text="Mostrar",command=self.procuraMaisVotado).grid(row=0,column=2)
        self.etiqueta = Label(self.janela)
        self.etiqueta['text']=""
        self.etiqueta.grid(row=2,column=0,columnspan=2)

       

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'

        
    




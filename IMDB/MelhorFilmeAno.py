# -*- coding: utf-8 -*- 
from Tkinter import *

class MelhorFilmeAno (Frame):
    
          
    def procuraMelhorFilmeAno(self):
        melhor = 0
        ano=int(self.anoinicial.get().strip('\n'))
        arq=open('FILMESvsNOTAS_.csv','r')
        nome = None
        for linha in arq:
            lista=linha.split('|')
            if lista[0][0]!="\"":
                filme = lista[0]
                voto= float(lista[2])
                media = float(lista[1])
                if voto > 25000 and int(lista[3])==ano:
                    nota = (voto / (voto + 25000)) * media + (25000 / (voto + 25000))
                    if nota > melhor:
                        melhor = nota
                        nome = "Melhor Filme: " + filme + " / " + "Nota: " + " -  %.1f" %  nota
        self.etiqueta['text'] = nome
        arq.close()


    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Melhor Filme Ano')
        Frame.__init__(self,framePai)
        self.linicial = Label(self.janela,text="Ano Inicial")
        self.linicial.grid(row=0,column=0)
        self.anoinicial = Entry(self.janela)
        self.anoinicial.grid(row=0,column=1)
        self.botao = Button(self.janela,text="Mostrar",command=self.procuraMelhorFilmeAno).grid(row=0,column=2)
        self.etiqueta = Label(self.janela)
        self.etiqueta['text']=""
        self.etiqueta.grid(row=2,column=0,columnspan=2)

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'


""""
média ponderada (WR) = (v ÷ (v + m)) × R + (m ÷ (v + m))
em que:
R = média para o filme (mean) = (Rating)
v = Número de votos para o filme = (votos)
m = mínimo de votos necessários para ser listado no Top 250 (atualmente 25000)
"""
        
    




# -*- coding: utf-8 -*- 
from Tkinter import *

class MelhorFilme (Frame):
    
    listaNomeFilmes=[]
    arq=open('FILMESvsNOTAS_.csv','r')
          
    def procuraMelhorFilme(self):
        melhor = 0
        nome = None
        for linha in self.arq:
            lista=linha.split('|')
            if lista[0][0]!="\"":
                filme = lista[0]
                voto= float(lista[2])
                media = float(lista[1])
                if voto > 25000:
                    nota = (voto / (voto + 25000)) * media + (25000 / (voto + 25000))
                    if nota > melhor:
                        melhor = nota
                        nome = "Melhor Filme: " + filme + " / " + "Nota: " + " -  %.1f" % nota
        self.etiqueta['text'] = nome
        self.arq.close()


    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Melhor Filme')
        Frame.__init__(self,framePai)
        self.etiqueta = Label(self.janela)
        self.etiqueta['text']=""
        self.etiqueta.pack()
        self.pack()

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'


""""
média ponderada (WR) = (v ÷ (v + m)) × R + (m ÷ (v + m))
em que:
R = média para o filme (mean) = (Rating)
v = Número de votos para o filme = (votos)
m = mínimo de votos necessários para ser listado no Top 250 (atualmente 25000)
"""
        
    




# -*- coding: utf-8 -*- 
from Tkinter import *
from operator import itemgetter, attrgetter

class RankingMelhorFilme (Frame):
    
         
    def procuraMelhorFilme(self):
        arq=open('FILMESvsNOTAS_.csv','r')
        numero = int(self.numero.get().strip('\n'))
        nota=0.0
        ranking = []
        self.texto.delete(0,END)
        for linha in arq:
            lista=linha.split('|')
            if lista[0][0]!="\"":
                filme = lista[0]
                voto= float(lista[2])  
                media = float(lista[1])
                if voto > 25000:
                    nota = (voto / (voto + 25000)) * media + (25000 / (voto + 25000))                   
                    ranking.append([filme,nota])
        ranking=sorted(ranking,key=itemgetter(1), reverse=True)
        for elemento in ranking[:numero]:
            exibir=elemento[0]+ " -  %.1f" % elemento[1]
            self.texto.insert(END,exibir)        
        
        self.texto.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.texto.yview)
        arq.close()
    


    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Ranking Melhores Filmes')
        Frame.__init__(self,framePai)
        self.lnumero = Label(self.janela,text="Top")
        self.lnumero.grid(row=0,column=0)
        self.numero = Entry(self.janela)
        self.numero.grid(row=0,column=1)
        self.botao = Button(self.janela,text="Mostrar",command=self.procuraMelhorFilme).grid(row=1,column=2)
        self.scroll = Scrollbar(self.janela)
        self.scroll.grid(row=2,column=2, sticky=N+S)
        self.texto = Listbox(self.janela)
        self.texto["height"] = 20
        self.texto["width"] = 90
        self.texto.grid(row=2,column=0,columnspan=2)

if __name__ == '__main__':
    print 'Abriu o Arquivo errado'


""""
média ponderada (WR) = (v ÷ (v + m)) × R + (m ÷ (v + m))
em que:
R = média para o filme (mean) = (Rating)
v = Número de votos para o filme = (votos)
m = mínimo de votos necessários para ser listado no Top 250 (atualmente 25000)
"""
        
    




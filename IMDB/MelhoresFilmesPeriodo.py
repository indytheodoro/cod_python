# -*- coding: utf-8 -*- 
from Tkinter import *
from random import *


class MelhoresFilmesPeriodo (Frame):
    
    listaNomeFilmes=[]
    
          
    def procuraFilmesAno(self):
        nota = 0
        anoINICIAL=int(self.anoinicial.get().strip('\n'))
        anoFIM=int(self.anofim.get().strip('\n'))
        global listaNomeFilmes
        arq=open('FILMESvsNOTAS_.csv','r')
        for linha in arq:
	    lista=linha.split('|')
	    if lista[0][0]!="\"":
		filme = lista[0]
		voto= float(lista[2])
		media = float(lista[1])
		if voto > 25000 and int(lista[3])>=anoINICIAL and int(lista[3])<=anoFIM:
		    nota = (voto / (voto + 25000)) * media + (25000 / (voto + 25000))
		    self.listaNomeFilmes.append(filme+ " - "+ lista[1] + " - " + lista[3])                          
        for linha in self.listaNomeFilmes:
           self.texto.insert(END,linha)
        self.texto.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.texto.yview)

        arq.close()

    def __init__(self,framePai):
        self.janela=Toplevel(framePai)
        self.janela.title('Melhores Filmes_Período')
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
        self.scroll = Scrollbar(self.janela)
        self.scroll.grid(row=2,column=2, sticky=N+S)
        self.texto = Listbox(self.janela)
        self.texto["height"] = 20
        self.texto["width"] = 90
        self.texto.grid(row=2,column=0,columnspan=2)



if __name__ == '__main__':
    print 'Abriu o Arquivo errado'

        
    

"""
“Quantidade de filmes produzidos em um intervalo (anos)” e “Quais os
melhores filmes entre um intervalo (anos)”
* Deverá haver alguma forma de perguntar ao usuário qual o ano inicial
e final
"""

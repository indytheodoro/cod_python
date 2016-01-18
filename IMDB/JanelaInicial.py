# -*- coding: utf-8 -*- 
from Tkinter import *
from MaisVotado import *
from MelhorFilme import *
from QtdFilmesPeriodo import *
from MelhoresFilmesPeriodo import *
from MaisVotadoAno import *
from MelhorFilmeAno import *
from RankingMelhoresFilmesSelecionados import *
from RankingMelhoresFilmes import *

class JanelaPrincipal (Frame):
    filho=0
    def __init__(self):
        self.principal=Tk()
        Frame.__init__(self,self.principal)
        BV = Label(self.principal, text="ESCOLHA SUA OPÇÃO DE BUSCA ABAIXO: \n")
        BV.pack()
        
        
        # BOTAO FILME MAIS VOTADO
        self.pesqBot = Button(self)
        self.pesqBot["text"] = "Mais votado"        
        self.pesqBot["command"] =  self.JanelaMaisVotado
        self.pesqBot.pack()   
        
        # BOTAO MELHOR FILME
        self.pesqBot1 = Button(self)
        self.pesqBot1["text"] = "Melhor filme"        
        self.pesqBot1["command"] =  self.JanelaMelhorFilme
        self.pesqBot1.pack()
        
        # BOTAO QUANTIDADE DE FILMES PRODUZIDOS EM INTERVALO DE ANO
        self.pesqBot2 = Button(self)
        self.pesqBot2["text"] = "Filmes produzidos por Periodo"        
        self.pesqBot2["command"] =  self.JanelaQtdFilmesAno
        self.pesqBot2.pack()
        
        # BOTAO MELHORES FILMES POR PERIODO
        self.pesqBot3 = Button(self)
        self.pesqBot3["text"] = "Melhores Filmes por Periodo"        
        self.pesqBot3["command"] =  self.JanelaMelhoresPeriodo
        self.pesqBot3.pack()

        # BOTAO O MAIS VOTADO NO ANO
        self.pesqBot4 = Button(self)
        self.pesqBot4["text"] = "Mais votado no Ano"        
        self.pesqBot4["command"] =  self.JanelaFilmeMaisVotadoAno
        self.pesqBot4.pack()
        
        # BOTAO O MELHOR NO ANO
        self.pesqBot5 = Button(self)
        self.pesqBot5["text"] = "Melhor no Ano"        
        self.pesqBot5["command"] =  self.JanelaMelhorFilmeAno
        self.pesqBot5.pack()
        
        # BOTAO Ranking dos filmes dentre os selecionados
        self.pesqBot6 = Button(self)
        self.pesqBot6["text"] = "Ranking Melhores Selecionados"        
        self.pesqBot6["command"] =  self.JanelaRankingMelhoresSelecionados
        self.pesqBot6.pack()
        
        # BOTAO Ranking dos melhores filmes
        self.pesqBot7 = Button(self)
        self.pesqBot7["text"] = "Ranking Melhores Filmes"        
        self.pesqBot7["command"] =  self.JanelaRankingMelhorFilme
        self.pesqBot7.pack()
        
        
       
        self.principal.title('Opções de Busca')
        self.pack()
        self.mainloop()
        
        
    def JanelaMaisVotado(self):
        self.filho=FilmeMaisVotado(self)
        self.filho.procuraMaisVotado()

    def JanelaMelhorFilme(self):
        self.filho=MelhorFilme(self)
        self.filho.procuraMelhorFilme()
    
    def JanelaQtdFilmesAno(self):
        self.filho=QtdFilmesAno(self)

    def JanelaMelhoresPeriodo(self):
        self.filho=MelhoresFilmesPeriodo(self)
        
    def JanelaFilmeMaisVotadoAno(self):
        self.filho=FilmeMaisVotadoAno(self)
        
    def JanelaMelhorFilmeAno(self):
        self.filho=MelhorFilmeAno(self)

    def JanelaRankingMelhoresSelecionados(self):
        self.filho=RankingMelhoresSelecionados(self)

    def JanelaRankingMelhorFilme(self):
        self.filho=RankingMelhorFilme(self)



if __name__ == '__main__':
    Janelinha=JanelaPrincipal()
 



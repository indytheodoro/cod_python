# -*- coding: utf-8 -*- 
from Tkinter import *
from random import *

class Application(Frame):
    filmes={}
    listaNomeFilmes=[]
    posProcura=0
    textoAtual=""
    
    def AbrirArquivo(self):
        f=open('FILMESvsNOTAS_.csv','r')
        for i in f:
            if i[0]!="\"":
                i=i.split('|')
                self.filmes[i[0]]=(i[3].strip('\n'),i[2],i[1])
                self.listaNomeFilmes.append(i[0])
        self.listaNomeFilmes.sort()
        f.close()
        
    def procura(self):
        palavra = (self.pesquisa.get(1.0,END)).strip('\n')
        tam=len(self.listaNomeFilmes)
        if palavra !=self.textoAtual:
            self.posProcura=0
            self.textoAtual=palavra
        for i in xrange(self.posProcura+1,tam):
            if palavra.encode('utf-8').lower() in self.listaNomeFilmes[i].lower():
                self.posProcura=i 
                break
        if i >= tam-1:
            self.posProcura=0
        self.texto.select_clear(0,END)
        self.texto.select_set(i)
        self.texto.see(i)
        
            
    def pegaSelecionados(self):
        for i in self.texto.curselection():
            print self.texto.get(i)
        
            
    def createWidgets(self):
        self.pesquisa = Text(self)
        self.pesquisa["height"] = 1
        self.pesquisa["width"] = 20
        self.pesquisa.grid(row=0)
        self.pesqBot = Button(self)
        self.pesqBot["text"] = "Pesquisa"
        self.pesqBot["fg"]   = "red"
        self.pesqBot["command"] =  self.procura
        self.pesqBot.grid(row=0,column=1)
        self.scroll = Scrollbar(self)
        self.scroll.grid(row=1,column=2, sticky=N+S)
        self.texto = Listbox(self,selectmode=EXTENDED)
        self.texto["height"] = 30
        self.texto["width"] = 90
        self.texto.grid(row=1,column=0,columnspan=2)
        self.QUIT = Button(self)
        self.QUIT["text"] = "Sair"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        
        for i in self.listaNomeFilmes:
           self.texto.insert(END,i)
        
        self.texto.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.texto.yview)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.AbrirArquivo()
        self.createWidgets()
        

root = Tk()
app = Application(master=root)
app.mainloop()

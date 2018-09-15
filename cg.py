from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import math
from bitstring import *


class Application1:   

    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.fontePadrao = ("Arial", "10")

        self.canvas_width = 1000
        self.canvas_height = 800

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 10
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 10
        self.quintoContainer.pack()


        self.w = Canvas(self.quintoContainer,
           width=self.canvas_width,
           height=self.canvas_height)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.configure(scrollregion=(-400, -400, 400, 400))

        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = 0


        self.label1 = Label(self.primeiroContainer,text="Ponto inicial", font=self.fontePadrao)

#-----------------Entrada x1----------------------------
        self.labelx1 = Label(self.primeiroContainer, text="Xinicial: ", font=self.fontePadrao)
        self.labelx1.pack(side=LEFT)

        self.entradax1 = Entry(self.primeiroContainer)
        self.entradax1["width"] = 10
        self.entradax1["font"] = self.fontePadrao
        self.entradax1.pack(side=LEFT)

#-----------------Entrada y1----------------------------
        self.labely1 = Label(self.segundoContainer, text="Yinicial: ", font=self.fontePadrao)
        self.labely1.pack(side=LEFT)

        self.entraday1 = Entry(self.segundoContainer)
        self.entraday1["width"] = 10
        self.entraday1["font"] = self.fontePadrao
        self.entraday1.pack(side=LEFT)

#-----------------Entrada xfinal----------------------------
        self.labelx2 = Label(self.primeiroContainer, text="Xfinal: ", font=self.fontePadrao)
        self.labelx2.pack(side=LEFT)

        self.entradax2 = Entry(self.primeiroContainer)
        self.entradax2["width"] = 10
        self.entradax2["font"] = self.fontePadrao
        self.entradax2.pack(side=LEFT)
 
#-----------------Entrada yfinal----------------------------
        self.labely2 = Label(self.segundoContainer, text="Yfinal: ", font=self.fontePadrao)
        self.labely2.pack(side=LEFT)

        self.entraday2 = Entry(self.segundoContainer)
        self.entraday2["width"] = 10
        self.entraday2["font"] = self.fontePadrao
        self.entraday2.pack(side=LEFT)

#----------------Raio---------------------------------------
        self.labelraio = Label(self.terceiroContainer, text="Raio: ", font=self.fontePadrao)
        self.labelraio.pack()

        self.entradaraio = Entry(self.terceiroContainer)
        self.entradaraio["width"] = 10
        self.entradaraio["font"] = self.fontePadrao
        self.entradaraio.pack()

#-------------------Botao------------------------------------        
        self.label2 = Label(self.quartoContainer,text="Ponto final", font=self.fontePadrao)
        self.botaoDDA = Button(self.quartoContainer)
        self.botaoDDA["font"] = self.fontePadrao
        self.botaoDDA["width"] = 10
        self.botaoDDA["text"] = 'DDA'
        self.botaoDDA["command"] = self.Algoritmo_DDA
        self.botaoDDA.pack(side=LEFT)

        self.botaoBresenhamReta = Button(self.quartoContainer)
        self.botaoBresenhamReta["font"] = self.fontePadrao
        self.botaoBresenhamReta["width"] = 14
        self.botaoBresenhamReta["text"] = 'Bresenham: Reta'
        self.botaoBresenhamReta["command"] = self.Algoritmo_Bresenham
        self.botaoBresenhamReta.pack(side=LEFT)

        self.botaoBresenhamCirculo = Button(self.quartoContainer)
        self.botaoBresenhamCirculo["font"] = self.fontePadrao
        self.botaoBresenhamCirculo["width"] = 24
        self.botaoBresenhamCirculo["text"] = 'Bresenham: Circunferência'
        self.botaoBresenhamCirculo["command"] = self.Algoritmo_Bresenham_Circulo
        self.botaoBresenhamCirculo.pack(side=LEFT)

        self.botaoApagar = Button(self.quartoContainer)
        self.botaoApagar["font"] = self.fontePadrao
        self.botaoApagar["width"] = 14
        self.botaoApagar["text"] = 'Apagar'
        self.botaoApagar["command"] = self.Apagar
        self.botaoApagar.pack(side=LEFT)

    
    def Apagar (self):
        self.w.delete("all")


    def Algoritmo_DDA (self):
        self.x1 = float(self.entradax1.get())
        self.y1 = float(self.entraday1.get())
        self.x2 = float(self.entradax2.get())
        self.y2 = float(self.entraday2.get())
        x = self.x1
        y = self.y1
        #self.w.create_oval(self.x1, self.y1, self.x2, self.y2)
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        if (abs(dx) > abs(dy)):
            passos = abs(dx)
        else:
            passos = abs(dy)
        Xincr = dx/passos
        Yincr = dy/passos
        self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line")
        i = 0
        while(i < passos):
            x = x + Xincr
            y = y + Yincr
            self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line")
            i = i + 1



    def Algoritmo_Bresenham (self):
        self.x1 = int(self.entradax1.get())
        self.y1 = int(self.entraday1.get())
        self.x2 = int(self.entradax2.get())
        self.y2 = int(self.entraday2.get())
        x = self.x1
        y = self.y1
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        
        #self.w.create_text(x, y, text = ".", tag = "line")
        if (dx < 0):
            dx = abs(dx)
            Xincr = -1
        else :
            Xincr = 1

        if (dy < 0):
            dy = abs(dy)
            Yincr = -1;
        else:
            Yincr = 1;
        
        if (dx > dy):
            p = 2*(dy) - dx
            const1 = 2*dy 
            const2 = 2*(dy - dx)
            for i in range(dx) :
                x += Xincr
                if (p < 0):
                    p += const1
                else:
                    y += Yincr
                    p += const2
                self.w.create_text(x, y, text = ".", tag = "line", fill='green')
        else :
            p = 2*(dx) - dy
            const1 = 2*dx
            const2 = 2*(dx - dy)
            for i in range(dy):
                y += Yincr
                if (p < 0):
                    p += const1
                else:
                    p += const2
                    x += Xincr
                self.w.create_text(x, y, text = ".", tag = "line", fill='green')


    def Algoritmo_Bresenham_Circulo (self):
        r = int(self.entradaraio.get())
        xc =  int(self.entradax1.get())
        yc =  int(self.entraday1.get())
        x = 0
        y = r 
        p = 3 - 2*(r)
        #print(x,y)
        self.plotaSimetricos(xc= xc, yc= yc, x= x, y= y)
        #self.plotaSimetricos(x, y) 
        while (x <= y):
            if ( p < 0 ):
                p += 4*(x) + 6
            else:
                p += 4*(x-y) + 10
                y = y -1
            x = x + 1
            #print(x,y)
            self.plotaSimetricos(xc= xc, yc= yc, x= x, y= y)
            #self.plotaSimetricos(x, y)



    def plotaSimetricos(self, xc, yc, x, y):
        # second quarter 4.octant
        self.w.create_text(xc+x, yc+y, text = ".", tag = "line")
        #print ((xc + x), (yc+y))
        # first quarter first octant
        self.w.create_text(xc-x, yc+y, text = ".", tag = "line")
        # third quarter 5.octant
        self.w.create_text(xc+x, yc-y, text = ".", tag = "line")
        # fourth quarter 8.octant
        self.w.create_text(xc-x, yc-y, text = ".", tag = "line")
        # first quarter 2nd octant
        self.w.create_text(xc+y, yc+x, text = ".", tag = "line")
        # second quarter 3rd octant
        self.w.create_text(xc-y, yc+x, text = ".", tag = "line")
        # third quarter 6.octant
        self.w.create_text(xc+y, yc-x, text = ".", tag = "line")
        # fourth quarter 7.octant
        self.w.create_text(xc-y, yc-x, text = ".", tag = "line")


 #	def inicializar_bf (self):
   # 	xc =  int(self.entradax1.get())
   #     yc =  int(self.entraday1.get())
 #  	self.boundary_fill(xc, yc)
    


   # def boundary_fill (self, x, y):
   # 	cor_atual = obtemCor(x, y)



   # def ObtemCor(self, x, y):

    


#------------------------------Segunda Classe-------------------------------------------
class Application2:   

    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.fontePadrao = ("Arial", "10")

        self.canvas_width = 1000
        self.canvas_height = 800

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 10
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 10
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 10
        self.sextoContainer.pack()


        self.w = Canvas(self.sextoContainer,
           width=self.canvas_width,
           height=self.canvas_height)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.configure(scrollregion=(-400, -400, 400, 400))

        self.x1 = 0
        self.y1 = 0

        self.x2 = 0
        self.y2 = 0


        self.label1 = Label(self.primeiroContainer,text="Ponto inicial", font=self.fontePadrao)

#-----------------Entrada x1----------------------------
        self.labelx1 = Label(self.primeiroContainer, text="Xinicial: ", font=self.fontePadrao)
        self.labelx1.pack(side=LEFT)

        self.entradax1 = Entry(self.primeiroContainer)
        self.entradax1["width"] = 10
        self.entradax1["font"] = self.fontePadrao
        self.entradax1.pack(side=LEFT)

#-----------------Entrada y1----------------------------
        self.labely1 = Label(self.segundoContainer, text="Yinicial: ", font=self.fontePadrao)
        self.labely1.pack(side=LEFT)

        self.entraday1 = Entry(self.segundoContainer)
        self.entraday1["width"] = 10
        self.entraday1["font"] = self.fontePadrao
        self.entraday1.pack(side=LEFT)

#-----------------Entrada xfinal----------------------------
        self.labelx2 = Label(self.primeiroContainer, text="Xfinal: ", font=self.fontePadrao)
        self.labelx2.pack(side=LEFT)

        self.entradax2 = Entry(self.primeiroContainer)
        self.entradax2["width"] = 10
        self.entradax2["font"] = self.fontePadrao
        self.entradax2.pack(side=LEFT)
        
#-----------------Entrada yfinal----------------------------
        self.labely2 = Label(self.segundoContainer, text="Yfinal: ", font=self.fontePadrao)
        self.labely2.pack(side=LEFT)

        self.entraday2 = Entry(self.segundoContainer)
        self.entraday2["width"] = 10
        self.entraday2["font"] = self.fontePadrao
        self.entraday2.pack(side=LEFT)

#----------------Angulo--------------------------------------
        self.labelangulo = Label(self.primeiroContainer, text="Ângulo: ", font=self.fontePadrao)
        self.labelangulo["width"] = 8
        self.labelangulo.pack(side=LEFT)

        self.entradaangulo = Entry(self.primeiroContainer)
        self.entradaangulo["width"] = 10
        self.entradaangulo["font"] = self.fontePadrao
        self.entradaangulo.pack(side=LEFT)

#----------------Forca--------------------------------------
        self.labelforca = Label(self.segundoContainer, text="Força: ", font=self.fontePadrao)
        self.labelforca["width"] = 8
        self.labelforca.pack(side=LEFT)

        self.entradaforca = Entry(self.segundoContainer)
        self.entradaforca["width"] = 10
        self.entradaforca["font"] = self.fontePadrao
        self.entradaforca.pack(side=LEFT)

#---------------Translacao: x e y--------------------------
        self.labeltransx = Label(self.primeiroContainer, text="Translação/Escala x: ", font=self.fontePadrao)
        self.labeltransx["width"] = 20
        self.labeltransx.pack(side=LEFT)

        self.entradatransx = Entry(self.primeiroContainer)
        self.entradatransx["width"] = 10
        self.entradatransx["font"] = self.fontePadrao
        self.entradatransx.pack(side=LEFT)

        self.labeltransy = Label(self.segundoContainer, text="Translação/Escala y: ", font=self.fontePadrao)
        self.labeltransy["width"] = 20
        self.labeltransy.pack(side=LEFT)

        self.entradatransy = Entry(self.segundoContainer)
        self.entradatransy["width"] = 10
        self.entradatransy["font"] = self.fontePadrao
        self.entradatransy.pack(side=LEFT)

#-------------------Botao------------------------------------   
#-------------------Priimeira Linha--------------------------
        self.botaocisalhamentox = Button(self.terceiroContainer)
        self.botaocisalhamentox["font"] = self.fontePadrao
        self.botaocisalhamentox["width"] = 18
        self.botaocisalhamentox["text"] = 'Cisalhamento: x'
        self.botaocisalhamentox["command"] = self.Cisalhamento_x
        self.botaocisalhamentox.pack(side=LEFT)  

        self.botaocisalhamentoy = Button(self.terceiroContainer)
        self.botaocisalhamentoy["font"] = self.fontePadrao
        self.botaocisalhamentoy["width"] = 18
        self.botaocisalhamentoy["text"] = 'Cisalhamento: y'
        self.botaocisalhamentoy["command"] = self.Cisalhamento_y
        self.botaocisalhamentoy.pack(side=LEFT)  

        self.botaoApagar = Button(self.terceiroContainer)
        self.botaoApagar["font"] = self.fontePadrao
        self.botaoApagar["width"] = 18
        self.botaoApagar["text"] = 'Apagar'
        self.botaoApagar["command"] = self.Apagar
        self.botaoApagar.pack(side=LEFT)  

#----------------Segunda linha:Botao---------------------------        
        self.botaorx = Button(self.quartoContainer)
        self.botaorx["font"] = self.fontePadrao
        self.botaorx["width"] = 18
        self.botaorx["text"] = 'Reflexão: eixo x'
        self.botaorx["command"] = self.Reflexao_x
        self.botaorx.pack(side=LEFT)

        self.botaory = Button(self.quartoContainer)
        self.botaory["font"] = self.fontePadrao
        self.botaory["width"] = 18
        self.botaory["text"] = 'Reflexão: eixo y'
        self.botaory["command"] = self.Reflexao_y
        self.botaory.pack(side=LEFT)

        self.botaororigem = Button(self.quartoContainer)
        self.botaororigem["font"] = self.fontePadrao
        self.botaororigem["width"] = 18
        self.botaororigem["text"] = 'Reflexão: origem'
        self.botaororigem["command"] = self.Reflexao_origem
        self.botaororigem.pack(side=LEFT)   

#--------------Terceira linha:Botao---------------------------
        self.botaotranslacao = Button(self.quintoContainer)
        self.botaotranslacao["font"] = self.fontePadrao
        self.botaotranslacao["width"] = 18
        self.botaotranslacao["text"] = 'Translação'
        self.botaotranslacao["command"] = self.Translacao
        self.botaotranslacao.pack(side=LEFT)

        self.botaorotacao = Button(self.quintoContainer)
        self.botaorotacao["font"] = self.fontePadrao
        self.botaorotacao["width"] = 18
        self.botaorotacao["text"] = 'Rotação'
        self.botaorotacao["command"] = self.Rotacao
        self.botaorotacao.pack(side=LEFT)

        self.botaoescala = Button(self.quintoContainer)
        self.botaoescala["font"] = self.fontePadrao
        self.botaoescala["width"] = 18
        self.botaoescala["text"] = 'Escala'
        self.botaoescala["command"] = self.Escala
        self.botaoescala.pack(side=LEFT)


#--------------------Algoritmos------------------------------
    def Apagar (self):
        self.w.delete("all")


    def Algoritmo_DDA (self, xi, yi, xf, yf, cor ):
        self.x1 = xi
        self.y1 = yi
        self.x2 = xf
        self.y2 = yf
        x = self.x1
        y = self.y1
        
        #self.w.create_oval(self.x1, self.y1, self.x2, self.y2)
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        if (abs(dx) > abs(dy)):
            passos = abs(dx)
        else:
            passos = abs(dy)
        Xincr = dx/passos
        Yincr = dy/passos
        self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line", fill=cor)
        i = 0
        while(i < passos):
            x = x + Xincr
            y = y + Yincr
            self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line", fill=cor)
            i = i + 1


#---------------------------------Reflexao---------------------------------------------------             
    def Reflexao_x(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])
        matriz_inverterX = np.matrix([[1,0],[0,-1]])

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='green')



    def Reflexao_y(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])
        matriz_inverterX = np.matrix([[-1,0],[0, 1]])

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='blue')


    def Reflexao_origem(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])
        matriz_inverterX = np.matrix([[-1,0],[0, -1]])

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='red')



#-----------------------Cisalhamento----------------------------------------------------
    def Cisalhamento_x(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        forca = float(self.entradaforca.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])
        matriz_inverterX = np.matrix([[1,forca],[0, 1]])

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='red')
        #print (x1final, y1final)
        #print (x2final, y2final)



    def Cisalhamento_y(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        forca = float(self.entradaforca.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])
        matriz_inverterX = np.matrix([[1,0],[forca, 1]])

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='purple')


#-----------------------Translacao----------------------------------------------------
    def Translacao(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        xt = float(self.entradatransx.get())
        yt = float(self.entradatransy.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])

        matriz_somar = np.matrix([[xt],[yt]])
        
        resultado1 = matriz_somar + originais1
        resultado2 = matriz_somar + originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))

        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='purple')



#-----------------------Rotacao----------------------------------------------------
    def Rotacao(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        angulo = float(self.entradaangulo.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])

        seno = np.sin(np.deg2rad(angulo))
        cosseno = math.cos(np.deg2rad(angulo))
        #print (seno, cosseno)
        matriz_inverterX = np.matrix([[cosseno, -seno],[seno, cosseno]])
        #print (matriz_inverterX)

        resultado1 = matriz_inverterX * originais1
        resultado2 = matriz_inverterX * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        #print(x1final, y1final)
        #print (x2final, y2final)

        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='hotpink')


#-----------------------Escala----------------------------------------------------
    def Escala(self):
        x1 = float(self.entradax1.get())
        y1 = float(self.entraday1.get())

        x2 = float(self.entradax2.get())
        y2 = float(self.entraday2.get())

        xt = float(self.entradatransx.get())
        yt = float(self.entradatransy.get())

        self.Algoritmo_DDA(xi= x1,yi= y1, xf= x2, yf= y2, cor='black')

        originais1 = np.matrix([[x1],[y1]])
        originais2 = np.matrix([[x2],[y2]])

        matriz_escala = np.matrix([[xt, 0],[0, yt]])
        
        resultado1 = matriz_escala * originais1
        resultado2 = matriz_escala * originais2

        x1final = float(np.asscalar(resultado1[0]))
        y1final = float(np.asscalar(resultado1[1]))
        x2final = float(np.asscalar(resultado2[0]))
        y2final = float(np.asscalar(resultado2[1]))
        #print(x1final, y1final)
        #print (x2final, y2final)

        self.Algoritmo_DDA(xi= x1final,yi= y1final, xf= x2final, yf= y2final, cor='black')




#----------------------------------Terceira Classe-----------------------------------------

"""class Application3:   

    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.fontePadrao = ("Arial", "10")

        self.canvas_width = 1000
        self.canvas_height = 800

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 10
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 10
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 10
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = 10
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(master)
        self.oitavoContainer["padx"] = 10
        self.oitavoContainer.pack()


        self.w = Canvas(self.oitavoContainer,
           width=self.canvas_width,
           height=self.canvas_height)
        self.w.pack(expand=YES, fill=BOTH)
        self.w.configure(scrollregion=(-400, -400, 400, 400))

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0
        self.x4 = 0
        self.y4 = 0

        self.label1 = Label(self.primeiroContainer,text="Pontos da janela", font=self.fontePadrao)
        self.label1.pack()

#-----------------Entrada 1 da janela----------------------------
        self.label1janelax = Label(self.segundoContainer, text="x1: ", font=self.fontePadrao)
        self.label1janelax.pack(side=LEFT)

        self.x1janela = Entry(self.segundoContainer)
        self.x1janela["width"] = 10
        self.x1janela["font"] = self.fontePadrao
        self.x1janela.pack(side=LEFT)

#-----------------Entrada 2 da janela----------------------------
        self.label2janelax = Label(self.segundoContainer, text="x2: ", font=self.fontePadrao)
        self.label2janelax.pack(side=LEFT)

        self.x2janela = Entry(self.segundoContainer)
        self.x2janela["width"] = 10
        self.x2janela["font"] = self.fontePadrao
        self.x2janela.pack(side=LEFT)

#-----------------Entrada 3 da janela----------------------------
        self.label3janelax = Label(self.segundoContainer, text="x3: ", font=self.fontePadrao)
        self.label3janelax.pack(side=LEFT)

        self.x3janela = Entry(self.segundoContainer)
        self.x3janela["width"] = 10
        self.x3janela["font"] = self.fontePadrao
        self.x3janela.pack(side=LEFT)

#-----------------Entrada 4 da janela----------------------------
        self.label4janelax = Label(self.segundoContainer, text="x4: ", font=self.fontePadrao)
        self.label4janelax.pack(side=LEFT)

        self.x4janela = Entry(self.segundoContainer)
        self.x4janela["width"] = 10
        self.x4janela["font"] = self.fontePadrao
        self.x4janela.pack(side=LEFT)

#-----------------Entrada 1 da janela----------------------------
        self.label1janelay = Label(self.terceiroContainer, text="y1: ", font=self.fontePadrao)
        self.label1janelay.pack(side=LEFT)

        self.y1janela  = Entry(self.terceiroContainer)
        self.y1janela["width"] = 10
        self.y1janela["font"] = self.fontePadrao
        self.y1janela.pack(side=LEFT)

#-----------------Entrada 2 da janela----------------------------
        self.label2janelay = Label(self.terceiroContainer, text="y2: ", font=self.fontePadrao)
        self.label2janelay.pack(side=LEFT)

        self.y2janela  = Entry(self.terceiroContainer)
        self.y2janela["width"] = 10
        self.y2janela["font"] = self.fontePadrao
        self.y2janela.pack(side=LEFT)

#-----------------Entrada 3 da janela----------------------------
        self.label3janelay = Label(self.terceiroContainer, text="y3: ", font=self.fontePadrao)
        self.label3janelay.pack(side=LEFT)

        self.y3janela  = Entry(self.terceiroContainer)
        self.y3janela["width"] = 10
        self.y3janela["font"] = self.fontePadrao
        self.y3janela.pack(side=LEFT)

#-----------------Entrada 4 da janela----------------------------
        self.label4janelay = Label(self.terceiroContainer, text="y4: ", font=self.fontePadrao)
        self.label4janelay.pack(side=LEFT)

        self.y4janela  = Entry(self.terceiroContainer)
        self.y4janela["width"] = 10
        self.y4janela["font"] = self.fontePadrao
        self.y4janela.pack(side=LEFT)

#-------------------------Entradas da reta-------------------------------------
        self.label1reta = Label(self.quartoContainer, text="Pontos da reta: ", font=self.fontePadrao)
        self.label1reta.pack()
#-----------------Entrada x1----------------------------
        self.labelx1 = Label(self.quintoContainer, text="Xinicial: ", font=self.fontePadrao)
        self.labelx1.pack(side=LEFT)

        self.entradax1 = Entry(self.quintoContainer)
        self.entradax1["width"] = 10
        self.entradax1["font"] = self.fontePadrao
        self.entradax1.pack(side=LEFT)

#-----------------Entrada y1----------------------------
        self.labely1 = Label(self.quintoContainer, text="Yinicial: ", font=self.fontePadrao)
        self.labely1.pack(side=LEFT)

        self.entraday1 = Entry(self.quintoContainer)
        self.entraday1["width"] = 10
        self.entraday1["font"] = self.fontePadrao
        self.entraday1.pack(side=LEFT)

#-----------------Entrada xfinal----------------------------
        self.labelx2 = Label(self.sextoContainer, text="Xfinal: ", font=self.fontePadrao)
        self.labelx2.pack(side=LEFT)

        self.entradax2 = Entry(self.sextoContainer)
        self.entradax2["width"] = 10
        self.entradax2["font"] = self.fontePadrao
        self.entradax2.pack(side=LEFT)
        
#-----------------Entrada yfinal----------------------------
        self.labely2 = Label(self.sextoContainer, text="Yfinal: ", font=self.fontePadrao)
        self.labely2.pack(side=LEFT)

        self.entraday2 = Entry(self.sextoContainer)
        self.entraday2["width"] = 10
        self.entraday2["font"] = self.fontePadrao
        self.entraday2.pack(side=LEFT)

#-------------------Botao------------------------------------   
#-------------------Priimeira Linha--------------------------
        self.botaocisalhamentox = Button(self.setimoContainer)
        self.botaocisalhamentox["font"] = self.fontePadrao
        self.botaocisalhamentox["width"] = 18
        self.botaocisalhamentox["text"] = 'Criar janela'
        self.botaocisalhamentox["command"] = self.criarJanela
        self.botaocisalhamentox.pack(side=LEFT)  

        self.botaocisalhamentoy = Button(self.setimoContainer)
        self.botaocisalhamentoy["font"] = self.fontePadrao
        self.botaocisalhamentoy["width"] = 18
        self.botaocisalhamentoy["text"] = 'Criar reta'
        self.botaocisalhamentoy["command"] = self.verRetanaJanela
        self.botaocisalhamentoy.pack(side=LEFT)  

        self.botaoApagar = Button(self.setimoContainer)
        self.botaoApagar["font"] = self.fontePadrao
        self.botaoApagar["width"] = 18
        self.botaoApagar["text"] = 'Apagar'
        #self.botaoApagar["command"] = self.Apagar
        self.botaoApagar.pack(side=LEFT)  


    def criarJanela(self):
    	self.x1 = float(self.x1janela.get())
    	self.y1 = float(self.y1janela.get())

    	self.x2 = float(self.x2janela.get())
    	self.y2 = float(self.y2janela.get())

    	self.x3 = float(self.x3janela.get())
    	self.y3 = float(self.y3janela.get())

    	self.x4 = float(self.x4janela.get())
    	self.y4 = float(self.y4janela.get())

    	self.Algoritmo_DDA(xi= self.x1,yi= self.y1, xf= self.x2, yf= self.y2, cor='black')
    	self.Algoritmo_DDA(xi= self.x2,yi= self.y2, xf= self.x3, yf= self.y3, cor='black')
    	self.Algoritmo_DDA(xi= self.x3,yi= self.y3, xf= self.x4, yf= self.y4, cor='black')
    	self.Algoritmo_DDA(xi= self.x4,yi= self.y4, xf= self.x1, yf= self.y1, cor='black')



    def verRetanaJanela(self):
    	xinicial = float(self.entradax1.get())
    	yinicial = float(self.entraday1.get())

    	xfinal = float(self.entradax2.get())
    	yfinal = float(self.entraday2.get())

    	aceito = False
    	feito = False
    	while(feito == False):
    		cod1 = self.obtemCodigo(xinicial, yinicial, self.x1, self.x2, self.y1, self.y3)
    		cod2 = self.obtemCodigo(xfinal, yfinal, self.x1, self.x2, self.y1, self.y3)
    		if (cod1 == 0 and cod2 == 0):
    			aceito = True
    			feito = True
    		elif ((cod1 and cod2) != 0):
    			feito = True
    		else:
    			if cod1 != 0:
    				cfora = cod1
    			else:
    				cfora = cod2
    			if( self.verificaBit(cfora, 0) == 1):#esq
    				feito = True
    				print ("AAAA")
    			elif ( self.verificaBit(cfora, 1) == 1):#dir
    				print ("BBBB")
    				feito = True
    			elif ( self.verificaBit(cfora, 2) == 1):#up
    				print ("CCCC")
    				feito = True
    			elif ( self.verificaBit(cfora, 3) == 1):
    				print ("DDDD")
    				feito = True
    			else:
    				feito = True


    	if aceito:
    		self.Algoritmo_DDA(xinicial, yinicial, xfinal, yfinal, cor='green')
    	else:
    		print ("NOPEE")


    def verificaBit(self, codigo, pos):
    	a = BitArray(int=codigo, length=32)
    	print(a.int)
    	#bit = a << (31 - pos)
    	#print (bin(bit))
    	bit = irshift(a, 31)
    	#print (bit)
    	return 5


    def rshift(self, val, n): 
    	return (val % 0x100000000) >> n


    def obtemCodigo(self, x, y, xmin, xmax, ymin, ymax):
    	codigo = 0
    	if (x < xmin):
    		print ("XMin", xmin)
    		codigo += 1
    	if (x > xmax):
    		print ("XMax", xmax)
    		codigo += 1
    	if (y < ymin):
    		print ("yMin", ymin)
    		codigo += 1
    	if (y > ymax):
    		print ("yMax", ymax)
    		codigo += 1
    	return codigo


    def Algoritmo_DDA (self, xi, yi, xf, yf, cor ):
        x = xi
        y = yi
        
        #self.w.create_oval(self.x1, self.y1, self.x2, self.y2)
        dx = xf - xi
        dy = yf - yi
        if (abs(dx) > abs(dy)):
            passos = abs(dx)
        else:
            passos = abs(dy)
        Xincr = dx/passos
        Yincr = dy/passos
        self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line", fill=cor)
        i = 0
        while(i < passos):
            x = x + Xincr
            y = y + Yincr
            self.w.create_text(round(x, 2), round(y, 2), text = ".", tag = "line", fill=cor)
            i = i + 1

"""



        

root1 = Tk()
root1.title("Rasterização, visualização em janela e preenchimento")

root2 = Tk()
root2.title("Transformações Geométricas 2D")

#root3 = Tk()
#root3.title("Operações em janela")


app = Application1(root1)
app1 = Application2(root2)
#app2 = Application3(root3)

root1.mainloop()
root2.mainloop()
#root3.mainloop()
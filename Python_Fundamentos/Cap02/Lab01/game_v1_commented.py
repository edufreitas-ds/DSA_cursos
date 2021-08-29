# Game Ping-Pong

from tkinter import *
import random
import time #importando bibliotecas necessárias para o game


level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n")) #variavel level que o jogador vai dar o input (escolher)
length = 500/level # ajustando tamanho de acordo com a escolha do jogador


root = Tk() # aparencia da janela
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()


count = 0
lost = False

class Bola: # Aparencia da Bola
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3] # Onde a bola inicia
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id) # definindo a area de movimento da bola

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]: # o que acontece se a bola acertar ou não acertar a barra
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra: # definições da barra
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color) # aparecencia e tamanho da barra
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left) # definindo movimento da barra
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event): # o que acontece ao mover a esquerda
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event): # o que acontece ao mover a direita
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event): # o que aparecer ao inciar o jogo
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count)) # texto score

def game_over():
    canvas.itemconfig(game, text="Game over!") # texto game over


Barra = Barra(canvas, "orange") # cor da barra
Bola = Bola(canvas, Barra, "purple") # cor da bola


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16)) # aparencia do score
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game) # combinar todos ao iniciar o game

root.mainloop() # fazer um loop com os processos descritos a cima

from tkinter import *
import random

fenetre = Tk()
def monter(event):
    global x,y,vitx,vity,pipex,pipey
    vity = -yvel*10

def jouer():

    global x,y,vitx,vity,pipex,pipey, cond, score, yvel
    vitx = vitx +0.003
    yvel +=  0.0003
    vity = vity + yvel
    pipex = pipex-vitx
    y = y+vity

    diff = random.randint(-1, 1)




    if pipex<=0:
        pipex = 450
        pipey = random.randint(-300, -100)

    if y >= 600 or y<=0:
        cond = False
    if pipey + 535 < y and pipex-67< x and pipex+5 > x:
        cond = False

    if pipey + 415 > y and pipex-67< x and pipex+5 > x:
        cond = False
    if pipex< x and pipex+vitx > x:
        score += 1
    print(yvel)
    dessin.coords(oiseau, x-20, y-20, x+20, y+20)
    dessin.coords(left_eye, x-10, y-5+diff, x-5, y+5+diff)
    dessin.coords(right_eye, x+10, y-5+diff, x+15, y+5+diff)
    dessin.coords(upper_pipe, pipex-50,pipey-5,pipex+5,pipey+400)
    dessin.coords(downer_pipe, pipex-50,pipey+ 555,pipex+5,pipey+950)
    dessin.itemconfig(score_text, text= str(score))

    if cond:
        fenetre.after(20,jouer)


def recommencer():
    global x,y,vitx,vity,pipex,pipey, cond, score, yvel

    yvel = 1
    x,y=200,300
    score = 0
    pipex, pipey = 450,  random.randint(-200, -100)
    vitx,vity = 10, 5
    cond = True
    diff = random.randint(-5, 5)


    dessin.coords(oiseau, x-20, y-20, x+20, y+20)
    dessin.coords(left_eye, x-10, y-5+diff, x-5, y+5+diff)
    dessin.coords(right_eye, x+10, y-5+diff, x+15, y+5+diff)
    dessin.coords(upper_pipe, pipex-50,pipey-5,pipex+5,pipey+400)
    dessin.coords(downer_pipe, pipex-50,pipey+ 555,pipex+5,pipey+950)
    dessin.itemconfig(score_text, text= str(score))


    jouer()

yvel = 1
x,y=175,300
score = 0
pipex, pipey = 450,  random.randint(-200, -100)
vitx,vity = 10, 5
cond = True



dessin = Canvas(fenetre,height=600,width=400,bg='lightblue')
dessin.bind('<Button-1>', monter)
#dessin.bind('<space>', monter)
dessin.pack(padx=5,pady=5)



oiseau = dessin.create_oval(x-5,y-5,x+5,y+5,width=1,fill='yellow')
left_eye = dessin.create_rectangle(x-5,y-5,x+5,y+5,width=1,fill='black')
right_eye = dessin.create_rectangle(x-5,y-5,x+5,y+5,width=1,fill='black')
upper_pipe = dessin.create_rectangle(pipex-50,pipey-5,pipex+5,pipey+400,width=1,fill='green')
downer_pipe = dessin.create_rectangle(pipex-50,pipey+ 555,pipex+5,pipey+950,width=1,fill='green')

score_text = dessin.create_text(200, 50, text= str(score), fill="black", font=('Helvetica 15 bold', 50))

jouer()


rejoue = Button(fenetre, text ="Rejouer" , command = recommencer)
rejoue.pack(padx = 5 , pady = 5)




quitte = Button (fenetre, text ="Quitter" , command = fenetre.destroy)


quitte.pack(padx = 5 , pady = 5)

fenetre.title("Flappy Bird")
fenetre.mainloop()

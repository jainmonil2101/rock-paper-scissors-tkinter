from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.resizable(False, False)
root.iconbitmap(r"game.ico")

rhp = PhotoImage(file="rock.png")
php = PhotoImage(file="paper.png")
shp = PhotoImage(file="scissor.png")

rphoto = PhotoImage(file="comp_rock.png")
pphoto = PhotoImage(file="comp_paper.png")
sphoto = PhotoImage(file="comp_scissor.png")

winphoto = PhotoImage(file="win.png")
losephoto = PhotoImage(file="lose.png")
tiephoto = PhotoImage(file="tie.png")

click = True

rockHandButton = ''
paperHandButton = ''
scissorHandButton = ''

def play():
    global rockHandButton, paperHandButton, scissorHandButton

    rockHandButton = Button(root, image = rhp, command= lambda: yourTurn('rock'))
    rockHandButton.grid(row=0, column=0)

    paperHandButton = Button(root, image = php, command= lambda: yourTurn('paper'))
    paperHandButton.grid(row=0, column=1)

    scissorHandButton = Button(root, image = shp, command= lambda: yourTurn('scissor'))
    scissorHandButton.grid(row=0, column=2)

def computerTurn():
    computerChoice = random.choice(["rock", "paper", "scissor"])
    return computerChoice
    

def yourTurn(yourChoice):
    global click
    comp = computerTurn()
    if click == True:
        if yourChoice == "rock":
            rockHandButton.configure(image = rhp)
            if comp == "rock":
                paperHandButton.configure(image=rhp)
                scissorHandButton.configure(image=tiephoto)
                click = False
            elif comp == "paper":
                paperHandButton.configure(image=php)
                scissorHandButton.configure(image=losephoto)
                click = False
            else:
                paperHandButton.configure(image=shp)
                scissorHandButton.configure(image=winphoto)
                click = False
        
        elif yourChoice == "paper":
            rockHandButton.configure(image = php)
            if comp == "rock":
                paperHandButton.configure(image=rhp)
                scissorHandButton.configure(image=winphoto)
                click = False
            elif comp == "paper":
                paperHandButton.configure(image=php)
                scissorHandButton.configure(image=tiephoto)
                click = False
            else:
                paperHandButton.configure(image=shp)
                scissorHandButton.configure(image=losephoto)
                click = False

        else:
            rockHandButton.configure(image = shp)
            if comp == "rock":
                paperHandButton.configure(image=rhp)
                scissorHandButton.configure(image=losephoto)
                click = False
            elif comp == "paper":
                paperHandButton.configure(image=php)
                scissorHandButton.configure(image=winphoto)
                click = False
            else:
                paperHandButton.configure(image=shp)
                scissorHandButton.configure(image=tiephoto)
                click = False

    else:
        if yourChoice == "rock" or yourChoice == "paper" or yourChoice == "scissor":
            rockHandButton.configure(image = rhp)
            paperHandButton.configure(image = php)
            scissorHandButton.configure(image = shp)
            click = True





play()

root.mainloop()
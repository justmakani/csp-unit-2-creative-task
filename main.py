from cmu_graphics import *
import random

Rect(0,0,400,400,fill='navy')

choices = ['rock','paper','scissors']
playerChoice = None
computerChoice = None
gameOver = False

textBg = Rect(20,300,360,80,fill='darkGray',border='white',borderWidth=1)
resultText = Label('Choose Rock, Paper, or Scissors!',200,340,size=16,fill='white',bold=True)

rockBtn = Rect(50,240,80,50,fill='gray',border='white',borderWidth=2)
paperBtn = Rect(160,240,80,50,fill='lightGray',border='white',borderWidth=2)
scissorsBtn = Rect(270,240,80,50,fill='lightBlue',border='white',borderWidth=2)

rockBtn.choice = 'rock'
paperBtn.choice = 'paper'
scissorsBtn.choice = 'scissors'

Label('Rock',rockBtn.centerX,rockBtn.centerY,fill='white')
Label('Paper',paperBtn.centerX,paperBtn.centerY,fill='black')
Label('Scissors',scissorsBtn.centerX,scissorsBtn.centerY,fill='black')

playerLabel = Label('You',100,80,fill='white',bold=True)
computerLabel = Label('Computer',300,80,fill='white',bold=True)

playerIcon = Rect(70,100,60,60,fill='black',border='white',borderWidth=2)
computerIcon = Rect(270,100,60,60,fill='black',border='white',borderWidth=2)

playerRect = Rect(playerIcon.left+10,playerIcon.top+10,40,40,fill=None)
computerRect = Rect(computerIcon.left+10,computerIcon.top+10,40,40,fill=None)

restartBtn = Rect(150,365,100,25,fill='black',border='white',borderWidth=2)
restartLabel = Label('Restart',restartBtn.centerX,restartBtn.centerY,fill='white',size=14)
restartBtn.visible = False
restartLabel.visible = False

colorMap = {'rock':'gray','paper':'lightGray','scissors':'lightBlue'}

def resetButtons():
    rockBtn.fill='gray'
    paperBtn.fill='lightGray'
    scissorsBtn.fill='lightBlue'

resetButtons()

def showResult():
    global computerChoice, gameOver, playerChoice
    computerChoice = random.choice(choices)
    playerRect.fill = colorMap[playerChoice]
    computerRect.fill = colorMap[computerChoice]

    if playerChoice == computerChoice:
        resultText.value = "Tie! Try again..."
        resultText.fill = 'white'
        playerChoice = None
        return 

    elif (playerChoice=='rock' and computerChoice=='scissors') or \
         (playerChoice=='paper' and computerChoice=='rock') or \
         (playerChoice=='scissors' and computerChoice=='paper'):
        resultText.value = f"You win! {playerChoice} beats {computerChoice}!"
        resultText.fill='lime'
        playerRect.fill = 'lime'
        computerRect.fill = 'tomato'
        restartBtn.visible=True
        restartLabel.visible=True
        gameOver=True
    else:
        resultText.value = f"You lose! {computerChoice} beats {playerChoice}!"
        resultText.fill='tomato'
        playerRect.fill = 'tomato'
        computerRect.fill = 'lime'
        restartBtn.visible=True
        restartLabel.visible=True
        gameOver=True
        playerChoice = None

def resetGame():
    global playerChoice, computerChoice, gameOver
    playerChoice=None
    computerChoice=None
    gameOver=False
    playerRect.fill=None
    computerRect.fill=None
    resultText.value='Choose Rock, Paper, or Scissors!'
    resultText.fill='white'
    restartBtn.visible=False
    restartLabel.visible=False
    resetButtons()

def onMousePress(x,y):
    global playerChoice
    if gameOver:
        return
    for btn in [rockBtn,paperBtn,scissorsBtn]:
        if btn.hits(x,y):
            btn.fill='yellow'
            playerChoice=btn.choice
            break

def onMouseRelease(x,y):
    clickPoint = Circle(x,y,1,visible=False)
    if restartBtn.hitsShape(clickPoint) and restartBtn.visible:
        resetGame()
        clickPoint.visible=False
        return
    if playerChoice:
        showResult()
    resetButtons()
    clickPoint.visible=False

def onMouseMove(x,y):
    for btn in [rockBtn,paperBtn,scissorsBtn]:
        btn.border='gold' if btn.hits(x,y) else 'white'

Label('Key:',50,20,fill='white',bold=True)
Rect(90,15,20,20,fill='gray')
Label('Rock',120,25,fill='white',size=12)
Rect(180,15,20,20,fill='lightGray')
Label('Paper',210,25,fill='black',size=12)
Rect(270,15,20,20,fill='lightBlue')
Label('Scissors',300,25,fill='black',size=12)

cmu_graphics.run()

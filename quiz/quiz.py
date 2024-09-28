import pgzrun

WIDTH=1000
HEIGHT=500



score=0

timeleft=10

g_over=False

question_box=Rect(0,0,700,100)
question_box.move_ip(20,50)

ans1=Rect(0,0,300,100)
ans1.move_ip(20,200)

ans2=Rect(0,0,300,100)
ans2.move_ip(20,350)

ans3=Rect(0,0,300,100)
ans3.move_ip(400,200)

ans4=Rect(0,0,300,100)
ans4.move_ip(400,350)

answerboxes=[ans1,ans2,ans3,ans4]

timer=Rect(0,0,100,100)
timer.move_ip(800,50)

skip=Rect(0,0,100,250)
skip.move_ip(800,200)

questioncount=0
questions=[]
questionindex=0

def draw():
    screen.fill('blue')
    screen.draw.filled_rect(question_box,'black')
    screen.draw.filled_rect(ans1,'white')
    screen.draw.filled_rect(ans2,'white')
    screen.draw.filled_rect(ans3,'white')
    screen.draw.filled_rect(ans4,'white')
    screen.draw.filled_rect(timer,'black')
    screen.draw.filled_rect(skip,'yellow')
    screen.draw.textbox(question[0],question_box,color='white')
    screen.draw.textbox('SKIP',skip,color='black',angle=-90)
    screen.draw.textbox(str(timeleft),timer,color='white')
    index=1
    for box in answerboxes:
        screen.draw.textbox(question[index],box,color='black')
        index=index+1

def readquestionfile():
    global questioncount,questions
    file=open('questions.txt','r')
    for i in file:
        questions.append(i)
        questioncount=questioncount+1
    file.close()

readquestionfile()
print(questions)

def readnextquestion():
    global questionindex
    questionindex=questionindex+1
    return questions.pop(0).split(',')

def correctanswer():
    global question
    if questions:
        question=readnextquestion()


def on_mouse_down(pos):
    i=1
    for box in answerboxes:
        if box.collidepoint(pos):
            if i is int(question[5]):
                correctanswer()
            else:
                gameover()
    i=i+1        
            
def gameover():
    global question
    question=['GAME over','-','-','-','-',5]


question=readnextquestion()
print(question)
print(question[0])

def update():
    pass

pgzrun.go()

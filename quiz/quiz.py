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


def update():
    pass

pgzrun.go()
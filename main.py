from processing import *

def setup():
    size(800,800)

angle= 90
def draw():
    global angle
    background(0)
    translate(width/2, height/2)
    stroke(100,50, 255)
    strokeWeight(3)
    for i in reversed(renge(0,300,10)):
        pushMatrix()
        rotate(cos(radians(angle+i)))
        ellipse(200*sin(radians(angle)),0,i,i)
        popMatrix()
    angle=angle+1
run()
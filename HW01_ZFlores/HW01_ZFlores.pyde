def setup():
    size(800,800);
    colorMode(HSB,height,width,height);
    background(600)

def draw():
    fill(mouseX,mouseY,height)
    stroke(mouseX,mouseY,height)
    
def mouseDragged():
    ellipse(mouseX,mouseY,random(100),random(100))

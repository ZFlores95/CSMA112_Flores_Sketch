add_library('sound')

import time
import microphone

history = []
lifespan = 3000

def setup():
    size(500, 500)
    frameRate(20)
    colorMode(RGB, height, width, 255, 100)
    microphone.initialize(this, AudioIn, Amplitude)
    noStroke()

def draw():
    background(0)
    sound_level = microphone.get_level() *10
    agent = Agent()
    agent.move_to(mouseX, mouseY)
    history.append(agent)
    if len(history) > 500:
        history.pop(0)
    for agent in history:
        
        r, g, b =  agent.x, agent.y, 0
        radius = width * sound_level
        fade_factor = agent.get_age() / float(agent.lifespan)
        a = 100 - fade_factor * 100
    
    
        fill(r, g, b, a)
    
        circle(agent.x, agent.y, radius)
    
def now():
    return int(time.time() * 1000)

class Agent(object):
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.lifespan = 3000
        self.birthday = now()
        #self.radius = 20
        
    def move_to(self, x ,y):
        self.x = x
        self.y = y
    
    def get_age(self):
        return now() - self.birthday

my_agent = Agent()
print(my_agent.get_age())

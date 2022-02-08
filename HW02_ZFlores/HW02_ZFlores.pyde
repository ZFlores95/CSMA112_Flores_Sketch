add_library('sound')

import model 
import microphone

def setup():
    size(model.x_dim, model.y_dim)
    colorMode(model.color_mode, height, width, height)
    microphone.initialize(this, AudioIn, Amplitude)

def draw():
    global startX, startY, radiusX, radiusY
    sound_level = microphone.get_level() * 2
    
    model.agent_x = sound_level * width
    model.agent_y = mouseY
    
    radiusX = map(model.agent_x, 0, width, 100, 10)
    radiusY = map(model.agent_y, 0, height, 100, 10)
    
    fill(mouseX,mouseY,height)
    background(model.bg_color)
    ellipse(model.agent_x, model.agent_y, radiusX, radiusY)

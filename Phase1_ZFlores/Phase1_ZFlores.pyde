# Zully Flores
# 2.24.22
# A program to generate a series of random agents from a main agent's location.

add_library('sound')    # Loads sound library into sketch

from agent import Agent # Import Agent class from agent module

import microphone       # Import microphone module

agents = [] # Creates an empty list call agents
fps = 20    # Variable for Frames per Seconds set to equal 20
ppf = 5     # Variable for Pixels per Frame set to equal 5

def setup():
    size(800, 800) # Set the size of the canvas
    frameRate(fps) # Set the sketch animation frame rate
    
    colorMode(RGB, height, width, 255, 100) # Sets color mode to RGB.
                                            # Range for the red is set to the height of canvas. Range for the green is set to the width of canvas. 
                                            # Range for the blue is set to 255. Range for the alpha is set to 100.
    
    microphone.initialize(this, AudioIn, Amplitude)  # Calls the microphone module's initialize function
    
    noStroke()     # Disables drawing the stroke

def draw():
    background(0)  # Set the background color
    
    sound_level = microphone.get_level() *1  # Variable for sound level set to equal microphone module's get_level() function multiplied by one
    
    agent = Agent()               # Creates an agent
    agent.move_to(mouseX, mouseY) # Calls the agent module's move_to() function
    
    circle(agent.x, agent.y, 25) # Draws Cirlce at agents x & y position. Shape size set to 25
    
    agents.append(agent) # Add agent to the end of the list
    
    for agent in agents: # For every agent in the list of agents Run the following
        r, g, b =  agent.x, agent.y, random(255) # Variables for r(red), g(green), and b(blue) set to equal agent.x, agent.y, and random(255)
        
        radius = width * sound_level             # Variable for radius set to equal width multiplied by sound_level
        
        fade_factor = agent.get_age() / float(agent.lifespan) # Variable for fade_factor set to equal agent module's get_age() function divided by 
                                                              # agent module's lifespan float value
                                                              
        a = 100 - fade_factor * 100         # Variable for Alpha set to equal 100 minus fade factor times 100
        
        agent.move(ppf)                     # Moves an agent by an Increment
        agent.check_boundary(width, height) # Checks agents boundary
        
        # Render
        fill(r, g, b, a)                 # Sets the color used to fill shapes
        circle(agent.x, agent.y, radius) # Draws Cirlce at agents x & y position. Shape size set to radius value
    
    

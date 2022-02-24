import time

class Agent(object):
    
    global now
    
    def __init__(self):
        self.x = 0            # default x position
        self.y = 0            # default y position
        self.lifespan = 8000  # Variable for lifespan set to equal 8000
        self.birthday = now() # Variable for birthday set to equal now() function
        self.direction = [random(-1, 1), random(-1, 1)] # Direction Vector. Random unit 0 or 1 in x and Random unit 0 or 1 in y
        self.history = [] # Creates an empty list call History
        self.history_max = 500 # The max number of items in the list
    
    def now(): # Now Function
        return int(time.time() * 1000)
        
    def get_age(self): # Get Age Function
        return now() - self.birthday # Calculates age by subtracting birthday from now() then returns the value
        
    def check_boundary(self, w, h): # Boundary Function
        if self.x >= width or self.x <= 0: # If x is greater or equal to width or x is less than or equal to 0, reverse x direction.
            self.reverse_x()
        if self.y >= height or self.y <= 0: # If y is greater or equal to height or y is less than or equal to 0, reverse y direction.
            self.reverse_y()
        
    def reverse_x(self): # Reverse direction in x Function
        self.direction[0] *= -1 # Multiply x component by -1
    
    def reverse_y(self): # Reverse direction in y Function
        self.direction[1] *= -1 # Multiply y component by -1
        
    def move(self, amount): # Move Function
        dx = amount * self.direction[0] # Movement Vector in x-axis. Amount times x component of the agents direction.
        dy = amount * self.direction[1] # Movement Vector in y-axis. Amount times y component of the agents direction.
        self.move_to(self.x + dx, self.y + dy) # Move x & y by a certain amount
    
    def move_to(self, x, y): # Move to Function
        if self.x == x and self.y == y: return # A guard. If self.x equals x and self.y equals y, then return
        self.x = x # self x equal new x position
        self.y = y # self y equal new y position

        self.history.append((self.x, self.y)) # Add current location to the History
        if len(self.history) > self.history_max: # If the length of the history list is greater than the max number of items in the list, remove first item.
            self.history.pop(0)

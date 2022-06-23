
import pygame

WIDTH, HEIGHT = 1400, 900
# creating the display surface
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD simulator")

FPS = 180




# the coordinates are 0, 0 at left upper corner, and get bigger right and down
# And i think that the specified position of a surface will be the position of it's left top corner.

# In pygame, everything that can be drawn is a surface.
# pygame.display is the starting surface.
# It is created by pygame.display.set_mode((WIDTH, HEIGHT)) and you assign it to a constant - this makes the window and thus the display surface appear.
# And then you can create new surfaes that you simply hold bound to your variables (and they have their .x and .y properties, which are used for collision detection and
# also so you can use them when drawing onto the screen and maybe other functions as well)
# And then you can draw the surfaces onto eachother, and in the same way draw the surface to the display (since it is itself a surface).


# Creating surfaces:
# pygame.Rect(xPosition, yPosition, xSize, ySize)    creates a rectangle surface
# pygame.image.load("./pathToImageFromWhereWeRead")    # makes a surface from an image  
# # #import os   # os.path.join("Mapa1", "Slika.jpg")    # makes it work for all os-es, by taking the current directory and adding all the written directories into the string and using the correct delimiter ( / or \ )
# pygame.image.load(os.path.join("Mapa1", "Slika.jpg"))



#Manipulating surfaces:
# surface.x   and    surface.y   are the surface's positions
# pygame.transform.scale(surface, (xSize, ySize))   #returns the surface scaled to the passed size
# pygame.transform.rotate(surface, angle)  # returns rotated surface, try out the direction of the angle to see how it works
# surface.get_width()    # returns the width



# Centering
# surface.get_width()//2    # You can use this to find the center and then calculate from there.
# This uses floor division. I think that decimals cause a problem with positions.




# Drawing onto surfaces:

# Surfaces can have other surfaces drawn onto them.
# surface1.blit(surface2, (xPosition, yPosition))     draws a surface on a surface - basically replaces the current pixels at those positions with the new ones
# surface.fill((R, G, B))    draws on the surface by changing all pixels to this color
# pygame.draw.rect(WIN, (color), rectangularSurfacePreviouslyCreated)   #takes the rectangular surface with its xPosition, yPos, xSize, ySize and draws it


# WIN.blit(surface, (xPosition, yPosition))   #draws the surface onto the window 

# .update simply shows, what has so far been drawn on the window. It's not drawing anything, just showing the change to the user.

# Surfaces can have a subsurface added to them, but this isn't used as much.
# look up .subsurface for this.






# Collisions:
# rectangle1.coliderect(rectangle2)   # returns true, if the rectangles are colliding at the moment. Only works for rectangles





# Events:
# (this uses pygames event handler)

#pressed_keys = pygame.key.get_presseed()    #gives you a boolean map, that maps all possible keys to false (not pressed at the moment) or true (pressed at the moment)
# pygame.K_a    # this is how the key a is represented in the map

# event.type == pygame.KEYDOWN    returns true, if any key has been pressed down (so we can put all the other pygame.K_something in an if and don't check all of them, if none has been pressed)
# event.key == pygame.K_a    retrns true, if the key (in this case a) has been pressed down. But doesn't remain true, while the key is down.

#creating events:
# YELLOW_HIT = pygame.USEREVENT + 1    # creates an event with this number* and assigns it to be called later. You set it at the top of the program as a constant.
# pygame.event.post(pygame.event.Event(YELLOW_HIT))    # saying there is an event that happened - it puts it into the array "events"
#    * - this is simply a number. I think that pygame.USEREVENT is the last number that pygame itself uses. Then you can assign pygame.USEREVENT + 1, pygame.USEREVENT + 2, ...
#  So I would create events at the top of the code like this:
#  event_counter = pygame.USEREVENT + 1
#  EVENT_NAME_ONE = event_counter++
#  EVENT_NAME_TWO = event_counter++
# ...  





# Fonts:

# pygame.font.init()    # initializes the font library - do it at the top

# SOMETHING_FONT = pygame.font.SysFont('comicsans', sizeOfFont)      # makes this font usable
# draw_text = SOMETHING_FONT.render("Whatever string", True, (color)))     # creates a surface with this text    # the True is for anti-aliasing, which means making lines look smooth by blurring their edge pixels




# Sound effects:
# pygame.mixer.init()   # at the top of the text
# SOMETHING_SOUND = pygame.mixer.Sound(os.path.join("Zvoki", "zvok.mp3"))    # loads the sound
# SOMETHING_SOUND.play()   # plays the sound


# Freezing the game:
# pygame.time.delay(num_of_miliseconds)   # freezes for num_of_miliseconds. This is useful for displaying any sort of announcement text.

# Restarting the game:
# Simply call the main function again. This adds a new function main to the stack and you just continue there.
# Right after the call put pygame.quit(), so that when you return from the restarted game(s), it immediately quits the current game (except if you want it to continue)











import os
import math
import random



DVD_START_POS = [100, 100]
DVD_WIDTH = 200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CORNER_MARGIN = 5

VELOCITY_SIZE = 250 / FPS

INIT_ANGLE = random.gauss(0, math.pi/2)
print(INIT_ANGLE)

START_VELOCITY = [VELOCITY_SIZE * math.cos(INIT_ANGLE), VELOCITY_SIZE * math.sin(INIT_ANGLE)]

KEY_VELOCITY_CHANGE_PER_SECOND = [2 / FPS, 2 / FPS]    # x and y direction

VELOCITY_UPPER_BOUND = [700 / FPS, 700 /FPS] # largest absolute value allowed in the x and y directions
# VELOCITY_LOWER_BOUND = [75 / FPS, 75 / FPS]    # smallest -||-
VELOCITY_LOWER_BOUND = [0 / FPS, 0 / FPS]    # smallest -||-



DVD_RAW = pygame.image.load(os.path.join("Slike", "dvd.jpg"))
DVD = pygame.transform.scale(DVD_RAW, (DVD_WIDTH, ((DVD_WIDTH / DVD_RAW.get_width()) * DVD_RAW.get_height())))






def draw_frame(DVD_POS):
    #here we put whatever we want to blit to the window before ve update
    WIN.fill(BLACK)
    WIN.blit(DVD, (DVD_POS[0], DVD_POS[1]))
    # updating the whole display surface - simply shows in the window what display looks like at the moment (what are it's pixels currently)
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True

    DVD_POS = DVD_START_POS
    velocity = START_VELOCITY

    while run:
        clock.tick(FPS)     # Returns how many seconds have passed since the last clock.tick call.
                            # If you pass a number (FPS) to it, it will return only if 1000/FPS miliseconds have passed since the last call 
                            # For some reason FPS needs to be an integer.

        DVD_POS[0] += velocity[0]
        DVD_POS[1] += velocity[1]

        # changing velocity with keys with upper bounding

        # x direction

        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[pygame.K_RIGHT] and velocity[0] < VELOCITY_UPPER_BOUND[0]):
            velocity[0] += (KEY_VELOCITY_CHANGE_PER_SECOND[0])
            
        if pressed_keys[pygame.K_LEFT] and velocity[0] > -VELOCITY_UPPER_BOUND[0]:
            velocity[0] -= (KEY_VELOCITY_CHANGE_PER_SECOND[0])

        # y direction

        if pressed_keys[pygame.K_DOWN] and velocity[1] < VELOCITY_UPPER_BOUND[1]:
            velocity[1] += (KEY_VELOCITY_CHANGE_PER_SECOND[1])
        
        if pressed_keys[pygame.K_UP] and velocity[1]< VELOCITY_UPPER_BOUND[1]:
            velocity[1] -= (KEY_VELOCITY_CHANGE_PER_SECOND[1])




        # velocity lower bounding
        if velocity[0] > 0 and velocity[0] < VELOCITY_LOWER_BOUND[0]:
            velocity[0] = VELOCITY_LOWER_BOUND[0]

        if velocity[0] < 0 and velocity[0]> -VELOCITY_LOWER_BOUND[0]:
            velocity[0] = -VELOCITY_LOWER_BOUND[0]

        if velocity[1] > 0 and velocity[1] < VELOCITY_LOWER_BOUND[1]:
            velocity[1] = VELOCITY_LOWER_BOUND[1]
        
        if velocity[1] < 0 and velocity[1] > -VELOCITY_LOWER_BOUND[1]:
            velocity[1] = -VELOCITY_LOWER_BOUND[1]
        




        # wall collision detection and bounce and correction of overlap in the collision

        if(DVD_POS[0] + DVD.get_width() >= WIDTH):
            DVD_POS[0] = WIDTH - DVD.get_width()
            velocity[0] = -abs(velocity[0])
        
        if(DVD_POS[0] <= 0):
            DVD_POS[0] = 0
            velocity[0] = abs(velocity[0])

        if(DVD_POS[1] <= 0):
            DVD_POS[1] = 0
            velocity[1] = abs(velocity[1])
        
        if(DVD_POS[1] + DVD.get_height() >= HEIGHT):
            DVD_POS[1] = HEIGHT - DVD.get_height()
            velocity[1] = -abs(velocity[1])


        
        
        # corner checking
        is_in_corner = (abs(DVD_POS[0]) <= CORNER_MARGIN or abs(DVD_POS[0] + DVD.get_width() - WIDTH) <= CORNER_MARGIN) and (abs(DVD_POS[1]) <= CORNER_MARGIN or abs( DVD_POS[1] + DVD.get_height() - HEIGHT) <= CORNER_MARGIN)
        if(is_in_corner):
            WIN.blit(pygame.transform.scale(pygame.image.load(os.path.join("Slike", "trophy.jpg")), (WIDTH/2, HEIGHT/2)), (WIDTH/4, HEIGHT/4))
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.quit()
            









        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            

            

        draw_frame(DVD_POS)
        
        
    
    pygame.quit()


main()
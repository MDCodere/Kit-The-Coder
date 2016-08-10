"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED, CYAN]

def random_color():
    return random.choice(colors)
    
#enemey = pygame.sprite.Group()

#enemey.add('man.png')
    
# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("CityScroller")

done = False

clock = pygame.time.Clock()

class Mouse(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, width, height, speed):
        super().__init__()
		
        # Loading the sprite from the file
        
        self.image = pygame.image.load('bullet.png')
		
		# This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)
		
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
        self.width  = width
        self.height = height
        self.speed = speed
		
    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = (400)
            self.rect.x = (300)
		
		

		

   
        image = pygame.image.load('bullet.png').convert()
        #print(image)
        image.set_colorkey(CYAN)
        screen.blit(image,[self.rect.x, self.rect.y]) 

        
        
    def moveRight(self, speed):
        self.rect.x += speed
        if self.rect.x > 900:
            self.rect.y = (400)
            self.rect.x = (300)
            
            

            

class Enemey(pygame.sprite.Sprite):
    def __init__(self, x_position , y_position, width, height, speed):
        super().__init__()
		
		# Loading the sprite from the file
        
        self.image = pygame.image.load('man.jpg')

        # This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
        self.width  = width
        self.height = height
        self.speed = speed
        self.man = []


    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = (390)
            self.rect.x = (-5)
		

        
        
        
    
        image = pygame.image.load('man.jpg').convert()
        #print(image)
        image.set_colorkey(CYAN)
        screen.blit(image,[self.rect.x, self.rect.y])    
        
    def move_man(self):
        self.rect.x -= 3
        if self.rect.x < 0: 
            self.rect.y = 500
        
            
      

class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_point -= speed
        
class Characters(pygame.sprite.Sprite):
    def __init__(self, x_point, y_point, width, height, speed): 
        super().__init__()
		
	
        # Loading the sprite from the file
        
        self.image = pygame.image.load('layla.png')


        # This sets the background of the image.
        # Setting it to white makes it so that it blends in the rest of screen
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x_point
        self.rect.y = y_point
        self.width  = width
        self.height = height
        self.speed = speed
        self.layla = []


    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = (390)
            self.rect.x = (-5)
		
		
        
        
        
   
        image = pygame.image.load('layla.png').convert()
        #print(image)
        image.set_colorkey(CYAN)
        screen.blit(image, [self.rect.x, self.rect.y])
        
    def moveRight(self, speed):
         #print(self.rect.x, self.rect.y)
         self.rect.x += speed
         print("moveRight", self.rect.x, self.rect.y)
         if self.rect.x > SCREEN_WIDTH:
            self.rect.y = (390)
            self.rect.x = (-5)
        
    def moveLeft(self, speed):
        self.rect.x -= speed
        print("moveLeft", self.rect.x, self.rect.y)
        if self.rect.x < 0:
            self.rect.y = (390)
            self.rect.x = (-5)
        
    def Jump(self, y_point, speed):
        self.y_point -= speed
   

    def moveBackward(self, y_point, speed):
        self.y_point += speed
       
        
        
class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        self.add_buildings() # Add builings each time a new instance is created

    def add_buildings(self):
        """
        Will add a randomly generated building that fits within the width and height
        of the scroller
        """
        current_width = 0 # How wide the scroller is right now
        while current_width <= self.width:
            self.add_building(current_width)
            current_width += self.buildings[-1].width
            self.scroll_end = current_width

    def add_building(self, x_location):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        # The building width will be a random integer between 1/20th and 1/4th of the width
        building_width = random.randint((self.width // 20), (self.width // 4))

        max_height = self.base - self.height # this sets the maximum height each building can be

        # The building width will be a random integer between 1/4th and just under the max_height
        building_height = random.randint((max_height // 4), (max_height - 1))

        y_location = self.base - building_height # This tells the building where along the y-axis to draw itself

        self.buildings.append(Building(x_location, y_location, building_width, building_height, self.color))


    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        for building in self.buildings:
            building.draw()
            

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        for building in self.buildings:
            building.move(self.speed)
            if building.x_point + building.width <= 0:
                self.buildings.remove(building)
    
                

        #gets the x_point of the last building and adds it's width to place the new building right next to it.
        new_building_location = self.buildings[-1].x_point + self.buildings[-1].width
        if new_building_location <= self.width:
            self.add_building(new_building_location)

            
CYAN = (0, 255, 255)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (0, 255, 255)


layla = Characters(-5, 370, 50, 75, 8)
man = Enemey(775, 250, 50, 75, 1)
bullet = Mouse(-50, 450, 25, 30, 5)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

bullet_list = []

sprite_list = []


characters_list = pygame.sprite.Group()
enemey_list = pygame.sprite.Group()
#enemey_list1 = pygame.sprite.Group()
mouse_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group() 
characters_list.add(layla)
enemey_list.add(man)
#enemey_list1.add(man)
mouse_list.add(bullet)
all_sprites_list.add(layla)
all_sprites_list.add(man)
all_sprites_list.add(bullet)


#for x in range(5):
    #characters_list.add(Characters(random.randint(400, 750), random.randint(300, 550), 50, 75, 3))


for x in range(5):
    enemey_list.add(Enemey(random.randint(400, 750), random.randint(300, 550), 50, 75, 3))

#for x in range(20):
#mouse_list.add(Mouse(-50, 465, 50, 75, 8))
#font = pygame.font.Font(None, 36)
#game_over = False



 # --- Main event loop
while not done:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            game_over = True 
                    
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_LEFT]:
            layla.moveLeft(40)
            print(layla.rect.x, layla.rect.y)
        if keys[pygame.K_RIGHT]:
            layla.moveRight(40)
        if keys[pygame.K_UP]:
            bullet.moveRight(25)
        if keys[pygame.K_DOWN]:
            speed = 5
            speed -= 0.05
        #if keys[pygame.K_UP]:
        #speed = 5
        #speed += 0.05
        #if keys[pygame.K_DOWN]:
        #speed = 5
        #speed -= 0.05
        
        #if pygame.sprite.collide_move(layla, man):
            #self.move_layla = self.x_point    
            #self.move.layla = self.y_point
            #print("GAME OVER!")
        
        #if pygame.sprite.spritecollideany(layla, man):
        #layla.kill()
        #for x in range(-1):
        #enemey_list.add(Enemey(random.randint(400, 750), random.randint(300, 550), 50, 75, 3))
        
        
                
            
        # --- Game logic should go here

        # --- Screen-clearing code goes here
    

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
    screen.fill(BACKGROUND_COLOR)
    
            
            
        # --- Drawing code should go here
    #if game_over:
    #text = font.render("GAME OVER", True, BLACK)
    #text_rect = text.get_rect()
    #text_x = SCREEN_WIDTH() / 2 - SCREEN_HEIGHT / 2
    #text_y = SCREEN_WIDTH() / 2 - SCREEN_HEIGHT / 2
    #screen.blit(text, [text_x, text_y])        
    
    

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    #man.update()
    #man.add_man()
    #bullet.update()
    #layla.update()
    # See if the player block has collided with anything.
    character_hit_list = pygame.sprite.spritecollide(man, characters_list, True)
    #enemey_hit_list1 = pygame.sprite.spritecollide(layla, enemey_list1, True)
    enemey_hit_list = pygame.sprite.spritecollide(bullet, enemey_list, True)
    mouse_hit_list = pygame.sprite.spritecollide(man, mouse_list, True)
    #characters_list.update()
    enemey_list.update()
    #mouse_list.update()
    
    
    all_sprites_list.draw(screen)
    #for sprite in sprite_list:
    #sprite.add_man()
    #sprite.move_man()
    
    #for bullet in bullet_list:
    #sprite.add_bullet()
    #sprite.moveRight()

        # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

        # --- Limit to 60 frames per second
    clock.tick(60)        


# Close the window and quit
pygame.quit()
exit() # Needed when using IDLE
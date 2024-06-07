import pygame
from sys import exit 

pygame.init()    #initialize  pygame
screen = pygame.display.set_mode((1200,600))   # create a display surface
clock = pygame.time.Clock() #limit the frame

# text 
title_font = pygame.font.Font(None, 45)
pygame.display.set_caption("MADE THIS AT 4AM")    
pygame.display.set_caption("Hope you enjoy this game :)")
title_surf = title_font.render('MADE THIS AT 4AM', False, 'white')
credit_surf = title_font.render('Hope you enjoy this game :)', False, 'white')
title_rect = title_surf.get_rect(midtop = (600,200))
credit_rect = title_surf.get_rect(midtop = (550,500))


#variables used later in the game
tile_size = 30
game_over1 = 0
game_over2 = 0
menu = 0
collide_list1 = []
collide_list2 = []
score_1 = 0
score_2 = 0

#image of background and buttons
scaled_sky_img = pygame.transform.scale(pygame.image.load('background/sky.png'), (1200,600))
restart_img = pygame.transform.scale(pygame.image.load('background/restart.png').convert_alpha(),(80,40))
start_img = pygame.transform.scale(pygame.image.load('background/start.png').convert_alpha(),(80,40))





text_font = pygame.font.SysFont('Bauhaus 93', 70)
score_font = pygame.font.SysFont('Bauhaus 93', 30)
color = (255, 255, 255)
#function to draw text in the game
def draw_text(text, font, text_col, x , y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y ))


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()     
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def display(self):
        click = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                click = True
        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        screen.blit(self.image, self.rect)
        return click


        
       
        

class World():
    def __init__(self,data):
        self.reset(data)

    def reset(self, data):
        self.tile_list = []

        tile1_surf = pygame.image.load('tile/tile1.png').convert_alpha()
        

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    scaled_tile_surf = pygame.transform.scale(tile1_surf, (tile_size, tile_size))
                    tile_rect = scaled_tile_surf.get_rect()
                    tile_rect.x = col_count * tile_size
                    tile_rect.y = row_count * tile_size
                    tile = (scaled_tile_surf, tile_rect )
                    self.tile_list.append(tile)
                if tile == 2:
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                if tile == 3:
                    snow = Snow(col_count * tile_size, row_count * tile_size)
                    snow_group.add(snow)
                if tile == 4:
                    red_gem = Red_gem(col_count * tile_size, row_count * tile_size)
                    redgem_group.add(red_gem)
                if tile == 5:
                    blue_gem = Blue_gem(col_count * tile_size, row_count * tile_size)
                    bluegem_group.add(blue_gem)
                if tile == 6:
                    fly = Enemy(col_count * tile_size, row_count * tile_size - 5)
                    fly_group.add(fly)
                if tile == 7:
                    gate = Gate(col_count * tile_size, row_count * tile_size - 15)
                    gate_group.add(gate)

                col_count += 1    #increase the counter when it finishes one tile in one row
            row_count += 1        #increase the row counter when it iterates through one row

    def display(self):
        for item in self.tile_list:
            screen.blit(item[0],item[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy/fly.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 2
        self.move_counter = 0

    def update(self):
       self.rect.x -= self.direction
       self.move_counter += 1 
       if abs(self.move_counter) > 100:
           self.image = pygame.transform.flip(self.image, True,False)
           self.direction *= -1
           self.move_counter *= -1

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        fire_image = pygame.image.load('tile/fire.png').convert_alpha()
        self.image = pygame.transform.scale(fire_image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top
        self.bottom = self.rect.bottom

class Snow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        snow_image = pygame.image.load('tile/snow.png').convert_alpha()
        self.image = pygame.transform.scale(snow_image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top
        self.bottom = self.rect.bottom

class Blue_gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        gem_image = pygame.image.load('item/gemBlue.png').convert_alpha()
        self.image = pygame.transform.scale(gem_image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top

class Red_gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        gem_image = pygame.image.load('item/gemRed.png').convert_alpha()
        self.image = pygame.transform.scale(gem_image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.top = self.rect.top

class Gate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        gate_image = pygame.image.load('background/gate.png').convert_alpha()
        self.image = pygame.transform.scale(gate_image,(tile_size, 45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        



#player1
class Player1():
    def __init__(self,x,y):
        self.reset(x,y)
        

    def update(self,game_over1):
        dx = 0
        dy = 0

        if game_over1 == 0 and game_over2 == 0:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w] and self.jumped == False and self.in_air == False:
                self.vel_y = -13
                self.jumped = True
            if key_pressed[pygame.K_w] == False:
                self.jumped = False
            if key_pressed[pygame.K_a]:
                dx -= 4  
                self.counter += 1  
                #only when pressing the left direction key the iteration counter incresases 
                self.direction = -1 #change the directoin to -1 which represents left
            if key_pressed[pygame.K_d]:
                dx += 4 
                self.counter += 1 
                self.direction = 1
            if key_pressed[pygame.K_a] == False and key_pressed[pygame.K_d] == False:
                self.counter = 0
                self.index = 0 
            #if both direction keys are not presssed, set the iteeration counter and direction back to 0
                if self.direction == 1:
                    self.player1 = self.player1_right[self.index] 
                if self.direction == -1:
                    self.player1 = self.player1_left[self.index]

            #walking animation
            if self.counter >= 5: 
                # when the right/left direction key is pressed, every 5 iteration it updates the walking image
                self.counter = 0
                self.index += 1   # access the next image in the list
                if self.index >= 3:
                    self.index = 0  
                    # make sure it doesn't go beyond the range of the list
                if self.direction == 1: # the player is walkting towards right
                    self.player1 = self.player1_right[self.index] # access the player_right list
                if self.direction == -1:
                    self.player1 = self.player1_left[self.index]

            #gravity
            self.vel_y += 1
            if self.vel_y >= 10: self.vel_y = 10
            dy += self.vel_y

            #check for collision with tiles
            self.in_air = True
            for tile in world.tile_list:  #access each tuple in the tile_list
                #check for collision in x direction
                if tile[1].colliderect( self.rect.x + dx, self.rect.y, self.player1_width, self.player1_height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect( self.rect.x, self.rect.y + dy, self.player1_width, self.player1_height):
                    # check if below the tile (jumping)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the tile (falling)
                    elif self.vel_y > 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #check for collision with enemies/snow/lava
            if pygame.sprite.spritecollide(self, fly_group, False):
                game_over1 = 1
            if pygame.sprite.spritecollide(self, snow_group, False):
                game_over1 = 1
            

            for lava in lava_group:
                if lava.rect.colliderect( self.rect.x, self.rect.y + dy, self.player1_width, self.player1_height):
                    if self.vel_y < 0:
                        dy = lava.bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y > 0:
                        dy = lava.top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False 
                
                        
           

            #update player coordinates
            if self.rect.x + dx < 0 or self.rect.right + dx >= 1200:
                dx = 0
            self.rect.x += dx
            self.rect.y += dy
            
        elif game_over1 == 1:
            self.player1 = self.dead_image
            draw_text('GAME OVER...', text_font, color, 400, 250)
            self.rect.y -= 5

        screen.blit(self.player1, self.rect)

        return game_over1
    
    def update1(self,collide_list1):
        if pygame.sprite.spritecollide(self, gate_group, False):
                if 1 not in collide_list1:  # Add player 1 to the list if not already present
                    collide_list1.append(1)
        else:
                if 1 in collide_list1:
                    collide_list1.remove(1)
        return collide_list1
    
    def reset(self,x,y):
        self.player1_right = [] 
        self.player1_left = []  
        self.index = 0 
        self.counter = 0  
        self.direction = 0
        for i in range (1,4):  
            player1_surf = pygame.image.load(f'player/pink{i}.png').convert_alpha() 
            player1_surf = pygame.transform.scale(player1_surf,(25,40))
            player1_surf_left = pygame.transform.flip(player1_surf, True,False) 
            self.player1_right.append(player1_surf) 
            self.player1_left.append(player1_surf_left)  
        self.dead_image = pygame.transform.scale(pygame.image.load('player/dead.png'),(25,40))
        self.player1 = self.player1_right[self.index] 
        self.rect = self.player1.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player1_width = self.player1.get_width()   
        self.player1_height = self.player1.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True




#player2
class Player2():
    def __init__(self,x,y):
        self.reset(x,y)

    def update(self,game_over2):
        dx = 0
        dy = 0

        if game_over2 == 0 and game_over1 == 0:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_UP] and self.jumped == False and self.in_air == False:
                self.vel_y = -13
                self.jumped = True
            if key_pressed[pygame.K_UP] == False:
                self.jumped = False
            if key_pressed[pygame.K_LEFT]:
                dx -= 4  
                self.counter += 1  #only pressing the left key the counter incresases 
                self.direction = -1
            if key_pressed[pygame.K_RIGHT]:
                dx += 4 
                self.counter += 1 #only pressing the right key the counter incresases 
                self.direction = 1
            if key_pressed[pygame.K_LEFT] == False and key_pressed[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.player2 = self.player2_right[self.index]
                if self.direction == -1:
                    self.player2 = self.player2_left[self.index]

            #walking animation
            if self.counter >= 5: # every 5 iteration it updates the walking image
                self.counter = 0
                self.index += 1
                if self.index >= 3:
                    self.index = 0
                if self.direction == 1:
                    self.player2 = self.player2_right[self.index]
                if self.direction == -1:
                    self.player2 = self.player2_left[self.index]
            #gravity
            self.vel_y += 1
            if self.vel_y >= 10: self.vel_y = 10
            dy += self.vel_y
            
            #check for collision
            self.in_air = True
            for tile in world.tile_list:  #access each tuple in the tile_list
                #check for collision in x direction
                if tile[1].colliderect( self.rect.x + dx, self.rect.y, self.player2_width, self.player2_height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect( self.rect.x, self.rect.y + dy, self.player2_width, self.player2_height):
                    # check if below the tile (jumping)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the tile (falling)
                    elif self.vel_y > 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            if pygame.sprite.spritecollide(self, fly_group, False):
                game_over2 = 1
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over2 = 1
            
            for snow in snow_group:
                if snow.rect.colliderect( self.rect.x, self.rect.y + dy, self.player2_width, self.player2_height):
                    if self.vel_y < 0:
                        dy = snow.bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the tile (falling)
                    elif self.vel_y > 0:
                        dy = snow.top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False
               
                

            #update player coordinates
            if  self.rect.x + dx < 0 or self.rect.right + dx >= 1200:
                dx = 0
            self.rect.x += dx
            self.rect.y += dy

        elif game_over2 == 1:
            self.player2 = self.dead_image
            draw_text('GAME OVER...', text_font, color, 400, 250)
            self.rect.y -= 5
        screen.blit(self.player2, self.rect)

        return game_over2
    
    def update1(self,collide_list2):
        if pygame.sprite.spritecollide(self, gate_group, False):
                if 2 not in collide_list2:
                    collide_list2.append(2)
        else:
                if 2 in collide_list2:
                    collide_list2.remove(2)
        return collide_list2
    
    def reset(self,x,y):
        self.player2_right = [] #list to store all images of player1 walking to right
        self.player2_left = []
        self.index = 0
        self.counter = 0
        for i in range (1,4):
            player2_surf = pygame.image.load(f'player/blue{i}.png').convert_alpha() # load the image to make the animation
            player2_surf = pygame.transform.scale(player2_surf,(25,40))
            player2_surf_left = pygame.transform.flip(player2_surf, True,False)
            self.player2_right.append(player2_surf) # add the image in the list
            self.player2_left.append(player2_surf_left)
        self.dead_image = pygame.transform.scale(pygame.image.load('player/dead.png'),(25,40))
        self.player2 = self.player2_right[self.index] #access the images in the list
        self.rect = self.player2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player2_width = self.player2.get_width()
        self.player2_height = self.player2.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,5,0,0,0,0,0,0,0,7,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,3,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,5,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,3,3,3,0,1,1,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,3,1,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0],
[0,0,5,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,1,1],
[1,1,3,3,3,1,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,1,3,3,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,5],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,2,1,0,0,0,0,0,0,0,1,1,1,1,2,2,1,1,1,0,1,1,1,3,3],
[0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,2,2,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

player1 = Player1(0,570) # player objects
player2 = Player2(0,570)

fly_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
snow_group = pygame.sprite.Group()
gate_group = pygame.sprite.Group()
bluegem_group = pygame.sprite.Group()
redgem_group = pygame.sprite.Group()

score_red = Red_gem(tile_size//2, tile_size//2)
redgem_group.add(score_red)
score_blue = Blue_gem(tile_size//2, tile_size + 15)
bluegem_group.add(score_blue)

world = World(world_data)
restart_button = Button(550, 350, restart_img)
start_button = Button(550,300, start_img)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

       
    #world
    screen.blit(scaled_sky_img,(0,0))
    
    if menu == 0:
        screen.blit(title_surf, title_rect)
        screen.blit(credit_surf, credit_rect)
        if start_button.display():
            menu = 1

    elif menu == 1:
        world.display()
        if game_over1 == 0 and game_over2 == 0:
            fly_group.update()
            if pygame.sprite.spritecollide(player1, redgem_group, True):
                score_1 += 1
            draw_text(' ' + str(score_1), score_font, color, tile_size + 10, 15)

            if pygame.sprite.spritecollide(player2, bluegem_group, True):
                score_2 += 1
            draw_text(' ' + str(score_2), score_font, color, tile_size + 10, 45)
            


        fly_group.draw(screen)
        lava_group.draw(screen)
        snow_group.draw(screen)
        gate_group.draw(screen)
        bluegem_group.draw(screen)
        redgem_group.draw(screen)
        game_over1 = player1.update(game_over1)
        collide_list1 = player1.update1(collide_list1)
        game_over2 = player2.update(game_over2)
        collide_list2 = player2.update1(collide_list2)
        

        if game_over1 == 1 or game_over2 == 1:
            if restart_button.display():
                    player1.reset(0,570)
                    player2.reset(0,570)
                    fly_group.empty()            
                    world.reset(world_data)
                    game_over1 = 0
                    game_over2 = 0
                    score_1 = 0
                    score_2 = 0

        if len(collide_list1) == 1 and len(collide_list2) == 1:
            menu = 3
    else:
         draw_text('YOU WIN!!!', text_font, color, 450, 250)

    pygame.display.update()
    clock.tick(60)


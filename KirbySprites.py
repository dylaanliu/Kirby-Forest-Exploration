import pygame, time, random

class Player(pygame.sprite.Sprite): 
    '''This class defines the sprite for the Player'''
    def __init__(self, screen): 
        '''This initializer takes a screen surface, and player number as 
        parameters.  Depending on the player number it loads the appropriate 
        image and positions it on the left or right end of the court'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
        
        self.start = time.time() 
        self.current = time.time()
        
        self.jump_counter = 0
        self.move_counter = 0
        self.atk_counter = 0
        self.j_atk_counter = 0
        self.jump_counter2 = 0
        self.fall_counter = 5
        
        self.eyes_closed = False
        self.move = False
        self.attack_button = False
        self.on_ground = True
        self.if_jump = False
        self.fall = False
        self.no_jump = False
        
        self.__idle = []
        self.__walk_right = []
        self.__walk_left = []
        self.__jump_right = []
        self.__jump_left = []
        self.__attack_right = []
        self.__attack_left = []
        self.__jump_attack_right = []
        self.__jump_attack_left = []
        
        # Appends images to self.__idle for idle animation
        for idle in range(1, 3):
            self.__idle.append(("./Kirby Sprites/Idle/Kirby Idle " + str(idle) + ".gif"))

        for x in range(1, 11):
            # Appends images to self.__walk_left for
        # walking left animation
            self.__walk_left.append(("./Kirby Sprites/Walk/Walk Left " + str(x) + ".gif"))
            # Appends images to self.__walk_right for
            # walking right animation
            self.__walk_right.append(("./Kirby Sprites/Walk/Walk Right " + str(x) + ".gif"))
            # Appends images to self.__jump_right for
            # jumping right animation
            self.__jump_right.append("./Kirby Sprites/Jump/Jump Right " + str(x) + ".gif") 
            # Appends images to self.__jump_left for
            # jumping left animation
            self.__jump_left.append("./Kirby Sprites/Jump/Jump Left " + str(x) + ".gif")  
            
        for g_atk in range(1, 8):
            # Appends images to self.__attack_right for
            # attacking right animation
            self.__attack_right.append("./Kirby Sprites/Attack/Attack Right " + str(g_atk) + ".gif")
            # Appends images to self.__attack_left for
            # attacking left animation
            self.__attack_left.append("./Kirby Sprites/Attack/Attack Left " + str(g_atk) + ".gif")
            
        # Appends images to 
        #self.__jump_attack_right for right jump
        # attack animation
        for jump_atk in range(1, 10):
            self.__jump_attack_right.append("./Kirby Sprites/Jump Attack/Jump Attack Right " + str(jump_atk) + ".gif")
            # Appends images to 
            #self.__jump_attack_left for left jump
            # attack animation
            self.__jump_attack_left.append("./Kirby Sprites/Jump Attack/Jump Attack Left " + str(jump_atk) + ".gif")
            
            
        self.image = pygame.image.load(self.__idle[0])
        self.image = self.image.convert() 
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect() 
        self.rect.top = screen.get_height() - 108
        
        # Center the player horizontally in the window. 
        self.rect.centerx = screen.get_width() / 2 
        self.__screen = screen 
        self.__dx = 0
        self.__dy = 0
       
    def change_direction(self, x_change): 
        '''This method takes a (x,y) tuple as a parameter, extracts the  
        x element from it, and uses this to set the players x direction.'''
        self.__dx = x_change[0]
        if self.__dx == 1 or self.__dx == -1:
            self.move = True
        else:
            self.move = False
        
    def attack(self):
        if self.move == False:
            self.attack_button = False
        elif self.move == True:
            self.attack_button = True
            
    def if_attack(self, y_or_n):
        if y_or_n == y:
            return True
        else:
            return False
            
    def jump(self):
        
        self.if_jump = True

    def update(self): 
        '''This method will be called automatically to reposition the 
        player sprite on the screen.'''
        # Check if we have reached the left or right of the screen. 
        # If not, then keep moving the player in the same x direction. 
        if ((self.rect.left > 0) and (self.__dx > 0)) or \
           ((self.rect.right < self.__screen.get_width() - 0) and (self.__dx < 0)): 
            self.rect.left -= (self.__dx * 5)
            
        # To control jumping (going up and then back
        # down)
        if self.if_jump == True and self.no_jump == False:
            if self.jump_counter2 != 5:
                self.jump_counter2 += 1
                self.rect.top -= 20
            if self.jump_counter2 == 5:
                self.jump_counter2 = 0
                self.if_jump = False
                self.fall = True
        if self.fall == True:
            self.no_jump = True
            if self.fall_counter != 0:
                self.fall_counter -= 1
                self.rect.top += 20
            if self.fall_counter == 0:
                self.fall_counter = 5
                self.fall = False
                self.no_jump = False
                
        if self.rect.bottom < 372:
            self.on_ground = False
        if self.rect.bottom >= 372:
            self.on_ground = True
            
        self.current = time.time()
        
        # For idle (with animation)
        if self.current - self.start > 1 and self.eyes_closed == False:
            self.image=pygame.image.load(self.__idle[1])
            self.image = self.image.convert()
            self.start = time.time()
            self.eyes_closed = True
        elif self.current - self.start > 0.05 and self.eyes_closed == True:
            self.image=pygame.image.load(self.__idle[0])
            self.image=self.image.convert()
            self.start = time.time()
        
        # For moving right (with animation)
        if self.move_counter >= 0 and self.move_counter < 10:
            if self.__dx == -1:
                self.image = pygame.image.load(self.__walk_right[self.move_counter])
                self.image = self.image.convert()
                self.move_counter += 1
            elif self.__dx == 1:
                self.image=pygame.image.load(self.__walk_left[self.move_counter])
                self.image = self.image.convert()
                self.move_counter += 1
            if self.move_counter == 10 and self.__dx == -1:
                self.move_counter = 0
            elif self.move_counter == 10 and self.__dx == 1:
                self.move_counter = 0
            if self.__dx == 0:
                self.move_counter = 0
            
        # For Jumping (with animation)
        if self.jump_counter >= 0 and self.jump_counter < 10 and self.on_ground == False:
            if self.__dx == -1:
                self.image = pygame.image.load(self.__jump_right[self.jump_counter])
                self.image = self.image.convert()
                self.jump_counter += 1
            elif self.__dx == 1:
                self.image = pygame.image.load(self.__jump_left[self.jump_counter])
                self.image = self.image.convert()
                self.jump_counter += 1
            if self.jump_counter == 10 and self.__dx == -1:
                self.jump_counter = 0
            elif self.jump_counter == 10 and self.__dx == 1:
                self.jump_counter = 0
            if self.__dx == 0:
                self.jump_counter = 0
            
        # For Attacking Right/Left
        if self.atk_counter >= 0 and self.atk_counter < 7 and self.attack_button == True:
            if self.__dx == -1:
                self.image = pygame.image.load(self.__attack_right[self.atk_counter])
                self.image = self.image.convert()
                self.atk_counter += 1
            elif self.__dx == 1:
                self.image = pygame.image.load(self.__attack_left[self.atk_counter])
                self.image = self.image.convert()
                self.atk_counter += 1
                if self.atk_counter == 6:
                    self.rect.centerx += 3
                    if self.rect.left < 0:
                        self.rect.left = 0
                if self.atk_counter < 6:
                    self.rect.centerx -= 3
            if self.atk_counter == 7 and ((self.__dx == -1) or (self.__dx == 1)):
                self.atk_counter = 0
                self.attack_button = False
            if self.__dx == 0:
                self.atk_counter = 0
               
        # For Jump Attacking Right/Left
        if self.j_atk_counter >= 0 and self.j_atk_counter < 7 and self.attack_button == True and self.on_ground == False:
            if self.__dx == -1:
                self.image = pygame.image.load(self.__jump_attack_right[self.j_atk_counter])
                self.image = self.image.convert()
                self.j_atk_counter += 1
            elif self.__dx == 1:
                self.image = pygame.image.load(self.__jump_attack_left[self.j_atk_counter])
                self.image = self.image.convert()
                self.j_atk_counter += 1
            if self.j_atk_counter == 7 and ((self.__dx == -1) or (self.__dx == 1)):
                self.j_atk_counter = 0
                self.attack_button = False
            if self.__dx == 0:
                self.j_atk_counter = 0
                
                
class Enemy(pygame.sprite.Sprite):
    '''This class defines the sprite for the enemies'''
    def __init__(self, screen, enemy_num, side):
        pygame.sprite.Sprite.__init__(self) 
        
        self.start_grizzo = time.time()
        self.current_grizzo = time.time()
         
        self.__screen = screen
        self.enemy_num = enemy_num
        self.side = side

        self.spawn = False
        
        self.grizzo = False
        self.waddle = False
        self.lololo = False
        self.bronto = False
        
        self.up = True
        self.down = False
        
        self.g_going_r = True
        
        self.b_counter = 0
        self.d_counter = 0
        self.g_counter = 0
        self.l_counter = 0
        
        self.up_counter = 0
        self.down_counter = 5
        
        self.__grizzo_r = []
        self.__grizzo_l = []
        self.__dee_r = []
        self.__dee_l = []
        self.__lololo_r = []
        self.__lololo_l = []
        self.__bronto_r = []
        self.__bronto_l = []
        self.__grizzo_death_r = [] # Still need anim.
        self.__grizzo_death_l = []# Still need anim.
        self.__dee_death_r = []# Still need anim.
        self.__dee_death_l = []# Still need anim.
        self.__lololo_death_r = []# Still need anim.
        self.__lololo_death_l = []# Still need anim.
        
        for enemy in range(1, 3):
            # Appends images to self.__Grizzo_r for
            # Grizzo walking right
            self.__grizzo_r.append(("./Enemy Sprites/Grizzo/Grizzo Right " + str(enemy) + ".gif"))
            # Appends images to self.__Grizzo_l for
            # Grizzo walking left
            self.__grizzo_l.append(("./Enemy Sprites/Grizzo/Grizzo Left " + str(enemy) + ".gif"))
            # Appends images to self.__dee_r for
            # Waddle Dee walking right
            self.__dee_r.append(("./Enemy Sprites/Waddle Dee/Waddle Dee Right " + str(enemy) + ".gif"))
            # Appends images to self.__dee_l for
            # Waddle Dee walking left
            self.__dee_l.append(("./Enemy Sprites/Waddle Dee/Waddle Dee Left " + str(enemy) + ".gif"))
            # Appends images to self.__lololo_r for
            # Lololo walking right
            self.__lololo_r.append(("./Enemy Sprites/Lololo/Lololo Right " + str(enemy) + ".gif"))
            # Appends images to self.__lololo_l for
            # Lololo walking left
            self.__lololo_l.append(("./Enemy Sprites/Lololo/Lololo Left " + str(enemy) + ".gif"))
            
        for fly in range(1, 4):
            # Appends images to self.__bronto_r for
            # Bronto Burt flying right
            self.__bronto_r.append(("./Enemy Sprites/Bronto Burt/Bronto Burt Right " + str(fly) + ".gif"))
            # Appends images to self.__bronto_l for
            # Bronto Burt flying left
            self.__bronto_l.append(("./Enemy Sprites/Bronto Burt/Bronto Burt Left " + str(fly) + ".gif"))
            
        if self.enemy_num == 1:
            self.grizzo = True
            if self.side == "L":
                self.spawn = True
                self.image = pygame.image.load(self.__grizzo_r[0])
            else:
                self.spawn = True
                self.image = pygame.image.load(self.__grizzo_l[0])
            self.image = self.image.convert() 
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect() 
            self.rect.top = screen.get_height() - 126
            if self.side == "L":
                self.rect.centerx = 5
            else:
                self.rect.centerx = 635
                
        if self.enemy_num == 2:
            self.waddle = True
            if self.side == "L":
                self.image = pygame.image.load(self.__dee_r[0])
            else:
                self.image = pygame.image.load(self.__dee_l[0])
            self.image = self.image.convert() 
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect() 
            self.rect.top = screen.get_height() - 112
            if self.side == "L":
                self.rect.centerx = 5
            else:
                self.rect.centerx = 635
                
        if self.enemy_num == 3:
            self.lololo = True
            if self.side == "L":
                self.image = pygame.image.load(self.__lololo_r[0])
            else:
                self.image = pygame.image.load(self.__lololo_l[0])
            self.image = self.image.convert() 
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect() 
            self.rect.top = screen.get_height() - 112
            if self.side == "L":
                self.rect.centerx = 5
            else:
                self.rect.centerx = 635
                
        if self.enemy_num == 4:
            self.bronto = True
            if self.side == "L":
                self.image = pygame.image.load(self.__bronto_r[0])
            else:
                self.image = pygame.image.load(self.__bronto_l[0])
            self.image = self.image.convert() 
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect() 
            self.rect.top = screen.get_height() - 140
            if self.side == "L":
                self.rect.centerx = 5
            else:
                self.rect.centerx = 635
            
        self.__dx = random.randrange(1, 6)
        if self.enemy_num == 4:
            self.__dy = 6
        else:
            self.__dy = 0
            
        if self.enemy_num == 4 and self.up == True:
            if self.up_counter != 5:
                self.up_counter += 1
                self.rect.top -= 50
            if self.up_counter == 5:
                self.up_counter = 0
                self.up = False
                self.down = True
        if self.enemy_num == 4 and self.down == True:
            if self.down_counter != 0:
                self.down_counter -= 1
                self.rect.top += 50
            if self.down_counter == 0:
                self.down_counter = 5
                self.down = False
                self.up = True
        
        '''self.hit = False'''
        '''self.going_off_screen = False
        self.died = False
        self.death_up = 0
        self.death_down = 5
        
        self.g_death_counter = 1'''
        
        
        
    def hit(self):
        self.__dy = 1
        self.hit = True
        self.died = True

    def update(self): 
        if ((self.rect.left > 0) and (self.__dx < 0)) or \
           ((self.rect.right < self.__screen.get_width()) and (self.__dx > 0)): 
            self.rect.left += self.__dx
            self.g_going_r = True
        else:
            self.__dx = -self.__dx
            self.g_going_r = False
            
        if ((self.rect.top > 200) and (self.__dy > 0)) or \
           ((self.rect.bottom + 100 < self.__screen.get_height()) and (self.__dy < 0)): 
            self.rect.top -= self.__dy 
        # If yes, then reverse the y direction.  
        else: 
            self.__dy = -self.__dy
        '''if self.__dy > 0 and self.hit == True:
            self.__dx = 0
            if self.death_up != 2:
                self.death_up += 1
                self.rect.top += 20
            if self.death_up == 2:
                self.death_up = 0
                self.hit = False
                self.going_off_screen = True
        if self.going_off_screen == True:
            if self.death_down != 0:
                self.death_down -= 1
                self.rect.top += 20
            if self.death_down == 0:
                self.death_down = 5
                self.going_off_screen = False'''
        '''if self.hit == True:
                if self.death_up != 2:
                    self.death_up += 1
                    self.rect.top += 20
                if self.death_up == 2:
                    self.death_up = 0
                    self.hit = False
                    self.going_off_screen = True
            if self.going_off_screen == True:
                if self.death_down != 0:
                    self.death_down -= 1
                    self.rect.top += 20
                if self.death_down == 0:
                    self.death_down = 5
                    self.going_off_screen = False'''
        
        if self.g_counter >= 0 and self.g_counter < 2 and self.grizzo == True:
            if self.side == "L" and self.spawn == True and self.g_going_r == True:
                self.image = pygame.image.load(self.__grizzo_r[self.g_counter])
                self.image = self.image.convert()
                self.g_counter += 1
            if self.spawn == True and self.g_going_r == False:
                self.image = pygame.image.load(self.__grizzo_l[self.g_counter])
                self.image = self.image.convert()
                self.g_counter += 1
        if self.g_counter == 2:
            self.g_counter = 0
            
        if self.d_counter >= 0 and self.d_counter < 2 and self.waddle == True:
            if self.side == "L":
                self.image = pygame.image.load(self.__dee_r[self.d_counter])
                self.image = self.image.convert()
                self.d_counter += 1
            else:
                self.image = pygame.image.load(self.__dee_l[self.d_counter])
                self.image = self.image.convert()
                self.d_counter += 1
        if self.d_counter == 2:
            self.d_counter = 0
            
        if self.l_counter >= 0 and self.l_counter < 2 and self.lololo == True:
            if self.side == "L":
                self.image = pygame.image.load(self.__lololo_r[self.l_counter])
                self.image = self.image.convert()
                self.l_counter += 1
            else:
                self.image = pygame.image.load(self.__lololo_l[self.l_counter])
                self.image = self.image.convert()
                self.l_counter += 1
        if self.l_counter == 2:
            self.l_counter = 0
            
        if self.b_counter >= 0 and self.b_counter < 3 and self.bronto == True:
            if self.side == "L":
                self.image = pygame.image.load(self.__bronto_r[self.b_counter])
                self.image = self.image.convert()
                self.b_counter += 1
            else:
                self.image = pygame.image.load(self.__bronto_l[self.b_counter])
                self.image = self.image.convert()
                self.b_counter += 1
        if self.b_counter == 3:
            self.b_counter = 0
        
        '''self.current_grizzo = time.time()
        
        if self.current_grizzo - self.start_grizzo > 5:
            if self.g_going_r == True:
                self.image=pygame.image.load(self.__grizzo_r[0])
                self.image = self.image.convert()
                self.start = time.time()
                self.g_going_r = False
            elif self.g_going_r == False:
                self.image=pygame.image.load(self.__grizzo_l[0])
                self.image = self.image.convert()
                self.start = time.time()
                self.g_going_r == True
        elif self.current_grizzo - self.start_grizzo > 1:
            if self.g_going_r == True:
                self.image = pygame.image.load(self.__grizzo_r[1])
                self.image=self.image.convert()
                self.start = time.time()
                self.g_going_r = False
            elif self.g_going_r == False:
                self.image = pygame.image.load(self.__grizzo_l[1])
                self.image=self.image.convert()
                self.start = time.time()
                self.g_going_r == True'''
        
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self): 
        '''This initializer loads the font and sets starting score
        to 0'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
        
        # Load our custom font, and initialize the starting score. 
        self.__font = pygame.font.SysFont("Comic Sans MS", 30) 
        self.__score = 0
        
    def plus_1000(self):
        self.__score += 1000
        
    def minus_1000(self):
        self.__score -= 1000
        if score < 0:
            self.__score = 0
        
    def update(self):
        message = "Score: %d" % (self.__score)
        self.image = self.__font.render(message, 1, (0,191, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)
        
class LifeKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the number
    of lives.'''
    def __init__(self): 
        '''This initializer loads the font and sets the lives 
        to 3 (3 Kirby images)'''
        # Call the parent __init__() method 
        pygame.sprite.Sprite.__init__(self) 
        
    def update(self):
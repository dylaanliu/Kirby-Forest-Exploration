"""
   Author: Dylan Liu
   
   Date: June 6, 2012      
   
   Description: Summative - Video Game - Kirby's Forest
                      Exploration
                
"""

# I - IMPORT AND INITIALIZE 
import pygame, random, KirbySprites
pygame.init() 
screen = pygame.display.set_mode((640, 480)) 

def main(): 
    '''This function defines the 'mainline logic' for the Super Break-Out Game.'''
       
    # DISPLAY 
    pygame.display.set_caption("Kirby's Forest Exploration") 
      
    # ENTITIES 
    # Background image
    background = pygame.image.load("./Background/Forest.png")
    background = background.convert() 
    screen.blit(background, (0, 0)) 
    
    a = False
    movement = False
    random_num = random.randrange(2, 6)
    #random_num2 = random.randrange(2, 6)
    player = KirbySprites.Player(screen)
    scorekeeper = KirbySprites.ScoreKeeper()
    enemies = []
    #non_enemies = []
    for x in range(1, 2):
        side = random.randrange(1,3)
        if side == 1:
            side = "L"
        else:
            side = "R"
        enemy_num = random.randrange(1,5)
        print enemy_num
        enemies.append(KirbySprites.Enemy(screen, enemy_num, side))
    enemyGroup = pygame.sprite.Group(enemies)
    allSprites = pygame.sprite.OrderedUpdates(enemies, player, scorekeeper)
    
    # ASSIGN  
    clock = pygame.time.Clock() 
    keepGoing = True
  
    # Hide the mouse pointer 
    pygame.mouse.set_visible(False) 
  
    # LOOP 
    while keepGoing: 
      
        # TIME 
        clock.tick(30) 
        
        # EVENT HANDLING
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif event.key == pygame.K_RIGHT:
                    player.change_direction((-1, 0))
                    movement = True
                elif event.key == pygame.K_LEFT:
                    player.change_direction((1, 0))
                    movement = True
                elif event.key == pygame.K_UP:
                    player.jump()
                    movement = True
                elif event.key == pygame.K_a:
                    player.attack()
                    a = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.change_direction((0, 0))
                    movement = False
                elif event.key == pygame.K_LEFT:
                    player.change_direction((0, 0))
                    movement = False
                elif event.key == pygame.K_UP:
                    movement = False
                elif event.key == pygame.K_a:
                    a = False
                    
        '''attacked = pygame.sprite.spritecollide(player, enemyGroup, False)
        if attacked:
            if a == True:
                enemy.hit()'''
            
        if a == True and movement == True and pygame.sprite.spritecollide(player, enemyGroup, True):
            print a
            scorekeeper.plus_1000()
            
        if enemies[0].rect.colliderect(player.rect):
            print 'x'
            
        # REFRESH SCREEN 
        allSprites.clear(screen, background) 
        allSprites.update() 
        allSprites.draw(screen)        
        pygame.display.flip() 
        
        
          
    #  Display "Game Over"
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
      
    pygame.quit()
    
# Call the main function 
main()
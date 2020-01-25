import pygame
from pygame.locals import *
import math
import worldManager
import time

pygame.init()
font = pygame.font.Font('Wolfenstein.ttf', 40)

worldMap =[
  [8,8,8,8,8,8,8,8,8,8,8,4,4,6,4,4,6,4,6,4,4,4,6,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,6,6,6,0,6,4,6],
  [8,8,8,8,0,8,8,8,8,8,8,4,4,4,4,4,4,6,0,0,0,0,0,6],
  [7,7,7,7,0,7,7,7,7,0,8,0,8,0,8,0,8,4,0,4,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,0,0,0,0,0,6],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,0,0,0,0,4],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,6,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,4,6,0,6,6,6],
  [7,7,7,7,0,7,7,7,7,8,8,4,0,6,8,4,8,3,3,3,0,3,3,3],
  [2,2,2,2,0,2,2,2,2,4,6,4,0,0,6,0,6,3,0,0,0,0,0,3],
  [2,2,0,0,0,0,0,2,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [2,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [1,0,0,0,0,0,0,0,1,4,4,4,4,4,6,0,6,3,3,0,0,0,3,3],
  [2,0,0,0,0,0,0,0,2,2,2,1,2,2,2,6,6,0,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,5,5,5,5,5,5,5,5,5]
];

#worldMap =[
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#]

sc = pygame.display.set_mode((1000, 700))
sprite_positions=[]
  #(20.5, 11.5, 2), #green light in front of playerstart
  ##green lights in every room
  #(18.5,4.5, 2),
  #(10.0,4.5, 2),
  #(10.0,12.5,2),
  #(3.5, 6.5, 2),
  #(3.5, 20.5,2),
  #(3.5, 14.5,2),
  #(14.5,20.5,2),
  
  ##row of pillars in front of wall: fisheye test
  #(18.5, 10.5, 1),
  #(18.5, 11.5, 1),
  #(18.5, 12.5, 1),
  
  ##some barrels around the map
  #(21.5, 1.5, 0),
  #(15.5, 1.5, 0),
  #(16.0, 1.8, 0),
  #(16.2, 1.2, 0),
  #(3.5, 2.5, 0),
  #(9.5, 15.5, 0),
  #(10.0, 15.1,0),
  #(10.5, 15.8,0),
#]

def load_image(image, darken, colorKey = None):
    ret = []
    if colorKey is not None:
        image.set_colorkey(colorKey)
    if darken:
        image.set_alpha(127)
    for i in range(image.get_width()):
        s = pygame.Surface((1, image.get_height())).convert()
        s.blit(image, (- i, 0))
        if colorKey is not None:
            s.set_colorkey(colorKey)
        ret.append(s)
    return ret

def main():
  
    t = time.process_time() #time of current frame
    oldTime = 0 #time of previous frame
    
    size = w, h = 640,580
    pygame.init()
    window = pygame.display.set_mode((640,580), pygame.FULLSCREEN)
    pygame.display.set_caption("Raycaster")

    #pixScreen = pygame.surfarray.pixels2d(window)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    
    f = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    
    wm = worldManager.WorldManager(worldMap,sprite_positions, 22, 11.5, -1, 0, 0, .66)
    
    weapons = [Weapon("fist", '∞'),
               Weapon("pistol", 120),
               Weapon("shotgun", 60),
               Weapon("dbshotgun", 40),
               Weapon("chaingun", 999),
               Weapon("plasma", 100),
               Weapon("rocket", 30),
               Weapon("bfg", 60),
               Weapon("chainsaw", '∞')]
    weapon_numbers = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_0]
    weapon = weapons[1]
    
    while(True):
        clock.tick(60)
        wm.draw(sc)

        pygame.draw.rect(window, (200, 200, 200), (0, 480, 640, 100))
        pygame.draw.rect(window, (30, 30, 30), (15, 490, 80, 80), 2)
        pygame.draw.rect(window, (30, 30, 30), (105, 490, 160, 80), 2)
        pygame.draw.rect(window, (30, 30, 30), (275, 490, 80, 80), 2)
        pygame.draw.rect(window, (30, 30, 30), (365, 490, 80, 80), 2)
        pygame.draw.rect(window, (30, 30, 30), (455, 490, 80, 80), 2)
        pygame.draw.rect(window, (30, 30, 30), (545, 490, 80, 80), 2)

        t_b_floor = font.render('Floor', False, (70, 70, 150))
        t_b_score = font.render('Score', False, (70, 70, 150))
        t_b_lives = font.render('Lives', False, (70, 70, 150))
        t_b_health = font.render('Health', False, (70, 70, 150))
        t_b_ammo = font.render('Ammo', False, (70, 70, 150))

        t_b_floor_exit = f.render('Sandbox', False, (20, 20, 20))
        t_b_score_exit = f.render('Sandbox', False, (20, 20, 20))
        t_b_lives_exit = f.render('Sandbox', False, (20, 20, 20))
        t_b_health_exit = f.render('100', False, (20, 20, 20))
        t_b_ammo_exit = f.render(str(weapon.bullets), False, (20, 20, 20))

        sc.blit(t_b_floor, (25, 490))
        sc.blit(t_b_score, (155, 490))
        sc.blit(t_b_lives, (285, 490))
        sc.blit(t_b_health, (465, 490))
        sc.blit(t_b_ammo, (555, 490))

        sc.blit(t_b_floor_exit, (25, 550))
        sc.blit(t_b_score_exit, (155, 550))
        sc.blit(t_b_lives_exit, (285, 550))
        sc.blit(t_b_health_exit, (495, 550))
        sc.blit(t_b_ammo_exit, (585, 550))


        frameTime = float(clock.get_time()) / 1000.0 # frameTime is the time this frame has taken, in seconds
        t = time.process_time()
        text = f.render(str(clock.get_fps()), False, (255, 255, 0))
        window.blit(text, text.get_rect(), text.get_rect())
        weapon.draw(sc, t)
        pygame.display.flip()

        # speed modifiers
        moveSpeed = frameTime * 5.0 # the constant value is in squares / second
        rotSpeed = frameTime * 3.0 # the constant value is in radians / second


        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == QUIT: 
                return 
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif keys[pygame.K_SPACE]:
                    # shoot
                    weapon.play()
                elif event.key in weapon_numbers:
                    weapon.stop()
                    weapon = weapons[weapon_numbers.index(event.key)]
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    weapon.stop()
            else:
                pass 
        
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            # move forward if no wall in front of you
            moveX = wm.camera.x + wm.camera.dirx * moveSpeed
            if worldMap[int(moveX)][int(wm.camera.y)] == 0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0:
                wm.camera.x += wm.camera.dirx * moveSpeed
            moveY = wm.camera.y + wm.camera.diry * moveSpeed
            if worldMap[int(wm.camera.x)][int(moveY)] == 0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0:
                wm.camera.y += wm.camera.diry * moveSpeed
        if keys[K_DOWN]:
            # move backwards if no wall behind you
            if worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0:
                wm.camera.x -= wm.camera.dirx * moveSpeed
            if worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0:
                wm.camera.y -= wm.camera.diry * moveSpeed
        if (keys[K_RIGHT] and not keys[K_DOWN]) or (keys[K_LEFT] and keys[K_DOWN]):
            # rotate to the right
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
            wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
        if (keys[K_LEFT] and not keys[K_DOWN]) or (keys[K_RIGHT] and keys[K_DOWN]): 
            # rotate to the left
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
            wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)

fps = 8
class Weapon(object):
    
    def __init__(self, weaponName="shotgun", bullets='∞', frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        self.bullets = bullets
        for i in range(frameCount):
            img = pygame.image.load("pics/weapons/%s%s.png" % (weaponName, i+1)).convert()
            img = pygame.transform.scale2x(img)
            img = pygame.transform.scale2x(img)
            img.set_colorkey(img.get_at((0,0)))
            self.images.append(img)
    def play(self):
        if self.bullets != 0:
            self.playing = True
            self.loop = True
            if self.bullets != '∞':
                self.bullets -= 1
    def stop(self):
        self.playing = False
        self.loop = False
    def draw(self, surface, time):
        if(self.playing or self.frame > 0):
            if(time > self.oldTime + 1./fps):
                self.frame = (self.frame+1) % len(self.images)
                if self.frame == 0: 
                    if self.loop:
                        self.frame = 1
                    else:
                        self.playing = False
                        
                self.oldTime = time
        img = self.images[self.frame]
        surface.blit(img, (surface.get_width()/2 - img.get_width()/2, surface.get_height()-img.get_height() - 100))
            
if __name__ == '__main__':
    main()
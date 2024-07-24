import pygame, camera_script
from camera_script import camera

class AnimatedSprite:
    def __init__(self):
        self.animations = {}
        self.frame = 0
        self.animation_timer = 0
        self.animation_loop = True
        self.new_animation()
        self.x = 0
        self.y = 0
        self.current_animation = None
        
    def new_animation(self,name: str,spritesheet: pygame.Surface,
                      start: list,dimensions: list,frames: int,speed: int,end: str,offset: tuple):
        '''
        Creates a new animation for your sprite, from a spritesheet.
        '''
        #crops image to only what is needed
        image = pygame.Surface((dimensions[0],dimensions[1]*frames)).convert_alpha()
        image.fill((0,0,0,0))
        image.blit(spritesheet,(-start[0],-start[1]))
        
        animation = {"name":name,"spritesheet":image,"dimensions":dimensions,"frames":frames,"speed":speed,"end":end,"offset":offset}
        self.animations[name] = animation
        
    def set_animation(self,anim:str="default",loop:int=-1):
        '''
        Sets the current animation to the selected animation. 
        The loop argument indicates how many times the animation will replay. 
        A negative value will make it loop indefinitely.
        '''
        if anim not in self.animations:
            anim = "default"
        
        valid = True
        if self.current_animation:
            if self.current_animation["name"] == anim:
                valid = False
                
        if valid:
            self.frame = 0
            self.animation_timer = 0
            self.animation_loop = True
            self.current_animation = self.animations[anim]
            self.animation_loop = loop
            self.image = pygame.Surface(self.current_animation["dimensions"]).convert_alpha()
            self.rect = self.image.get_rect()
    
    def play_animation(self):
        '''
        Updates animation. Goes down vertically through the spritesheet.
        '''
        self.image.fill((0,0,0,0))
        self.image.blit(self.current_animation["spritesheet"],(0,-self.current_animation["dimensions"][1]*self.frame))
        self.align()
        self.animation_timer += 1
        if self.animation_timer == self.current_animation["speed"]:
            self.animation_timer = 0
            self.frame += 1
            if self.frame == self.current_animation["frames"]:
                if self.animation_loop == 0:
                    self.finish_animation()
                else:
                    self.animation_loop -= 1
                self.frame = 0
    
    def align(self):
        self.rect.center = self.x,self.y
    
    def finish_animation(self):
        self.set_animation(self.current_animation["end"])
        self.play_animation()

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x+self.current_animation["offset"][0]-camera.x, self.rect.y+self.current_animation["offset"][1]-camera.y))
    
    def update(self):
        self.play_animation()
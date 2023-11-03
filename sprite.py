import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups, image = pygame.Surface((20, 20)), position = (0,0)):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = position)

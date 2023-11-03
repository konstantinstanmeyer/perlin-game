import pygame
from sprite import Entity

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites])
    def update(self):
        pass
    def draw(self):
        self.app.screen.fill('blue')
        self.sprites.draw(self.app.screen)
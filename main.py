import pygame
import sys
from scene import Scene

# abstracting the steps to have coherent control of each "phase" within a typical pygame loop (init, run, update, draw)
# using OOP for increased understanding, could instead run functionally
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))

        self.clock = pygame.time.Clock()

        self.running = True

        self.scene = Scene(self)
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.scene.update()

        pygame.display.update()
        self.clock.tick(60)
    def draw(self):
        self.scene.draw()
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
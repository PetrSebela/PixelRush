import pygame
from pygame import Vector2
from config import config
from engine.scene import scene

class camera:
    def __init__(self, config, canvas:pygame.Surface, scene:scene) -> None:
        self.camera_size = (1280, 720)
        
        # add this feature later, too lazy to add it now and there are more important things to do 
        self.ssf = config.RESOLUTION[0] / self.camera_size[0]

        self.position = pygame.Vector2(0,0)
        self.camera_offset = Vector2(
            (self.camera_size[0] / 2 * self.ssf),
            (self.camera_size[1] / 2 * self.ssf)
        )

        # render stuff
        self.canvas = canvas
        self.scene = scene


    def move_to(self, vector:Vector2):
        self.position = vector


    def draw_scene(self):
        for layer in self.scene.layers:
            for go in layer.gos:
                compensated_position = Vector2(
                    self.position.x,
                    -self.position.y
                )
                go.render(self.canvas, self.camera_offset, compensated_position)
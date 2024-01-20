from pygame import Vector2, Surface
import pygame

from engine.game_object import game_object
from config import config

class tilemap(game_object):
    def __init__(self) -> None:
        super().__init__(static=True) 
        self.tiles = []
        self.tile_map = {}
        self.tile_size = 0
        self.paralax = 0


    def render(self, canvas:Surface, camera_offset:Vector2, camera_position:Vector2) -> None:
        for tile_position in self.tile_map:
            x = tile_position[0] * self.tile_size + camera_offset.x - camera_position.x
            y = tile_position[1] * self.tile_size + camera_offset.y + camera_position.y
            sprite = self.tiles[self.tile_map[tile_position]]
            
            canvas.blit(sprite, (x , y))

            if config.DEBUG:
                pygame.draw.rect(canvas, (255,20,150),(x,y,self.tile_size,self.tile_size),1)
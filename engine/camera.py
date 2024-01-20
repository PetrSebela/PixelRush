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
            (self.camera_size[0] / 2 * self.ssf) - self.position.x,
            (self.camera_size[1] / 2 * self.ssf) + self.position.y
        )

        # render stuff
        self.canvas = canvas
        self.scene = scene


    def move_by(self,vector:Vector2):
        self.position += vector
        self.update_offsets()


    def


    def update_offsets(self):
        self.camera_offset = Vector2(
            (self.camera_size[0] / 2 * self.ssf) - self.position.x,
            (self.camera_size[1] / 2 * self.ssf) + self.position.y
        )


    def draw_scene(self):
        for layer in self.scene.layers:
            for tile_position in layer.tile_map:
                
                x = tile_position[0] * layer.tile_size + self.camera_offset.x - self.position.x * layer.paralax
                y = tile_position[1] * layer.tile_size + self.camera_offset.y + self.position.y * layer.paralax
                
                
                self.canvas.blit(
                    layer.tiles[layer.tile_map[tile_position]],
                    (x , y)
                )
                
                if not config.DEBUG:
                    continue

                pygame.draw.rect(
                    self.canvas,
                    (0, 220, 120), 
                    (   x, 
                        y, 
                        layer.tile_size,
                        layer.tile_size),
                    1)
                
            if not layer.has_player:
                continue

            for player in self.scene.players:
                player.render(self.canvas, self.camera_offset)
            

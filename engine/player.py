# deps import
from pygame import Vector2, image
from pygame import Vector2, Surface, transform
from pygame import event
import pygame

# engine import
from engine.game_object import game_object
from engine.helper import tuple_to_vector, lerp
from config import config

MAX_SPEED = 20
JUMP_TIME = 2.5
JUMP_FORCE = 6

class player(game_object):
    def __init__(self, sprite_path='', terrain_tilemap=None) -> None:
        # sprite
        self.sprite = image.load(sprite_path)
        self.sprite = transform.scale(self.sprite,(96, 96))
        size = self.sprite.get_size()
        self.size = tuple_to_vector(size)

        self.terrain_tilemap = terrain_tilemap
        self.grounded = False
        
        # jump
        self.is_jumping = False
        self.jump_timer = 0

        # input
        self.wish_direction = Vector2()
        self.jump_key = False

        super().__init__(size=tuple_to_vector(size))
        

    def render(self, canvas:Surface, offset:Vector2, position:Vector2) -> None:
        render_position = Vector2(
            self.position.x + offset.x - position.x,
            self.position.y + offset.y + position.y
        )

        canvas.blit(
            self.sprite,
            (render_position.x, render_position.y)
        )

        if config.DEBUG:
            rect_box = (   
                render_position.x,
                render_position.y, 
                self.size.x, 
                self.size.y)
            
            pygame.draw.rect(
                canvas, 
                (0, 217, 255),
                rect_box,
                1)
            
            pygame.draw.line(
                canvas, 
                (255, 10, 20),
                (render_position.x + self.size.x / 2, render_position.y + self.size.y / 2), 
                (render_position.x + self.size.x / 2 + self.velocity.x * 3, render_position.y + self.size.y / 2 + self.velocity.y * 3))
    
    
    def handle_input(self, event:event) -> None:
        
        match event.type:
            case pygame.KEYDOWN:
                if event.key in config.MOVE_LEFT:
                    self.wish_direction.x -= 1

                elif event.key in config.MOVE_RIGHT:
                    self.wish_direction.x += 1

                elif event.key in config.JUMP:
                    self.jump_key = True

            case pygame.KEYUP:
                if event.key in config.MOVE_LEFT:
                    self.wish_direction.x += 1

                elif event.key in config.MOVE_RIGHT:
                    self.wish_direction.x -= 1
                
                elif event.key in config.JUMP:
                    self.jump_key = False


    def update_physics(self, deltaTime):
        self.velocity.x = self.wish_direction.x * MAX_SPEED
        self.velocity.y += 0.98    
        
        can_jump = self.grounded

        # if self.jump_key:
        #     self.velocity.y += -5 
            

        if (can_jump or self.is_jumping) and self.jump_key and self.jump_timer <= JUMP_TIME:
            self.is_jumping = True
            self.velocity.y += -JUMP_FORCE * (JUMP_TIME - self.jump_timer) / JUMP_TIME
            self.jump_timer += deltaTime


        collision_tuple = self.get_terrain_collision_vector(self.terrain_tilemap, deltaTime)
        self.grounded = collision_tuple[1]
        self.horizontal_block = collision_tuple[0]

        if self.horizontal_block:
            self.velocity.x = 0
        
        if self.grounded:
            self.velocity.y = 0 
            # self.grounded = True
            self.is_jumping = False
            self.jump_timer = 0

        self.position += self.velocity * deltaTime


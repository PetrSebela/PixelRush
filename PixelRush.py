#!/usr/bin/python
#! World space negative Y is up
#! player is 2 units high
 
import pygame
from pygame import Vector2

from config import config
from engine.camera import camera
from engine.scene import scene
from engine.player import player
from engine.helper import lerp

pygame.init()

canvas = pygame.display.set_mode(config.RESOLUTION)
pygame.display.set_caption('Pixel rush')

font = pygame.font.Font('assets/minecraft/Minecraft.ttf', 24)
clock = pygame.time.Clock()

main_scene = scene('assets/maps/test_field.json')
player_object = player('assets/sprites/player.png', main_scene.layers[1].gos[0])
player_object.position = Vector2(0,-100)
#! add automatic player to layer assignment later
main_scene.layers[1].gos.append(player_object)

cam = camera(config, canvas, main_scene)


if __name__ == "__main__":
    # player input
    move_direction = Vector2()
    jumping = False

    # game loop
    running = True
    while running: 
        # new frame setup
        clock.tick(120)
        deltaTime = clock.get_fps()/1000
        canvas.fill(pygame.Color(0, 15, 37))


        # event handling
        for event in pygame.event.get(): 
            match event.type:
                case pygame.QUIT:
                    running = False

                case pygame.KEYDOWN:
                    if event.key in config.EZ_QUIT:
                        running = False
                
            player_object.handle_input(event)

        player_object.update_physics(deltaTime)

        # update scene
        cam.move_to(lerp(cam.position, player_object.position, 0.25 * deltaTime))
        cam.draw_scene()
        
        # debug
        if(config.DEBUG):
            fps = int(clock.get_fps())
            fps_display = font.render(f"FPS: {str(fps)}", True, pygame.Color(255, 255, 255))
            player_position = font.render(f"position: {str(player_object.position)}", True, pygame.Color(255, 255, 255))
            player_velocity = font.render(f"velocity: {str(player_object.velocity)}", True, pygame.Color(255, 255, 255))
            delta_time = font.render(f"dt: {str(deltaTime)}", True, pygame.Color(255, 255, 255))
            
            canvas.blit(fps_display, (0,0))
            canvas.blit(player_position, (0,24))
            canvas.blit(player_velocity, (0,48))
            canvas.blit(delta_time, (0,72))


        pygame.display.flip()
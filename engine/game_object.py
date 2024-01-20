from pygame import Vector2, Surface
from engine.helper import segment_intersects, tuple_to_vector

class game_object:
    def __init__(self, position=Vector2(), size=Vector2(1,1), velocity=Vector2(), static=False) -> None:
        self.position = position
        self.size = size
        self.velocity = velocity
        self.static = static

    def render(self, canvas:Surface, offset:Vector2, position:Vector2) -> None:
        pass

    def update_physics():
        pass

    def get_terrain_collision_vector(self, tilemap_object, deltaTime:float):
        if self.velocity.magnitude_squared() == 0 or deltaTime == 0:
            return Vector2()
        
        intersection_tuple = [False, False]

        checkVectors = {
            (0, 0):[
                [Vector2(1,1), Vector2(0,1)],
                [Vector2(1,1), Vector2(1,0)],
            ],
            (self.size.x, 0):[
                [Vector2(0,1), Vector2(1,1)],
                [Vector2(0,1), Vector2(0,0)],
            ],
            (0, self.size.y):[
                [Vector2(1,0), Vector2(0,0)],
                [Vector2(1,0), Vector2(1,1)],
            ],
            (self.size.x, self.size.y):[
                [Vector2(0,0), Vector2(1,0)],
                [Vector2(0,0), Vector2(0,1)],
            ]
        }
        

        for tile in tilemap_object.tile_map:
            for vertex in checkVectors:
                collision_vertical = segment_intersects(
                    self.position + tuple_to_vector(vertex),
                    self.position + tuple_to_vector(vertex) + self.velocity * deltaTime,

                    (tuple_to_vector(tile) + checkVectors[vertex][0][0]) * tilemap_object.tile_size,
                    (tuple_to_vector(tile) + checkVectors[vertex][0][1]) * tilemap_object.tile_size
                )
                collision_horizontal = segment_intersects(
                    self.position + tuple_to_vector(vertex),
                    self.position + tuple_to_vector(vertex) + self.velocity * deltaTime,

                    (tuple_to_vector(tile) + checkVectors[vertex][1][0]) * tilemap_object.tile_size,
                    (tuple_to_vector(tile) + checkVectors[vertex][1][1]) * tilemap_object.tile_size
                )

                if collision_horizontal:
                    intersection_tuple[0] = True
                if collision_vertical:
                    intersection_tuple[1] = True

        return intersection_tuple



        

    
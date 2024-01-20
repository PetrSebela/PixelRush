import json, pygame
from engine.tilemap import tilemap

class layer():
    def __init__(self) -> None:
        self.gos = []
        self.paralax = 0


class scene:
    def __init__(self,path="") -> None:
        self.scene_descriptor = {}

        self.players = []
        self.layers = []
        
        self.load_scene(path)
        self.construct_scene()


    def load_scene(self, path) -> None:
        with open(path) as file:
            self.scene_descriptor = json.load(file)
        

    def construct_scene(self):
        for layer_key in self.scene_descriptor:
            layer_object = layer()
            tilemap_object = self.get_layer_tilemap(self.scene_descriptor[layer_key])
            layer_object.gos.append(tilemap_object)
            self.layers.append(layer_object)


    def get_layer_tilemap(self, layer_dict):           
        tilemap_object = tilemap()

        tilemap_object.tiles = self.get_layer_tiles(
            layer_dict["tile_sheet"], 
            layer_dict["tile_size"], 
            layer_dict["world_size"])

        tilemap_object.paralax = layer_dict["paralax"]
        tilemap_object.tile_size = layer_dict["world_size"]
        tilemap_object.tile_map = self.get_layer_tile_map(layer_dict["tile_map"])

        return tilemap_object
        

    def get_layer_tiles(self, path, tile_size, world_size):
        tile_sheet = pygame.image.load(path)
        resolution = tile_sheet.get_size()
        tiles = []

        for y in range(0, resolution[1], tile_size):
            for x in range(0, resolution[0], tile_size):
                tile = tile_sheet.subsurface((x ,y , tile_size, tile_size))
                tile = pygame.transform.scale(tile, (world_size, world_size))
                tiles.append(tile)

        return tiles
    

    def get_layer_tile_map(self, layer_tile_map):
        tile_map = {}

        for tile_position_raw in layer_tile_map:
            x = int(tile_position_raw.split(" ")[0])
            y = int(tile_position_raw.split(" ")[1])
            tile_map[(x, y)] = layer_tile_map[tile_position_raw]

        return tile_map


if __name__ == "__main__":
    scene = scene("map.json")


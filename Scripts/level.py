from Scripts.object import Object as Obj


def tile_map(tile_map_array, image, width, height, collision_list, player, spawn_block):
    tile_map_list = []
    y = 0
    for column in tile_map_array:
        x = 0
        last_loop_count = 0
        last_number = 0
        for row in column.split(","):
            
            if row == "s":
                player.x = x
                player.y = y
                row = str(spawn_block)
                
            tile = Obj(x, y, image[int(row)-1], False)

            tile.collision = collision_list[int(row)-1]
            if last_number == int(row):
                tile.loop += last_loop_count
                tile_map_list.pop()
            tile_map_list.append(tile)
            last_loop_count = tile.loop
            last_number = int(row)
            x += width
        y += height
    return tile_map_list


class Level:
    def __init__(self, name, layout, images, collisions, player, spawn_block):
        self.name = name
        self.layout = layout
        self.images = images
        self.collisions = collisions
        self.player = player
        self.objects = tile_map(self.layout, self.images, 32, 32, self.collisions, self.player, spawn_block)

    def get_objects(self):
        return tile_map(self.layout, self.images, 32, 32, self.collisions, self.player)
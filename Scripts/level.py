from Scripts.object import Object as Obj


def tile_map(tile_map_array, image, width, height, collision_list, spawns=[]):
    tile_map_list = []
    objects = []
    y = 0
    for column in tile_map_array:
        x = 0
        last_loop_count = 0
        last_number = 0
        for row in column.split(","):
            row = row.split("-")

            for tup in spawns:
                if row[0] == tup[0]:
                    if tup[3]:
                        obj = Obj(x, y, tup[1].image, False, tup[1].layer, tup[1].entity)
                        if obj.entity:
                            obj.pygame = tup[1].pygame
                        objects.append(obj)
                    else:
                        obj = tup[1]
                    obj.x = x
                    obj.y = y
                    row[0] = row[1]

            tile = Obj(x, y, image[int(row[0]) - 1], False)

            tile.collision = collision_list[int(row[0]) - 1]
            if last_number == int(row[0]):
                tile.loop += last_loop_count
                tile_map_list.pop()
            tile_map_list.append(tile)
            last_loop_count = tile.loop
            last_number = int(row[0])
            x += width
        y += height
    for block in objects:
        tile_map_list.append(block)
    return tile_map_list


class Level:
    def __init__(self, name, layout, images, collisions, arguments, requirements=0):
        self.name = name
        self.layout = layout
        self.images = images
        self.collisions = collisions
        self.arguments = arguments
        self.requirements = requirements
        self.objects = tile_map(self.layout, self.images, 32, 32, self.collisions, self.arguments)

    def load(self):
        return tile_map(self.layout, self.images, 32, 32, self.collisions, self.arguments)

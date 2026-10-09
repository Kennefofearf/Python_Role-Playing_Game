class Camera:
    def __init__(self, height, width):
        self.y = 0
        self.x = 0
        self.height = height
        self.width = width

    def world_to_screen(self, world_y, world_x, start_y, start_x):
        return (start_y + world_y - self.y,
                start_x + world_x - self.x
                )

    def follow(self, target_y, target_x, map_height, map_width):

        self.y = target_y - self.height // 2
        self.x = target_x - self.width // 2

        max_y = max(0, map_height - self.height)
        max_x = max(0, map_width - self.width)

        self.y = max(0, min(self.y, max_y))
        self.x = max(0, min(self.x, max_x))

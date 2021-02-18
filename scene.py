class Scene:

    def __init__(self, scene):
        self.assets = scene

    def run(self,time_delta):
        self.assets.run(time_delta)

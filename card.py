class Card():
    def __init__(self, name, cost, type, color, image, stars=0, effects={}, status=None):
        self.name = name
        self.cost = cost
        self.type = type
        self.color = color
        self.image = image
        self.stars = stars
        self.effects = effects
        self.status = status
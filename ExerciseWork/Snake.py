class Snake:
    # Initialize the states
    def __init__(self):
        self.x_position = 250
        self.y_position = 250
        self.width = 10
        self.height = 10
        self.direction = 'stop'
        self.speed = 10
        self.body = []
        self.head_color = (153, 204, 255)
        self.body_color = (204, 229, 255)

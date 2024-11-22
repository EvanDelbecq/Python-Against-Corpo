import pygame

class Map:
    def __init__(self, window):
        self.window = window
        self.lines = [
            #Bordures
            ((0, 0), (0, 720)), ((0, 720), (1080, 720)), ((1080, 720), (1080, 0)), ((1080, 0), (0, 0)),
            #Piece1
            ((0, 300), (200, 300)), ((300, 305), (300, 0)),
            #Piece2
            ((300, 300), (1000, 300)),
            #Couloir
            ((540, 300), (540, 450)), ((540, 720), (540, 600))
        ]
        self.thickness = 10

    def draw(self):    
        for start_pos, end_pos in self.lines:
            pygame.draw.line(self.window, 'black', start_pos, end_pos, self.thickness)

    def check_collision(self, rect):
        for start_pos, end_pos in self.lines:
            line_rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                    abs(start_pos[0] - end_pos[0]) or self.thickness,
                                    abs(start_pos[1] - end_pos[1]) or self.thickness)
            if rect.colliderect(line_rect):
                return True, line_rect
        return False, None
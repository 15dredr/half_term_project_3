import pygame
print()
pygame.init()
window_width = 800
window_height = 600
DISPLAY = pygame.display.set_mode((window_width, window_height))
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
width = 20
height = 20


class MyCharacter(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.max_health = 10
        self.attack_damage = 2
        self.move_speed = 20
        self.name = 'name not found'
        self.current_health = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(white)

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def damage_or_healing(self, amount):
        return False

    def update(self, hostile_group, wall_group, direction):
        pass


class MyEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.move_speed = 20

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def update(self, wall_group, hostile_group, direction):
        pass


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.damage = None
        self.mode = None
        self.count = None
        self.move_speed = None
        self.direction = None

    def update(self):
        pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    DISPLAY.fill(black)  # comment

import pygame

pygame.init()
window_width = 800
window_height = 600
DISPLAY = pygame.display.set_mode((window_width, window_height))
FPSCLOCK = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
hero_x_speed = 3
hero_y_speed = 3
hero_colour = green
hero_left = 20
hero_top = 20
hero_width = 20
hero_height = 20
villain_x_speed = 2
villain_y_speed = 2
villain_width = 10
villain_height = 10
villain_colour = red
villain_left = 10
villain_top = 10


class Hero(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.max_health = 10
        self.attack_damage = 2
        self.move_speed = 20
        self.name = 'Hero'
        self.current_health = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(hero_colour)
        self.hero_x_speed = hero_x_speed
        self.hero_y_speed = hero_y_speed

    def collide_hostile_check(self, hostile_group):
        list_of_collied_sprites = []
        if hostile_group.rect.left > self.rect.right > hostile_group.rect.right or hostile_group.rect.left > self.rect.left > hostile_group.rect.right:
            if hostile_group.rect.top < self.rect.top < hostile_group.rect.bottom or hostile_group.rect.top < self.rect.bottom < hostile_group.rect.bottom:
                list_of_collied_sprites.append(hostile_group)
                return (True, [list_of_collied_sprites])
            else:
                return (False, [])
        else:
            return (False, [])

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def damage_or_healing(self, amount):
        return False

    def update(self, hostile_group, wall_group, direction):
        pass


class Villain(pygame.sprite.Sprite):
    def __init__(self, villain_width, villain_height):
        super().__init__()
        self.health = 5
        self.move_speed = 20
        self.villain_x_speed = villain_x_speed
        self.villain_y_speed = villain_y_speed
        self.image = pygame.Surface([villain_width, villain_height])
        self.rect = self.image.get_rect()
        self.image.fill(villain_colour)
        self.villain_x_speed = villain_x_speed
        self.villain_y_speed = villain_y_speed
        self.villain_left = villain_left
        self.villain_top = villain_top

    def collide_wall_check(self, wall_group, direction):
        return (False, None)

    def collide_hostile_check(self, hostile_group):
        return (False, [])

    def update(self, wall_group, hostile_group, direction):
        self.rect.x += self.villain_x_speed
        if self.rect.right >= window_width:
            self.villain_x_speed *= -1
            self.rect.x += self.villain_x_speed
        if self.rect.left <= 0:
            self.villain_x_speed *= -1
            self.rect.x += self.villain_x_speed

        self.rect.y += self.villain_y_speed
        if self.rect.bottom >= window_height:
            self.villain_y_speed *= -1
            self.rect.y += self.villain_y_speed
        if self.rect.top <= 0:
            self.villain_y_speed *= -1
            self.rect.y += self.villain_y_speed

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


mos_pos = pygame.mouse.get_pos()

my_hero = Hero
while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mos_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            quit()

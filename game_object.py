import pygame
from constants import WIN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='chick.png'):
        super().__init__()
        # Загружаем изображение в спрайт
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        # Задаем положение спрайта игрока на экране
        self.rect.x = x
        self.rect.y = y
        # Задаем скорость игрока по x и по y
        self.change_x = 0
        self.change_y = 0
        # Создаем группу препятствий для игрока:
        self.platforms = pygame.sprite.Group()

    def update(self):
        # Движение вправо - влево
        self.rect.x += self.change_x
        # Проверим, что объект не врезается в стену:
        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        for block in block_hit_list:
            # Если игрок двигался вправо, вернем его правую границу к левой границе препятствия:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Если он двигался влево, делаем все наоборот:
                self.rect.left = block.rect.right

        # Движение вверх - вниз
        self.rect.y += self.change_y
        # Проверим, что объект не врезается в стену:
        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        for block in block_hit_list:
            # Вернем игрока за границу препятствия, в которое он врезался:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        self.rect.y -= 2
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= WIN_HEIGHT:
            self.change_y = -10
        
    def go_left(self):
        self.change_x = -6
        
    def go_right(self):
        self.change_x = 6
        
    def stop(self):
        self.change_x = 0
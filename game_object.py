import pygame

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
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
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
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # Вернем игрока за границу препятствия, в которое он врезался:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
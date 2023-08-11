from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed


back = (200, 255, 255)
window = display.set_mode(700, 500)
window.fill(back)
game = True

ball = GameSprite('tenis_bal.png', 200,200, 4, 50,50)

while gaame:
    for e in event.get():
        if e.type ==QUIT:
            game = False
        ball.reset()
        display.update()
        time.delay(10)
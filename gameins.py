import pygame
import sys
import random

pygame.init()

# ================= GAME =================
class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 400, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Falling Blocks")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self.WIDTH // 2, self.HEIGHT - 60)
        self.enemies = []

        self.spawn_timer = 0

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()

        # Spawn de inimigos
        self.spawn_timer += 1
        if self.spawn_timer > 60:  # 1 inimigo por segundo
            self.enemies.append(Enemy(self.WIDTH))
            self.spawn_timer = 0

        # Atualiza inimigos
        for enemy in self.enemies[:]:
            enemy.update()

            # Colisão
            if enemy.rect.colliderect(self.player.rect):
                self.running = False  # game over

            # Remove inimigo que saiu da tela
            if enemy.rect.top > self.HEIGHT:
                self.enemies.remove(enemy)

    def draw(self):
        self.screen.fill((25, 25, 25))
        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        pygame.display.flip()


# ================= PLAYER =================
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 20)
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 255), self.rect)


# ================= ENEMY =================
class Enemy:
    def __init__(self, width):
        x = random.randint(0, width - 40)
        self.rect = pygame.Rect(x, -40, 40, 40)
        self.speed = random.randint(10, 15)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 60, 60), self.rect)


# ================= START =================
if __name__ == "__main__":
    game = Game()
    game.run()

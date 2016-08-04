import pygame, random

pygame.init()
screen = pygame.display.set_mode([1000, 1000], pygame.RESIZABLE)
pygame.display.set_caption("Test")
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    for row in range(100):
        for col in range(100):
            if bool(random.getrandbits(1)):
                pygame.draw.rect(screen, (0, 0, 0), [col*5, row*5, 5, 5])
    pygame.time.Clock().tick(10)
    pygame.display.flip()

pygame.quit()

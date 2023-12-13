import pygame
import random
 
pygame.init()

size = [700, 700]
res = [400, 400]

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

chunk_size = 8
tile_size = 16

textures = {0: [pygame.image.load('0.png')], 
            1: [pygame.image.load('1.png')]}

def generate_tile(x, y, chunk_x, chunk_y):
    tile_x = (chunk_x//tile_size)+x
    tile_y = (chunk_y//tile_size)+y

    return int((chunk_x//chunk_size//tile_size)/2 == 0) 

class Chunk:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.nap = [generate_tile(x, y, self.x, self.y) for y in range(chunk_size) for x in range(chunk_size)]

    def render(self):
        for y in range(chunk_size):
            for x in range(chunk_size):
                texture = textures[self.nap[x+y*chunk_size]][0]
                screen.blit(texture, (self.x+x*tile_size, self.y+y*tile_size)) 

world_size_chunk_y = 3
world_size_chunk_x = 3

chunks = []
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x*chunk_size*tile_size, y*chunk_size*tile_size))


while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for chunk in chunks:
        chunk.render()         

    window.blit(pygame.transform.scale(screen, size), (0, 0))

    pygame.display.update()
    clock.tick(60)
    

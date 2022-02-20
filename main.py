import pygame, sys
from atoms import Carbon
import random
from matplotlib import pyplot as plt

initial_conc = int(input("Enter initial number of atoms: "))
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Radioactivity")
clock = pygame.time.Clock()

carbons = []
nitros = []

concentration = []
TIME = []

for i in range(initial_conc):
    x = random.randint(0, screen_size[0])
    y = random.randint(0, screen_size[1])
    carbons.append(Carbon((x, y)))


def plot(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.title('Concentration Vs Time')
    plt.show()


time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for carbon in carbons:
        if carbon.status == "decayed_and_stable":
            nitros.append(carbon)
            carbons.remove(carbon)
    
    screen.fill([0, 0, 0])
    for carbon in carbons:
        carbon.draw(screen)
    for nitro in nitros:
        nitro.draw(screen)
    
    pygame.display.flip()
    num_c = len(carbons)
    concentration.append(num_c)
    TIME.append(time)
    time += 1
    clock.tick(60)

plot(TIME, concentration)

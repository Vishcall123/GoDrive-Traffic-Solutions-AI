import pygame
import sys
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Load Background")

# Load the existing background image
background_image = pygame.image.load("Intersection.png")  # Replace with your image filename

# Optionally, scale the background to fit the screen
background_image = pygame.transform.scale(background_image, (width, height))

# Blit the background image to the screen
screen.blit(background_image, (0, 0))

#Creating our model class

class Model(nn.Module):
  # Input layer (4 features) -> hidden layer1 (some neuron count) -> hidden layer2 (neurons) -> output (3 classes of Iris)
  def __init__(self, in_features=20, h1 = 40, h2=40, h3=40, h4 =20, out_features=4):
    super().__init__()
    self.fc1 = nn.Linear(in_features, h1)
    self.fc2 = nn.Linear(h1, h2)
    self.dropout = nn.Dropout(p=0.1)
    self.fc3 = nn.Linear(h2, h3)
    self.out = nn.Linear(h3, out_features)

  def forward(self, x):
    x = F.tanh(self.fc1(x))
    x = self.dropout(x)
    x = F.tanh(self.fc2(x))
    x = F.tanh(self.fc3(x))
    x = self.dropout(x)
    x = self.out(x)

    return x


class Connection:
    def __init__(self):
        self.top_center = self.top_right = self.top_left = 7
        self.left_center = self.left_right = self.left_left = 7
        self.bottom_center = self.bottom_right = self.bottom_left = 7
        self.right_center = self.right_right = self.right_left = 7

        #pedestrians
        self.top_east = self.top_west = 7
        self.left_up = self.left_down = 7
        self.bottom_east = self.bottom_west = 7
        self.right_up = self.right_down = 7
        
        #neural network
        self.neural_net = Model()
        self.neural_net.load_state_dict(torch.load("traffic_model.pt", weights_only=True))
    
    def draw(self):
        #draw top cars
        print("DRAWING")
        for i in range(self.top_center):
            pygame.draw.circle(screen, (255, 0, 0), (348, 250 - 24 * i), 10)
        
        for i in range(self.top_right):
            pygame.draw.circle(screen, (255, 0, 0), (318, 250 - 24 * i), 10)

        for i in range(self.top_left):
            pygame.draw.circle(screen, (255, 0, 0), (380, 250 - 24 * i), 10)
        
        #draw left cars
        for i in range(self.left_center):
            pygame.draw.circle(screen, (255, 0, 0), (250 - 24 * i, 452), 10)
        
        for i in range(self.left_right):
            pygame.draw.circle(screen, (255, 0, 0), (250 - 24 * i, 484), 10)

        for i in range(self.left_left):
            pygame.draw.circle(screen, (255, 0, 0), (250 - 24 * i, 420), 10)
        
        #draw bottom cars
        for i in range(self.bottom_center):
            pygame.draw.circle(screen, (255, 0, 0), (452, 550 + 24 * i), 10)
        
        for i in range(self.bottom_right):
            pygame.draw.circle(screen, (255, 0, 0), (484, 550 + 24 * i), 10)

        for i in range(self.bottom_left):
            pygame.draw.circle(screen, (255, 0, 0), (420, 550 + 24 * i), 10)
            
        #draw right cars
        for i in range(self.right_center):
            pygame.draw.circle(screen, (255, 0, 0), (550 + 24 * i, 348), 10)
        
        for i in range(self.right_right):
            pygame.draw.circle(screen, (255, 0, 0), (550 + 24 * i, 318), 10)

        for i in range(self.right_left):
            pygame.draw.circle(screen, (255, 0, 0), (550 + 24 * i, 380), 10)


        #draw top pedestrians    
        pygame.draw.circle(screen, (10 * max(0, self.top_east) + 10, 10 * max(0, self.top_east), 10 * max(0, self.top_east)), (318, 290), 20)
        pygame.draw.circle(screen, (10 * max(0, self.top_west) + 10, 10 * max(0, self.top_west), 10 * max(0, self.top_west)), (482, 290), 20)

        pygame.draw.circle(screen, (10 * max(0, self.bottom_east) + 10, 10 * max(0, self.bottom_east), 10 * max(0, self.bottom_east)), (318, 510), 20)
        pygame.draw.circle(screen, (10 * max(0, self.bottom_west) + 10, 10 * max(0, self.bottom_west), 10 * max(0, self.bottom_west)), (482, 510), 20)

        pygame.draw.circle(screen, (10 * max(0, self.left_up) + 10, 10 * max(0, self.left_up), 10 * max(0, self.left_up)), (290, 486), 20)
        pygame.draw.circle(screen, (10 * max(0, self.left_down) + 10, 10 * max(0, self.left_down), 10 * max(0, self.left_down)), (290, 316), 20)

        pygame.draw.circle(screen, (10 * max(0, self.right_up) + 10, 10 * max(0, self.right_up), 10 * max(0, self.right_up)), (510, 486), 20)
        pygame.draw.circle(screen, (10 * max(0, self.right_down) + 10, 10 * max(0, self.right_down), 10 * max(0, self.right_down)), (510, 316), 20)

        
    def update(self):
        random_state = 0
        tensor_info = torch.tensor([max(0, float(self.top_right)), max(0, float(self.top_center)), max(0, float(self.top_left)), max(0, float(self.left_left)), max(0, float(self.left_center)), max(0, float(self.left_right)), max(0, float(self.bottom_left)), max(0, float(self.bottom_center)), max(0, float(self.bottom_right)), max(0, float(self.right_right)), max(0, float(self.right_center)), max(0, float(self.right_left)), max(0, float(self.right_up)), max(0, float(self.left_up)), max(0, float(self.left_down)), max(0, float(self.right_down)), max(0, float(self.top_west)), max(0, float(self.top_east)), max(0, float(self.bottom_east)), max(0, float(self.bottom_west))])
        with torch.no_grad():
            random_state = int(self.neural_net.forward(tensor_info).argmax().item())
        #north/south = 0
        #east/west = 1
        #east/west left = 2
        #north/south left = 3
        if random_state == 0:
            #cars
            self.top_center -= 1
            self.top_right -= 1
            self.bottom_right -=1
            self.bottom_center -= 1
            self.right_right -= 1
            self.left_right -= 1

            #pedestrians
            self.left_down -= 1
            self.right_down -= 1
            self.right_up -= 1
            self.left_up -= 1
        elif random_state == 1:
            #cars
            self.left_center -= 1
            self.left_right -= 1
            self.right_center -= 1
            self.right_right -= 1
            self.top_right -= 1
            self.bottom_right -= 1

            #pedestrians
            self.top_east -= 1
            self.top_west -=1
            self.bottom_east -= 1
            self.bottom_west -= 1

        elif random_state == 2:
            self.right_left -= 1
            self.left_left -= 1

        elif random_state == 3:
            self.top_left -= 1
            self.bottom_left -= 1
        
    def all_zeroes(self):
        return all(
                getattr(self, var) <= 0 for var in [
                    'top_right', 'top_center', 'top_left', 'left_left', 'left_center', 'left_right', 'bottom_left', 'bottom_center',
                    'bottom_right', 'right_right', 'right_center', 'right_left', 'right_up', 'left_up', 'left_down', 'right_down',
                    'top_west', 'top_east', 'bottom_east', 'bottom_west'
                ]
            )           


x = Connection()
total_frames  = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update the display
    x.update()
    time.sleep(1)
    screen.blit(background_image, (0, 0))
    x.draw()

    pygame.display.flip()
    total_frames += 1
    if x.all_zeroes():
        break


print("The model ran for: " + str(total_frames))

# import matplotlib.pyplot as plt
# from ale_py import ALEInterface, roms
# import keyboard
# import time

# # Initialize ALE and load the game ROM
# ale = ALEInterface()
# ale.loadROM(roms.get_rom_path("pong"))

# # Set up a matplotlib figure for visual feedback
# plt.ion()
# fig, ax = plt.subplots()
# screen_obs = ale.getScreenRGB()
# img = ax.imshow(screen_obs)

# # Get the minimal action set and identify the actions for up and down
# actions = ale.getMinimalActionSet()
# move_up = actions[2]  # Assumes action 2 is 'move up'
# move_down = actions[3]  # Assumes action 3 is 'move down'
# noop = actions[0]  # No operation

# # Game loop for manual control
# for _ in range(1000):  # Adjust steps as desired
#     # Check for key press and decide action
#     keyboard.add_hotkey('w', lambda: None)  # Workaround for keyboard.is_pressed() bug
    
#     if keyboard.is_pressed('w'):
#         action = move_up
#     # elif keyboard.is_pressed('s'):  # Press 'S' to move down
#     #     action = move_down
#     else:
#         action = noop  # No action if no key is pressed

#     # Execute action and update screen
#     reward = ale.act(action)
#     screen_obs = ale.getScreenRGB()
#     img.set_data(screen_obs)
#     fig.canvas.draw()
#     fig.canvas.flush_events()
    
#     time.sleep(0.02)  # Control game speed

# plt.ioff()
# plt.show()




# import pygame
# from ale_py import ALEInterface, roms
# import numpy as np

# # Initialize ALE and load the game ROM
# ale = ALEInterface()
# ale.loadROM(roms.get_rom_path("pong"))

# # Initialize pygame and set up display
# pygame.init()
# width, height = 160, 210  # Typical dimensions for ALE Pong
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Pong - Manual Control")

# # Get the minimal action set and identify actions for up and down
# actions = ale.getMinimalActionSet()
# print(actions)
# right = actions[2]  # Assumes action 2 is 'move up'
# left = actions[3]  # Assumes action 3 is 'move down'
# noop = actions[0]  # No operation

# # Define a clock to cap the frame rate
# clock = pygame.time.Clock()
# fps = 30  # Set to a reasonable frame rate

# # Game loop for manual control
# running = True
# while running:
#     action = noop  # Default to no action each frame

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:  # Press 'W' to move up
#                 action = right
#             elif event.key == pygame.K_s:  # Press 'S' to move down
#                 action = left

#     # Take action and update the game
#     ale.act(action)
#     screen_obs = ale.getScreenRGB()  # Get the latest frame in RGB

#     # Render the frame in pygame
#     surface = pygame.surfarray.make_surface(np.flipud(screen_obs))  # Flip image vertically
#     screen.blit(surface, (0, 0))
#     pygame.display.flip()

#     # Cap the frame rate
#     clock.tick(fps)

# pygame.quit()


import matplotlib.pyplot as plt
from ale_py import ALEInterface, roms
import time

# Initialize ALE and load the game ROM
ale = ALEInterface()
ale.loadROM(roms.get_rom_path("pong"))

# Set up a matplotlib figure for visual feedback
plt.ion()
fig, ax = plt.subplots()
screen_obs = ale.getScreenRGB()
img = ax.imshow(screen_obs)

# Get the minimal action set and find the index for up and down actions
actions = ale.getMinimalActionSet()
move_up = actions[2]  # Assuming action 2 is 'move up'
move_down = actions[3]  # Assuming action 3 is 'move down'

# Play the game with simple control logic
for _ in range(1000):  # Play for 1000 steps
    # Get the screen and use basic image analysis to track the ball and paddle
    screen_obs = ale.getScreenGrayscale()
    
    # Example logic to control paddle based on ball position
    paddle_y = ale.getRAM()[51]  # Approximate position of the paddle (might vary by ROM)
    ball_y = ale.getRAM()[49]    # Approximate position of the ball (might vary by ROM)
    
    if paddle_y < ball_y:  # Ball is below paddle
        action = move_down
    elif paddle_y > ball_y:  # Ball is above paddle
        action = move_up
    else:
        action = 0  # No operation if aligned (optional)

    # Take action and observe reward
    reward = ale.act(action)
    
    # Update the display with the new frame
    screen_obs = ale.getScreenRGB()
    img.set_data(screen_obs)
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    time.sleep(0.02)  # Control game speed

plt.ioff()
plt.show()

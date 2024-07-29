import pygame

# Initialize Pygame
pygame.init()

# Check if there are any joysticks connected
if pygame.joystick.get_count() > 0:
    # Initialize first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick '{joystick.get_name()}' initialized.")
else:
    print("No joystick connected.")

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Joystick Event Handling")

running = True

# Main event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Joystick button {event.button} pressed.")

        elif event.type == pygame.JOYBUTTONUP:
            print(f"Joystick button {event.button} released.")

# Quit Pygame
pygame.quit()

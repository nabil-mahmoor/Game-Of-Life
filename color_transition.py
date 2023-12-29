import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smooth Color Transition")

# Define colors
colors = {
    '0': (0, 0, 0),
    '1': (72, 202, 228),
    '2': (0, 180, 216),
    '3': (0, 150, 199),
    '4': (0, 119, 182),
    '5': (63, 55, 201),
    '6': (72, 12, 168),
    '7': (58, 12, 163),
    '8': (3, 4, 94)
}

color_len = len(colors)

# Define transition duration (in frames)
transition_duration = 30

clock = pygame.time.Clock()

def lerp_color(color1, color2, alpha):
    """
    Linear interpolation between two colors.
    """
    r = int(color1[0] + alpha * (color2[0] - color1[0]))
    g = int(color1[1] + alpha * (color2[1] - color1[1]))
    b = int(color1[2] + alpha * (color2[2] - color1[2]))
    return r, g, b

def main():
    frame_count = 0
    index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate alpha value for interpolation (0 to 1)
        alpha = min(frame_count / transition_duration, 1.0)

        # Interpolate between start_color and end_color
        current_color = lerp_color(colors[str(index % color_len)], colors[str((index + 1) % color_len)], alpha)
    
        screen.fill(current_color)

        frame_count += 1

        # Check if transition is complete
        if frame_count > transition_duration:
            frame_count = 0
            index += 1

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
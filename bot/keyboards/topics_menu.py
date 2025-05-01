import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Theme Selection Menu")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Menu options
menu_options = ["Theme 1", "Theme 2", "Theme 3"]
selected_option = 0

def draw_menu():
    screen.fill(BG_COLOR)
    for i, option in enumerate(menu_options):
        color = TEXT_COLOR if i == selected_option else (100, 100, 100)
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
        screen.blit(text, text_rect)
    pygame.display.flip()

def main():
    global selected_option
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    print(f"Selected: {menu_options[selected_option]}")
                    # Add code to handle theme selection here

        draw_menu()
        clock.tick(30)

if __name__ == "__main__":
    main()
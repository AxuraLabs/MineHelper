import pygame
import sys

class MineHelper:
    def __init__(self):
        self.hints = [
            {
                "title": "1. Start by collecting basic resources",
                "details": [
                    "Punch trees to gather wood.",
                    "Craft wooden planks and sticks.",
                    "Collect stone from the ground or hillsides."
                ]
            },
            {
                "title": "2. Craft essential tools",
                "details": [
                    "Make a crafting table with wood planks.",
                    "Craft a wooden pickaxe and other tools.",
                    "Upgrade to stone tools as soon as possible."
                ]
            },
            {
                "title": "3. Build a simple shelter",
                "details": [
                    "Use wood, dirt, or stone to create walls and a roof.",
                    "Ensure your shelter is fully enclosed.",
                    "Place torches inside to prevent monster spawns."
                ]
            },
            {
                "title": "4. Explore to find coal and iron ores",
                "details": [
                    "Look for exposed stone areas or caves.",
                    "Coal is often found around stone surfaces.",
                    "Iron can be mined with a stone pickaxe."
                ]
            },
            {
                "title": "5. Craft armor and better tools",
                "details": [
                    "Smelt iron ores to create iron ingots.",
                    "Craft iron armor and tools for better durability.",
                    "Remember to always have backup tools."
                ]
            },
            {
                "title": "6. Begin farming and taming animals",
                "details": [
                    "Craft a hoe to till soil for planting crops.",
                    "Use seeds to plant wheat and other crops.",
                    "Tame animals with their favorite foods (e.g., seeds for chickens)."
                ]
            },
            {
                "title": "7. Explore deeper to find diamonds",
                "details": [
                    "Mine down to levels 11-12 for best diamond ores.",
                    "Use an iron pickaxe or better!",
                    "Be cautious of lava pockets."
                ]
            },
            {
                "title": "8. Prepare for the Nether",
                "details": [
                    "Gather obsidian to create a Nether Portal.",
                    "Light the portal with flint and steel.",
                    "Prepare your gear for a difficult environment."
                ]
            },
            {
                "title": "9. Build potions for combat advantage",
                "details": [
                    "Find blaze rods and nether wart in the Nether.",
                    "Craft a brewing stand and start brewing potions.",
                    "Focus on healing, fire resistance, and strength potions."
                ]
            },
            {
                "title": "10. Find and activate the End Portal",
                "details": [
                    "Locate a stronghold using Eye of Ender.",
                    "Place Eyes of Ender into portal frames to activate.",
                    "Ensure you have ample supplies before entry."
                ]
            },
            {
                "title": "11. Defeat the Ender Dragon",
                "details": [
                    "Bring many arrows and a bow.",
                    "Destroy the Ender Crystals to weaken the dragon.",
                    "Once Ender Crystals are gone, attack the dragon."
                ]
            },
            {
                "title": "12. Explore the End cities for high-level loot",
                "details": [
                    "Use end gateways to reach end cities.",
                    "Find and raid the End cities for valuable items.",
                    "Beware of shulkers and keep your gear ready."
                ]
            }
        ]
        self.current_hint_index = 0

    def next_hint(self):
        if self.current_hint_index < len(self.hints) - 1:
            self.current_hint_index += 1
        else:
            self.current_hint_index = 0  # Loop back to start

    def get_current_hint(self):
        return self.hints[self.current_hint_index]

def draw_button(screen, text, position, size=(200, 50)):
    """
    Draw a button on the screen with specified text, position, and size
    """
    font = pygame.font.Font(None, 36)
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, (0, 128, 0), button_rect)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))
    return button_rect

def draw_hint(screen, hint, position):
    """
    Draw the current hint on the screen
    """
    font = pygame.font.Font(None, 28)
    title_surface = font.render(hint['title'], True, (255, 255, 255))
    screen.blit(title_surface, position)
    
    detail_font = pygame.font.Font(None, 24)
    for i, detail in enumerate(hint['details']):
        detail_surface = detail_font.render(f"- {detail}", True, (255, 255, 255))
        screen.blit(detail_surface, (position[0], position[1] + 30 + i * 30))

def minecraft_helper_loop():
    """
    Main loop for the Minecraft helper
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("MineHelper")
    
    mine_helper = MineHelper()
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    mine_helper.next_hint()

        screen.fill((50, 50, 50))
        button_rect = draw_button(screen, "Next Hint", (300, 500))
        current_hint = mine_helper.get_current_hint()
        draw_hint(screen, current_hint, (50, 50))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    minecraft_helper_loop()
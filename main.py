import pygame, sys
from settings import *
from level import Level
from support import resource_path

class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        icon = pygame.image.load(resource_path("graphics\player\down\down_0.png"))
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)

        # game states
        self.game_over = False
        self.game_win = False

        self.title_font = pygame.font.Font(UI_FONT, 90)
        self.info_font = pygame.font.Font(UI_FONT, 40)

    def draw_game_over(self):
        # texts
        title = self.title_font.render("Player Dead!",True,(255,50,50))
        info = self.info_font.render("Press any key to restart the game",True,('white'))

        title_rect = title.get_rect(center = (WIDTH//2, HEIGHT//2 - 50))
        info_rect = info.get_rect(center = (WIDTH//2, HEIGHT//2 + 40))

        # title box
        pygame.draw.rect(self.screen, UI_BG_COLOR, title_rect.inflate(50,30))
        pygame.draw.rect(self.screen, UI_BORDER_COLOR,title_rect.inflate(50,30),3)

        # info box
        pygame.draw.rect(self.screen, UI_BG_COLOR, info_rect.inflate(40,20))
        pygame.draw.rect(self.screen, UI_BORDER_COLOR,info_rect.inflate(40,20),2)

        self.screen.blit(title,title_rect)
        self.screen.blit(info,info_rect)

    def draw_game_win(self):
        # texts
        title = self.title_font.render("YOU WIN!", True, (50, 255, 50))
        info = self.info_font.render("Press any key to play again", True, ("white"))

        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        info_rect = info.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))

        # title box
        pygame.draw.rect(self.screen, UI_BG_COLOR, title_rect.inflate(50,30))
        pygame.draw.rect(self.screen, UI_BORDER_COLOR, title_rect.inflate(50,30), 3)

        # info box
        pygame.draw.rect(self.screen, UI_BG_COLOR, info_rect.inflate(40,20))
        pygame.draw.rect(self.screen, UI_BORDER_COLOR, info_rect.inflate(40,20), 2)

        self.screen.blit(title, title_rect)
        self.screen.blit(info, info_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if (self.game_over or self.game_win) and event.type == pygame.KEYDOWN:
                    self.level = Level()
                    self.game_over = False
                    self.game_win = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            if not self.game_over and not self.game_win:
                self.screen.fill(WATER_COLOR)
                self.level.run()

                if self.level.player.health <= 0:
                    self.game_over = True

                elif self.level.all_enemies_defeated():
                    self.game_win = True

            elif self.game_over:
                self.draw_game_over()

            elif self.game_win:
                self.draw_game_win()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
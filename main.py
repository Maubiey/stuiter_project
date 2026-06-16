import sys
import pygame

SCHERM_BREEDTE = 600
SCHERM_HOOGTE  = 700
FPS            = 60
TITEL          = "DodgeBlitz"

WIT         = (255, 255, 255)
ZWART       = (  0,   0,   0)
ORANJE      = (230, 100,   0)
GRIJS       = (160, 160, 160)
DONKERGRIJS = ( 60,  60,  60)
BG_MENU     = ( 10,  10,  30)
BG_SPEL     = (240, 240, 245)

SPELER_BREEDTE  = 28
SPELER_HOOGTE   = 28
SPELER_SNELHEID = 6
SPELER_START_X  = SCHERM_BREEDTE // 2
SPELER_START_Y  = SCHERM_HOOGTE - 60
SPELER_KLEUR    = (50, 110, 220)

class Speler:

    def __init__(self):
        self.x = SPELER_START_X - SPELER_BREEDTE // 2
        self.y = SPELER_START_Y
        self.breedte  = SPELER_BREEDTE
        self.hoogte   = SPELER_HOOGTE
        self.snelheid = SPELER_SNELHEID

    def verwerk_invoer(self, toetsen):
        if toetsen[pygame.K_LEFT] or toetsen[pygame.K_a]:
            self.x -= self.snelheid

        if toetsen[pygame.K_RIGHT] or toetsen[pygame.K_d]:
            self.x += self.snelheid

        if self.x < 0:
            self.x = 0
        if self.x + self.breedte > SCHERM_BREEDTE:
            self.x = SCHERM_BREEDTE - self.breedte

    def reset(self):
        self.x = SPELER_START_X - SPELER_BREEDTE // 2
        self.y = SPELER_START_Y

    def teken(self, scherm):
        pygame.draw.rect(
            scherm, SPELER_KLEUR,
            (self.x, self.y, self.breedte, self.hoogte),
            border_radius=4,
        )
        pygame.draw.rect(
            scherm, ZWART,
            (self.x, self.y, self.breedte, self.hoogte),
            2, border_radius=4,
        )

pygame.init()
scherm = pygame.display.set_mode((SCHERM_BREEDTE, SCHERM_HOOGTE))
pygame.display.set_caption(TITEL)
klok = pygame.time.Clock()

font_titel  = pygame.font.SysFont("Arial", 52, bold=True)
font_middel = pygame.font.SysFont("Arial", 28)
font_mini   = pygame.font.SysFont("Arial", 15)

MENU   = "menu"
SPELEN = "spelen"

toestand = MENU

speler = Speler()

def teken_menu(scherm):
    scherm.fill(BG_MENU)

    titel = font_titel.render("DODGEBLITZ", True, ORANJE)
    scherm.blit(titel, (SCHERM_BREEDTE // 2 - titel.get_width() // 2, 130))

    pygame.draw.line(scherm, ORANJE, (80, 225), (SCHERM_BREEDTE - 80, 225), 2)

    opties = [
        ("SPELEN",    WIT,   "ENTER"),
        ("AFSLUITEN", GRIJS, "ESC"),
    ]
    for i, (label, kleur, toets) in enumerate(opties):
        y = 280 + i * 80

        optie = font_middel.render(label, True, kleur)
        scherm.blit(optie, (SCHERM_BREEDTE // 2 - optie.get_width() // 2, y))

        hint = font_mini.render(f"[{toets}]", True, DONKERGRIJS)
        scherm.blit(hint, (SCHERM_BREEDTE // 2 + optie.get_width() // 2 + 10, y + 7))

def teken_spel(scherm):
    scherm.fill(BG_SPEL)

    speler.teken(scherm)

    esc_txt = font_mini.render("ESC = Menu", True, GRIJS)
    scherm.blit(esc_txt, (SCHERM_BREEDTE // 2 - esc_txt.get_width() // 2, SCHERM_HOOGTE - 22))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if toestand == MENU:
                if event.key == pygame.K_RETURN:
                    speler.reset()
                    toestand = SPELEN
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif toestand == SPELEN:
                if event.key == pygame.K_ESCAPE:
                    toestand = MENU

    if toestand == SPELEN:
        ingedrukte_toetsen = pygame.key.get_pressed()
        speler.verwerk_invoer(ingedrukte_toetsen)

    if toestand == MENU:
        teken_menu(scherm)

    elif toestand == SPELEN:
        teken_spel(scherm)

    pygame.display.flip()
    klok.tick(FPS)
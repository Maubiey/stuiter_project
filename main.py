import sys
import pygame

SCHERM_BREEDTE = 600
SCHERM_HOOGTE  = 700
FPS            = 60
TITEL          = "DodgeBlitz"

WIT         = (255, 255, 255)
ORANJE      = (230, 100,   0)
GRIJS       = (160, 160, 160)
DONKERGRIJS = ( 60,  60,  60)
BG_MENU     = ( 10,  10,  30)
BG_SPEL     = (240, 240, 245)

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

def teken_menu(scherm):
    scherm.fill(BG_MENU)

    titel = font_titel.render("DODGEBLITZ", True, ORANJE)
    scherm.blit(titel, (SCHERM_BREEDTE // 2 - titel.get_width() // 2, 130))
  
    pygame.draw.line(scherm, ORANJE, (80, 225), (SCHERM_BREEDTE - 80, 225), 2)

    # ITERATIE: teken elke menuoptie
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
                    toestand = SPELEN
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif toestand == SPELEN:
                if event.key == pygame.K_ESCAPE:
                    toestand = MENU

    if toestand == MENU:
        teken_menu(scherm)

    elif toestand == SPELEN:
        teken_spel(scherm)

    pygame.display.flip()
    klok.tick(FPS)
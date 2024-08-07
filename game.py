import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR_ECRAN, HAUTEUR_ECRAN = 800, 600
FPS = 60
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLEU_FONCE = (0, 0, 128)
BLEU_CLAIR = (173, 216, 230)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
GRIS = (200, 200, 200)
TRANSPARENT = (0, 0, 0, 0)

# Création de l'écran
ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("Space Invaders")
horloge = pygame.time.Clock()

# Variables globales
plein_ecran = False
debug_mode = True
debug_overlay_visible = False
debug_invincible = False
debug_rapid_fire = False
creation_mode_ennemi = False
creation_mode_allie = False
derniere_tir = 0
RAPID_FIRE_INTERVALLE = 200
TEMPS_REAPPARITION_ENNNEMIS = 5000
INTERVALLE_TIR_ALLIE = 500
INTERVALLE_TIR_ENNEMI = 1000  # Réduit pour des tirs plus fréquents

# Groupes de sprites
tous_les_sprites = pygame.sprite.Group()
ennemis = pygame.sprite.Group()
allies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Fonction pour afficher le texte
def afficher_texte(texte, position, couleur=BLANC, taille=36):
    police = pygame.font.Font(None, taille)
    surface_texte = police.render(texte, True, couleur)
    ecran.blit(surface_texte, position)

# Fonction pour afficher un bouton
def afficher_bouton(texte, position, couleur_fond, couleur_texte):
    police = pygame.font.Font(None, 36)
    surface_texte = police.render(texte, True, couleur_texte)
    rect_bouton = pygame.Rect(position[0], position[1], 200, 50)
    pygame.draw.rect(ecran, couleur_fond, rect_bouton, border_radius=10)
    pygame.draw.rect(ecran, couleur_texte, rect_bouton, 2, border_radius=10)  # Bordure du bouton
    ecran.blit(surface_texte, (position[0] + 10, position[1] + 10))
    return rect_bouton

# Classe Joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLANC)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGEUR_ECRAN / 2
        self.rect.bottom = HAUTEUR_ECRAN - 10
        self.vitesse = 5

    def update(self):
        global derniere_tir
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            self.rect.x -= self.vitesse
        if touches[pygame.K_RIGHT]:
            self.rect.x += self.vitesse
        if touches[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if debug_rapid_fire and (now - derniere_tir > RAPID_FIRE_INTERVALLE):
                self.tirer()
                derniere_tir = now
            elif not debug_rapid_fire and (now - derniere_tir > INTERVALLE_TIR_ALLIE):
                self.tirer()
                derniere_tir = now

    def tirer(self):
        projectile = ProjectileAllie(self.rect.centerx, self.rect.top - 10)  # Position ajustée
        projectiles.add(projectile)
        tous_les_sprites.add(projectile)



# Classe Ennemi
class Ennemi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(ROUGE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGEUR_ECRAN - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.vitesse = 2
        self.vitesse_initiale = 2
        self.derniere_tir = pygame.time.get_ticks()
        self.tir_en_cours = False

    def update(self):
        if self.tir_en_cours:
            self.rect.y += self.vitesse_initiale * 0.25
        else:
            self.rect.y += self.vitesse

        if self.rect.y > HAUTEUR_ECRAN:
            self.kill()
            return

        now = pygame.time.get_ticks()
        if now - self.derniere_tir > INTERVALLE_TIR_ENNEMI:
            self.tir_en_cours = True
            projectile = ProjectileEnnemi(self.rect.centerx, self.rect.bottom + 10)  # Position ajustée
            projectiles.add(projectile)
            tous_les_sprites.add(projectile)
            self.derniere_tir = now
            pygame.time.set_timer(pygame.USEREVENT, 500)
        else:
            self.tir_en_cours = False


# Classe Allie
class Allie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(VERT)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGEUR_ECRAN - self.rect.width)
        self.rect.y = random.randint(0, HAUTEUR_ECRAN // 2)
        self.vitesse = 2
        self.tirs = pygame.sprite.Group()
        self.derniere_tir = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.vitesse
        if self.rect.left < 0 or self.rect.right > LARGEUR_ECRAN:
            self.vitesse = -self.vitesse

        now = pygame.time.get_ticks()
        if now - self.derniere_tir > INTERVALLE_TIR_ALLIE:
            projectile = ProjectileAllie(self.rect.centerx, self.rect.top - 10)  # Position ajustée
            self.tirs.add(projectile)
            projectiles.add(projectile)
            tous_les_sprites.add(projectile)
            self.derniere_tir = now

        # Détection des collisions avec les projectiles ennemis
        collisions_allies = pygame.sprite.groupcollide(self.tirs, ennemis, False, True)
        if collisions_allies:
            self.kill()

# Classe Projectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, couleur=BLANC, origine='joueur', direction=1):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(couleur)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.vitesse = 10
        self.origine = origine
        self.direction = direction

    def update(self):
        self.rect.y -= self.vitesse * self.direction
        if self.rect.bottom < 0 or self.rect.top > HAUTEUR_ECRAN:
            self.kill()

        # Afficher les hitboxes pour le débogage
        if debug_overlay_visible:
            pygame.draw.rect(ecran, (0, 255, 0), self.rect, 2)

# Classes pour les projectiles des ennemis et alliés
class ProjectileEnnemi(Projectile):
    def __init__(self, x, y):
        super().__init__(x, y, couleur=ROUGE, origine='ennemi', direction=-1)  # Direction vers le bas

class ProjectileAllie(Projectile):
    def __init__(self, x, y):
        super().__init__(x, y, couleur=VERT, origine='allie', direction=1)  # Direction vers le haut

# Fonction pour afficher un overlay de débogage
def afficher_overlay_debug():
    cadre_debug = pygame.Rect(10, 10, 300, 200)
    pygame.draw.rect(ecran, GRIS, cadre_debug, 2)
    pygame.draw.rect(ecran, NOIR, cadre_debug.inflate(-2, -2))
    
    afficher_texte(f"DEBUG MODE: {'ACTIVÉ' if debug_mode else 'DÉSACTIVÉ'}", (20, 20), GRIS, 24)
    afficher_texte(f"PLEIN ECRAN: {'ACTIVÉ' if plein_ecran else 'DÉSACTIVÉ'}", (20, 50), GRIS, 24)
    afficher_texte(f"INVINCIBLE: {'ACTIVÉ' if debug_invincible else 'DÉSACTIVÉ'}", (20, 80), GRIS, 24)
    afficher_texte(f"TIR RAPIDE: {'ACTIVÉ' if debug_rapid_fire else 'DÉSACTIVÉ'}", (20, 110), GRIS, 24)
    afficher_texte(f"CRÉATION ENNEMI: {'ACTIVÉ' if creation_mode_ennemi else 'DÉSACTIVÉ'}", (20, 140), GRIS, 24)
    afficher_texte(f"CRÉATION ALLIE: {'ACTIVÉ' if creation_mode_allie else 'DÉSACTIVÉ'}", (20, 170), GRIS, 24)

# Fonction pour afficher l'écran de Game Over
def ecran_game_over():
    ecran.fill(BLEU_FONCE)
    afficher_texte("GAME OVER", (LARGEUR_ECRAN / 2 - 150, HAUTEUR_ECRAN / 2 - 50), ROUGE, 64)
    afficher_texte("Appuyez sur ESC pour quitter", (LARGEUR_ECRAN / 2 - 200, HAUTEUR_ECRAN / 2 + 20), BLANC, 36)
    pygame.display.flip()

    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Fonction pour gérer la boucle principale du jeu
def boucle_principale():
    global debug_mode, debug_overlay_visible, debug_invincible, debug_rapid_fire, plein_ecran
    global creation_mode_ennemi, creation_mode_allie

    joueur = Joueur()
    tous_les_sprites.add(joueur)

    pygame.time.set_timer(pygame.USEREVENT + 1, TEMPS_REAPPARITION_ENNNEMIS)

    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_F11:
                    plein_ecran = not plein_ecran
                    if plein_ecran:
                        ecran_mode = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN), pygame.FULLSCREEN)
                    else:
                        ecran_mode = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
                    global ecran
                    ecran = ecran_mode
                elif evenement.key == pygame.K_p:
                    debug_mode = not debug_mode
                    debug_overlay_visible = debug_mode  # Afficher l'overlay lorsque le mode debug est activé
                elif evenement.key == pygame.K_i:
                    debug_invincible = not debug_invincible
                elif evenement.key == pygame.K_r:
                    debug_rapid_fire = not debug_rapid_fire
                elif evenement.key == pygame.K_e:
                    creation_mode_ennemi = not creation_mode_ennemi
                elif evenement.key == pygame.K_a:
                    creation_mode_allie = not creation_mode_allie

            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if creation_mode_ennemi:
                    position = pygame.mouse.get_pos()
                    ennemi = Ennemi()
                    ennemi.rect.center = position
                    ennemis.add(ennemi)
                    tous_les_sprites.add(ennemi)
                elif creation_mode_allie:
                    position = pygame.mouse.get_pos()
                    allie = Allie()
                    allie.rect.center = position
                    allies.add(allie)
                    tous_les_sprites.add(allie)

            elif evenement.type == pygame.USEREVENT + 1:
                ennemi = Ennemi()
                ennemis.add(ennemi)
                tous_les_sprites.add(ennemi)

        # Mise à jour des sprites
        tous_les_sprites.update()

        # Vérifier si le joueur est mort
        if not debug_invincible and pygame.sprite.spritecollideany(joueur, projectiles):
            ecran_game_over()
            return  # Quitter la boucle principale pour retourner à l'écran titre ou quitter le jeu

        # Vérifier si un allié est mort
        for allie in allies:
            if pygame.sprite.spritecollide(any(allie, projectiles), ennemis, False):
                allie.kill()

        # Détection des collisions entre les projectiles du joueur et les ennemis
        collisions = pygame.sprite.groupcollide(projectiles, ennemis, True, True)
        if collisions:
            for ennemis_tues in collisions.values():
                for ennemi in ennemis_tues:
                    ennemi.kill()

        # Affichage
        ecran.fill(TRANSPARENT)  # Aucun arrière-plan coloré
        tous_les_sprites.draw(ecran)

        # Affichage de l'overlay de débogage
        if debug_overlay_visible:
            afficher_overlay_debug()

        pygame.display.flip()
        horloge.tick(FPS)
# Fonction pour afficher l'écran titre
def ecran_titre():
    while True:
        ecran.fill(BLEU_FONCE)
        afficher_texte("SPACE INVADERS", (LARGEUR_ECRAN / 2 - 150, HAUTEUR_ECRAN / 2 - 100), BLANC, 64)
        rect_bouton_jouer = afficher_bouton("Jouer", (LARGEUR_ECRAN / 2 - 100, HAUTEUR_ECRAN / 2), BLEU_CLAIR, BLANC)
        rect_bouton_quitter = afficher_bouton("Quitter", (LARGEUR_ECRAN / 2 - 100, HAUTEUR_ECRAN / 2 + 60), BLEU_CLAIR, BLANC)
        pygame.display.flip()

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if rect_bouton_jouer.collidepoint(evenement.pos):
                    return  # Quitter l'écran titre et démarrer le jeu
                elif rect_bouton_quitter.collidepoint(evenement.pos):
                    pygame.quit()
                    sys.exit()

# Lancer le jeu
ecran_titre()
boucle_principale()
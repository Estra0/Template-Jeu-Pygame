# Space Invaders

Space Invaders est un jeu d'arcade classique développé en Python avec la bibliothèque Pygame. Dans ce jeu, vous contrôlez un vaisseau spatial et devez défendre la Terre contre une invasion d'ennemis extraterrestres. Le jeu propose des mécaniques de tir, des ennemis qui descendent lentement vers le bas de l'écran, et des alliés qui vous aideront dans votre mission.

## Fonctionnalités

- **Contrôles** :
  - **Flèches gauche/droite** : Déplacez le vaisseau spatial.
  - **Barre d'espace** : Tire des projectiles.
  - **Ctrl + P** : Ouvre/ferme le menu de débogage.

- **Gameplay** :
  - **Vaisseau spatial** : Déplacez-vous horizontalement et tirez pour éliminer les ennemis.
  - **Ennemis** : Ils descendent lentement et tirent des projectiles vers le bas.
  - **Alliés** : Des alliés peuvent apparaître et tirer des projectiles pour aider le joueur.
  - **Projectiles** : Les projectiles du joueur et des ennemis peuvent interagir et provoquer des destructions.

- **Modes de Jeu** :
  - **Mode Invincible** : Rendre le joueur invincible aux projectiles ennemis.
  - **Tir Rapide** : Permet au joueur de tirer plus rapidement.
  - **Création d'Ennemis** : Les ennemis peuvent être créés en cliquant avec la souris si le mode est activé.
  - **Création d'Alliés** : Les alliés peuvent être créés en cliquant avec la souris si le mode est activé.

## Menu de Débogage

Le jeu inclut un menu de débogage accessible via la combinaison de touches **Ctrl + P**. Ce menu vous permet de :

- **Activer/Désactiver le mode débogage**.
- **Activer/Désactiver le plein écran**.
- **Activer/Désactiver la visibilité du menu de débogage**.
- **Activer/Désactiver l'invincibilité du joueur**.
- **Activer/Désactiver le tir rapide du joueur**.
- **Activer/Désactiver la création d'ennemis via la souris**.
- **Activer/Désactiver la création d'alliés via la souris**.
- **Revenir au menu principal**.

## Installation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/votre-utilisateur/space-invaders.git
   cd space-invaders



2. **Installer les dépendances** :

```bash
pip install pygame

```

3. **Exécuter le jeu** :

```bash
python game.py
```

## Compilation en Exécutable

1. **Installer PyInstaller** :
```bash
pip install pyinstaller
```

2. **Générer l'exécutable** :
```bash
pyinstaller --onefile --windowed game.py
```

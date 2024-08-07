# Space Invaders

Space Invaders est un prototype de jeu d'arcade développé en Python avec la bibliothèque Pygame. Ce jeu est un prototype simple utilisant des figures géométriques de base pour représenter les éléments du jeu, tels que les vaisseaux, les ennemis, et les projectiles. L'objectif est de défendre la Terre contre une invasion extraterrestre.

## Fonctionnalités

- **Contrôles** :
  - **Flèches gauche/droite** : Déplacez le vaisseau spatial.
  - **Barre d'espace** : Tire des projectiles.

- **Modes de Jeu** :
  - **Invincibilité** : Le joueur ne peut pas être touché par les projectiles ennemis. 
    - Activer/Désactiver : **Ctrl + I**
  - **Tir Rapide** : Le joueur peut tirer plus rapidement.
    - Activer/Désactiver : **Ctrl + R**
  - **Création d'Ennemis** : Les ennemis peuvent être créés en cliquant avec la souris, si ce mode est activé.
    - Activer/Désactiver : **Ctrl + E**
  - **Création d'Alliés** : Les alliés peuvent être créés en cliquant avec la souris, si ce mode est activé.
    - Activer/Désactiver : **Ctrl + A**

- **Menu de Débogage** :
  - Ouvrir/fermer le menu de débogage :
    - **Ctrl + P**

  Options dans le menu de débogage :
  - **Mode Débogage** : Activer/Désactiver le mode de débogage.
    - **Ctrl + D**
  - **Plein Écran** : Passer en mode plein écran ou revenir en mode fenêtré.
    - **Ctrl + F**
  - **Menu Débogage** : Activer/Désactiver la visibilité du menu de débogage.
    - **Ctrl + M**
  - **Invincibilité** : Activer/Désactiver l'invincibilité du joueur.
    - **Ctrl + I**
  - **Tir Rapide** : Activer/Désactiver le tir rapide du joueur.
    - **Ctrl + R**
  - **Création Mode Ennemi** : Activer/Désactiver la création d'ennemis en cliquant avec la souris.
    - **Ctrl + E**
  - **Création Mode Allié** : Activer/Désactiver la création d'alliés en cliquant avec la souris.
    - **Ctrl + A**

## Instructions pour l'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/space-invaders.git



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

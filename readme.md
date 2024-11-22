# Projet de Jeu en Python

## Description
Ce projet est un jeu développé en Python utilisant la bibliothèque Pygame. Le joueur contrôle un personnage qui doit éviter des notifications et des mails tout en tirant des projectiles.

## Installation
1. Clonez le dépôt.
2. Assurez-vous d'avoir Python et Pygame installés.
3. Exécutez le fichier `game.py` pour lancer le jeu.

## Fichiers Principaux
- `game.py` : Contient la boucle principale du jeu et la gestion des événements.
- `map.py` : Gère la carte et les collisions.
- `player.py` : Définit le joueur et ses mouvements.
- `projectile.py` : Gère les projectiles tirés par le joueur.
- `drawer.py` : Définit les tiroirs dans le jeu.
- `notif.py` : Gère les notifications qui apparaissent.
- `mail.py` : Gère les mails qui apparaissent.
- `text.py` : Gère l'affichage des textes à l'écran.

## Comment Jouer
- Utilisez les touches `W`, `A`, `S`, `D` pour déplacer le joueur.
- Appuyez sur les fleches pour tirer des projectiles.
- Évitez les les mails pour maintenir votre score.
- Attention aux notifications teams qui pompe votre salaire, cliquez dessus pour les faire partir

## Auteurs
- Evan Delbecq

## Fonctionnement du Code
Le code de ce projet de jeu en Python utilise la bibliothèque Pygame pour créer un environnement interactif où le joueur doit éviter des notifications et des mails tout en tirant des projectiles. Voici un aperçu de son fonctionnement :

### Initialisation
Le fichier `game.py` initialise le jeu, configure l'écran, charge les ressources (images, sons), et crée les objets principaux comme le joueur, les projectiles, les notifications, et les mails.

### Gestion des Sprites
La méthode `manage_sprites` de la classe `Game` gère l'affichage et le mouvement des différents sprites (joueur, projectiles, notifications, mails) à chaque frame.

### Déplacement du Joueur
La méthode `player_movement` permet de déplacer le joueur en utilisant les touches `W`, `A`, `S`, `D`.

### Tir de Projectiles
La méthode `shoot` permet au joueur de tirer des projectiles dans une direction donnée. Les projectiles sont ajoutés à une liste et leur mouvement est géré à chaque frame.

### Collisions
La méthode `check_collisions` vérifie les collisions entre les différents sprites (joueur, projectiles, notifications, mails) et applique les effets correspondants.

### Cooldowns
Les méthodes `cooldown_decrement`, `spawn_notif`, et `spawn_mail` gèrent les intervalles de temps entre les actions (tir, apparition de notifications et de mails).

### Suivi des Notifications
La méthode `notifs_stalking` permet aux notifications de suivre le joueur.

### Interaction avec les Notifications
La méthode `check_click` vérifie si le joueur clique sur une notification pour interagir avec elle.

Le jeu se déroule dans une boucle principale (`run`) qui met à jour l'état du jeu, gère les événements, et rafraîchit l'affichage à chaque itération.
# Notes Bash – Phase 1

- `for i in {nbr1..nbr2}` : boucle for de nbr1 à nbr2
- `mv` : déplace un fichier (et supprime l’original).  
   → utilisé aussi pour renommer un fichier dans le même dossier
- `read` : récupère une entrée utilisateur
- `[[ $var =~ ^[0-9]+$ ]]` : vérifier qu’une variable est bien un nombre
- `if [[ ... ]]` : version moderne et plus puissante de `[ ]`  
   (plus tolérante, gère `&&`, `||`…)
- `find . -type f -mtime +$x` : fichiers datant de plus de `x` jours  
   - `+$x` = plus de x jours  
   - `-$x` = moins de x jours  
   - `=$x` = exactement x jours  
   - `-mmin` : même logique mais en minutes
- `$(commande)` : récupérer la sortie d’une commande dans une variable
- `grep "mot" fichier` : chercher un mot/ensemble de mots dans un fichier
   - `-i` : ignore la casse (supprime les majuscules)
- `wc -l` : compte le nombre de lignes

# Notes Git - Phase 1
- `git status` : voir l’état des fichiers (modifiés, suivis, à commit)
- `git add fichier` : ajouter un fichier dans la mémoire tampon
- `git add` : ajoute tous les fichiers nouveaux/modifiés
- `git commit -m "message"` : ajout d'un message d'explication dans l'historique Git
- `git push` : envoyer les commits 

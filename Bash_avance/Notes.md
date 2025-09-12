# 📝 Notes Bash – Phase 3 (Arguments, Fonctions, Logs)

## Arguments et variables
- `$0` → nom du script 
- `$1`, `$2` → premier et deuxième argument 
- `$#` → nombre total d’arguments 
- `$@` → liste de tous les arguments 
- `$(( a + b ))` → calcul arithmétique 

## Fonctions
- Définition :
  `ma_fonction()` {
      # instructions
  }
- Appel :
  `ma_fonction argument`

## Log & Redirection
- `>` : redirige stdout (sortie normale) vers un fichier (écrase)
- `>>` : redirige stdout vers un fichier (ajoute)
- `2>` : redirige stderr (erreurs) vers un fichier (écrase)
- `2>>` : redirige stderr vers un fichier (ajoute)
- `commande > out.log 2> err.log` : sortie et erreurs séparées
- `commande > tout.log 2>&1` : fusion stdout + stderr dans le même fichier
- `$(date)` : insérer la date/heure actuelle (utile pour logs)

## Cron
- Toujours utiliser le chemin absolu si fichier dans un script et pour la commande dans crontab

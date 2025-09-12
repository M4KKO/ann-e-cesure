# Notes Réseau – Test de connectivité

## Ping
- `ping -c 1 <hôte>` : tester la connectivité ICMP
- Retour 0 = succès, retour ≠0 = échec
- Erreurs : unknown host, timeout, unreachable

## Curl
- `curl --head <url>` : récupère uniquement les en-têtes HTTP
- `-s` : mode silencieux (supprime les infos inutiles)
- Erreurs fréquentes : (6) DNS introuvable, (7) connexion refusée, (28) timeout
- Teste si le service web est disponible

## Bash
- `> /dev/null` masque la sortie standard
- `2>&1` masque aussi la sortie d’erreur
- `ss -tln` : scan de port TCP ouvert 
   - `-uln` : scan de port UDP ouvert 
   - `-tulnp` : scan TCP+UDP + programmes associés 

## Processus
- `ps aux` : liste les processus en cours
- `grep <nom>` : filtre un processus par nom
- `kill <PID>` : arrêter un processus proprement (SIGTERM) (-15 implicite)
- `kill -9 <PID>` : forcer l’arrêt (SIGKILL)
- `pkill <nom>` : arrêter par nom de processus
- `pgrep <nom>` : trouver le PID d’un processus
- `grep -v grep` : supprime le grep de la liste des processus 

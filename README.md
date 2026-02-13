# Année de césure — Portfolio (Linux / Réseau / Sécurité)

Ce dépôt regroupe mes scripts et exercices réalisés pendant mon année de césure, orientés **Linux**, **Bash**, **réseau Python** et **sécurité**.

## Projet vitrine : TCP Port Scanner (Python)
Un scanner de ports TCP **multithread** qui teste une liste de ports sur une IP et exporte les résultats en **JSON** et **CSV**.

- Tech: Python, sockets, threading
- Sorties: `resultats.json`, `resultats.csv`

### Usage
```bash
python3 Python_reseau/scripts/test_port.py 127.0.0.1 22 80 443

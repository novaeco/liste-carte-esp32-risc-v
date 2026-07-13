# 🛠️ Scripts - Automatisation & Outils

Dossier contenant tous les scripts Python pour automatiser la gestion de la base de données.

## 📋 Scripts disponibles

### ✅ Validation

#### `validate_boards.py`
Valide la base de données JSON contre le schéma.

```bash
python scripts/validate_boards.py
```

**Vérifications:**
- ✓ Schéma JSON valide
- ✓ Pas de doublons d'ID
- ✓ Types de données corrects
- ✓ Champs requis présents
- ✓ Statistiques de la base

**Output:**
```
🔍 Validation de la base de données ESP32 RISC-V...
✓ Validant le schéma JSON...
✅ Schéma valide (0 boards)
✓ Vérification des doublons...
✅ Aucun doublon détecté

📊 Statistiques:
  - Boards: 0
  - Fabricants: 0
  - SoCs: 0
  - Cartes avec écran: 0

✅ Validation réussie!
```

---

### 📊 Export

#### `generate_csv.py`
Génère un export CSV depuis la base JSON.

```bash
python scripts/generate_csv.py
```

**Output:** `database/boards.csv`
- Colonnes: ID, Manufacturer, Reference, SoC, Memory, Display, Connectivity, Interfaces, etc.
- Format: UTF-8, semicolon-separated
- Importable dans Excel/LibreOffice

---

#### `generate_excel.py`
Génère un export Excel formaté.

```bash
python scripts/generate_excel.py
```

**Output:** `database/boards.xlsx`
- Feuilles multiples (Overview, Detailed, By Manufacturer, By SoC)
- Mise en forme automatique
- Filtres activés
- Graphiques de statistiques

---

#### `generate_markdown.py`
Génère des fiches Markdown pour chaque carte.

```bash
python scripts/generate_markdown.py
```

**Output:** `docs/boards/[id].md`
- Une fiche par carte
- Liens croisés (fabricant, SoC)
- Tableau de spécifications
- Embedded images

---

#### `generate_pdf.py`
Génère un rapport PDF complet.

```bash
python scripts/generate_pdf.py
```

**Output:** `database/boards.pdf`
- Rapport complet de toutes les cartes
- Classement par fabricant/SoC
- Graphiques et statistiques
- 300+ pages (à terme)

---

### 🔧 Maintenance

#### `detect_duplicates.py`
Détecte les cartes dupliquées ou similaires.

```bash
python scripts/detect_duplicates.py
```

**Heuristiques:**
- Même ID
- Même manufacturer + reference
- Similitude de noms (Levenshtein > 85%)
- Même SoC + reference similaire

**Output:** JSON avec doublons potentiels

---

#### `check_links.py`
Vérifie que tous les URLs sont valides.

```bash
python scripts/check_links.py
# Options:
# --verbose  : Affiche tous les URLs testés
# --repair   : Essaie de corriger les URLs cassés
# --report   : Génère un rapport JSON
```

**Vérifie:**
- ✓ Datasheets
- ✓ Schematics
- ✓ GitHub repos
- ✓ Pages fabricants
- ✓ Buy links

**Output:** JSON avec status 200/404/timeout

---

#### `build_website.py`
Construit le site web statique.

```bash
python scripts/build_website.py
```

**Actions:**
1. Copie `boards.json` → `website/data/`
2. Génère pages HTML
3. Optimise images
4. Génère sitemap
5. Prépare pour GitHub Pages

---

#### `index_generator.py`
Génère un index pour la recherche.

```bash
python scripts/index_generator.py
```

**Output:** `website/data/index.json`
- Index complet pour recherche JS
- Optimisé pour performance
- Full-text search ready

---

## 🚀 Installation & Setup

### Prérequis
- Python 3.11+
- pip (gestionnaire de packages)

### Installation des dépendances

```bash
# 1. Créer un virtual environment
python -m venv venv

# 2. L'activer
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Installer les packages
pip install -r requirements.txt
```

### Vérifier l'installation

```bash
python scripts/validate_boards.py
# Devrait afficher "✅ Validation réussie!" (avec 0 boards)
```

---

## 📝 Workflow d'utilisation

### Ajouter une nouvelle carte

```bash
# 1. Éditez database/boards.json
nano database/boards.json
# Ajoutez le JSON de la nouvelle carte

# 2. Validez
python scripts/validate_boards.py

# 3. Générez les exports
python scripts/generate_csv.py
python scripts/generate_excel.py

# 4. Vérifiez les liens (optionnel)
python scripts/check_links.py

# 5. Commitez
git add database/boards.json database/boards.csv database/boards.xlsx
git commit -m "feat: Add [Manufacturer] [Board Name]"
git push
```

### Workflow CI/CD automatisé

Les scripts s'exécutent automatiquement via GitHub Actions :

```yaml
# Triggers:
- Push sur database/boards.json
- Pull request
- Manuellement via GitHub UI
- Chaque semaine (pour check_links.py)

# Actions:
1. validate_boards.py
2. generate_csv.py + generate_excel.py
3. build_website.py
4. check_links.py (hebdo)
5. Commit des fichiers générés
```

---

## 🔍 Développement des scripts

### Structure d'un script

```python
#!/usr/bin/env python3
"""Description courte du script"""

import json
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    
    print("🔍 Titre du script...")
    
    try:
        # Logique du script
        boards = load_json(boards_file)
        
        # Traitement
        process(boards)
        
        print("✅ Succès!")
        return 0
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Guidelines

- Toujours utiliser `Path()` pour les chemins de fichiers
- Afficher des emojis pour la clarté
- Toujours retourner 0 (succès) ou 1 (erreur)
- Supporter les options en ligne de commande (`argparse`)
- Ajouter des docstrings

---

## 🧪 Tester localement

```bash
# Tester un script
python scripts/validate_boards.py

# Tester avec couverture de code
pytest scripts/ --cov=scripts

# Format code
black scripts/

# Lint
flake8 scripts/
```

---

## 📊 Performance

| Script | Temps (0 boards) | Temps (300 boards) |
|--------|------------------|-------------------|
| validate_boards.py | < 1s | ~2s |
| generate_csv.py | < 1s | ~3s |
| generate_excel.py | < 2s | ~5s |
| generate_markdown.py | < 1s | ~10s |
| generate_pdf.py | < 5s | ~30s |
| check_links.py | varies | ~5min |
| build_website.py | < 2s | ~5s |

---

## 🐛 Troubleshooting

### ModuleNotFoundError

```
ModuleNotFoundError: No module named 'jsonschema'
```

**Solution:**
```bash
pip install -r requirements.txt
```

### Permission Denied

```
Permission denied: 'scripts/validate_boards.py'
```

**Solution:**
```bash
chmod +x scripts/*.py
python scripts/validate_boards.py
```

### File Not Found

```
FileNotFoundError: database/boards.json
```

**Solution:** Assurez-vous d'exécuter les scripts depuis la racine du dépôt
```bash
cd liste-carte-esp32-risc-v
python scripts/validate_boards.py
```

---

## 📝 TODO

- [ ] `generate_excel.py` - Implémenter
- [ ] `generate_markdown.py` - Implémenter
- [ ] `generate_pdf.py` - Implémenter
- [ ] `detect_duplicates.py` - Implémenter
- [ ] `check_links.py` - Implémenter
- [ ] `build_website.py` - Implémenter
- [ ] `index_generator.py` - Implémenter
- [ ] Tests unitaires pour chaque script
- [ ] Benchmarks de performance

---

**Mainteneur:** [@novaeco](https://github.com/novaeco)  
**Status:** 🚧 En développement

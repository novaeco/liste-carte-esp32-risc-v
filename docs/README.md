# 🚀 Bienvenue dans ESP32 RISC-V Board Encyclopedia

## 📖 Documentation disponible

- **[README.md](../README.md)** - Vue d'ensemble et structure du projet
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Guide de contribution
- **[ROADMAP.md](../ROADMAP.md)** - Feuille de route et phases
- **[CHANGELOG.md](../CHANGELOG.md)** - Historique des versions
- **[AGENTS.md](../AGENTS.md)** - Documentation des agents et automation

## 🎯 Quick Start

### 1️⃣ Ajouter une nouvelle carte

```bash
# Éditez database/boards.json
# Suivez le schéma dans database/schema.json
git add database/boards.json
git commit -m "feat: Add [Manufacturer] [Board Name]"
git push
```

### 2️⃣ Valider localement

```bash
pip install -r requirements.txt
python scripts/validate_boards.py
```

### 3️⃣ Générer les exports

```bash
python scripts/generate_csv.py
```

## 📂 Structure des dossiers

```
docs/              Cette documentation
database/          Base de données JSON et schéma
scripts/           Scripts Python d'automatisation
media/             Images, schémas, datasheets
website/           Site GitHub Pages (à venir)
.github/workflows/ CI/CD GitHub Actions
```

## ❓ Questions fréquentes

**Q: Où ajouter une carte ?**
R: Dans `database/boards.json`, en suivant le schéma `database/schema.json`

**Q: Puis-je laisser des champs vides ?**
R: Oui, utilisez `null` au lieu de deviner

**Q: Comment vérifier mon travail ?**
R: Exécutez `python scripts/validate_boards.py` avant de committer

**Q: Qui maintient le projet ?**
R: [@novaeco](https://github.com/novaeco) - Contributeurs bienvenue!

---

**Besoin d'aide?** [Ouvrir une issue](https://github.com/novaeco/liste-carte-esp32-risc-v/issues) 💬

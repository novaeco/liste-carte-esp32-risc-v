# 🌐 Website - ESP32 RISC-V Board Encyclopedia

Dossier pour le site web GitHub Pages (à développer en Phase 4).

## 📋 Structure (future)

```
website/
├── index.html           # Page d'accueil
├── search.html          # Interface de recherche
├── compare.html         # Outil de comparaison
├── about.html           # À propos du projet
│
├── css/
│   ├── style.css        # Styles principaux
│   └── responsive.css   # Design responsive
│
├── js/
│   ├── main.js          # Script principal
│   ├── search.js        # Moteur de recherche
│   ├── filters.js       # Système de filtrage
│   ├── compare.js       # Comparaison de cartes
│   └── utils.js         # Fonctions utilitaires
│
└── data/
    └── boards.json      # Copy du database/boards.json
```

## 🚀 Fonctionnalités prévues

### Phase 4 (Décembre 2026)

- [ ] Landing page attractive
- [ ] Moteur de recherche JavaScript
- [ ] Filtres multiples (SoC, fabricant, écran, mémoire, etc.)
- [ ] Outil de comparaison (2-5 cartes)
- [ ] Galerie de cartes avec images
- [ ] Classement par catégorie
- [ ] Design responsive (mobile, tablet, desktop)
- [ ] Performance optimisée
- [ ] SEO-friendly

### Filtres prévus

```
✓ Recherche texte (full-text)
✓ Par SoC (C2, C3, C5, C6, H2, P4, P4+C6)
✓ Par fabricant
✓ Par taille écran (avec/sans écran)
✓ Par type écran (LCD, OLED, AMOLED, ePaper)
✓ Par connectivité (Wi-Fi, BLE, Zigbee, etc.)
✓ Par mémoire (Flash, PSRAM)
✓ Par prix (plage)
✓ Par statut (production, discontinued, etc.)
✓ Combinaisons avancées
```

## 🛠️ Technologies

- **HTML5** / **CSS3** / **JavaScript** (vanilla)
- **GitHub Pages** (hébergement gratuit)
- **JSON statique** (pas de backend nécessaire)
- **Responsive design** (mobile-first)

## 📊 Données

Le site consomme `database/boards.json` :
- Généré automatiquement par script Python
- Versioning via Git
- Mis à jour automatiquement

## 🎨 Design

### Couleurs proposées
```
Primary:   #0066CC (ESP-IDF blue)
Success:   #00AA44
Warning:   #FFAA00
Danger:    #DD0000
Dark:      #1a1a1a
Light:     #f5f5f5
```

### Sections principales
1. **Header** : Logo + Navigation
2. **Hero** : Titre + Statistiques en direct
3. **Recherche** : Barre de recherche + filtres
4. **Galerie** : Grille de cartes
5. **Détails** : Vue complète d'une carte
6. **Comparaison** : Tableau comparatif
7. **Footer** : Liens + Contribution

## 📱 Responsive

```
Mobile:    < 768px   (1 colonne)
Tablet:    768-1024px (2 colonnes)
Desktop:   > 1024px  (3+ colonnes)
```

## 🔄 Build Process

```bash
# Générer les données
python scripts/generate_csv.py
cp database/boards.json website/data/

# Le site se met à jour automatiquement
# Push → GitHub Pages serve le contenu
```

## 📊 Statistiques en direct

Le site affiche automatiquement :
- Nombre total de boards
- Nombre de fabricants
- Nombre de SoC
- Dernière mise à jour

```javascript
// Exemple
const stats = {
  boards: boards.length,
  manufacturers: new Set(boards.map(b => b.manufacturer)).size,
  socs: new Set(boards.map(b => b.soc.name)).size,
  updated: new Date().toLocaleDateString('fr-FR')
};
```

## 🔍 Recherche

### Exemples de requêtes

```
ESP32-P4           → Tous les P4
display:7inch      → Écrans 7"
wifi6              → Support Wi-Fi 6
price:<50          → Moins de 50 USD
waveshare          → Fabricant Waveshare
```

## 🧪 Développement local

```bash
# Option 1: Python server
python -m http.server 8000
# Puis ouvrir http://localhost:8000/website/

# Option 2: Live server (VS Code)
# Extension "Live Server" → Right-click → Open with Live Server
```

## 🚀 Déploiement

```bash
# Le dépôt utilise GitHub Pages automatiquement
# Configure dans Settings > Pages > Branch: main, folder: /website

# Après chaque push sur main:
# GitHub Actions génère le site
# Il est accessible à: https://novaeco.github.io/liste-carte-esp32-risc-v/
```

## 📝 TODO

- [ ] Wireframes et mockups
- [ ] Design système
- [ ] Structure HTML
- [ ] CSS base et responsive
- [ ] JavaScript logique
- [ ] Intégration données
- [ ] Optimisation performance
- [ ] Tests UX
- [ ] SEO optimization
- [ ] Analytics setup
- [ ] Accessibilité (WCAG 2.1)

## 🤝 Contribution

Pour le design web, voir [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**Status** : 🔄 En attente de Phase 4 (Décembre 2026)  
**Mainteneur** : [@novaeco](https://github.com/novaeco)

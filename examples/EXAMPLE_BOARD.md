# 📄 Example Board - ESP32-C3-DevKitC-02

Ceci est un **template d'exemple** montrant comment ajouter une carte à la base de données.

## Donnees JSON

```json
{
  "id": "espressif-esp32-c3-devkitc-02",
  "manufacturer": "Espressif",
  "reference": "ESP32-C3-DevKitC-02",
  "commercial_name": "ESP32-C3 Development Board",
  "revision": "2.1",
  "release_date": "2024-01-15",
  "status": "production",
  "price_usd": 12.99,
  
  "soc": {
    "name": "ESP32-C3",
    "architecture": "RISC-V",
    "cores": 1,
    "frequency_mhz": 160,
    "riscv_isa": "RV32IMAC"
  },
  
  "memory": {
    "flash_mb": 4,
    "psram_mb": 0,
    "sram_mb": 384,
    "memory_type": "SPI Flash"
  },
  
  "display": {
    "enabled": false,
    "size_inches": null,
    "resolution": null,
    "type": null,
    "interface": null,
    "colors": null,
    "brightness": null,
    "touchscreen": false,
    "touch_type": null,
    "touch_controller": null
  },
  
  "connectivity": {
    "wifi": true,
    "wifi6": false,
    "bluetooth": false,
    "ble": true,
    "zigbee": false,
    "thread": false,
    "matter": false,
    "ethernet": false
  },
  
  "interfaces": {
    "gpio_count": 22,
    "uart": 2,
    "spi": 3,
    "i2c": 1,
    "i2s": 1,
    "usb": 1,
    "usb_type": "USB OTG",
    "jtag": true,
    "can": false,
    "microsd": false
  },
  
  "multimedia": {
    "camera": false,
    "mipi_csi": false,
    "dvp": false,
    "microphone": false,
    "speaker": false,
    "audio_codec": null
  },
  
  "software_support": {
    "esp_idf": true,
    "arduino": true,
    "platformio": true,
    "zephyr": true,
    "micropython": true,
    "lvgl": false,
    "rust": true
  },
  
  "documentation": {
    "datasheet_url": "https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf",
    "schematic_url": "https://github.com/espressif/esp-dev-kits/blob/master/esp32-c3-devkitc-02/schematics/",
    "pinout_url": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32-c3-devkitc-02_v1_1_pinlayout.png",
    "github_repo": "https://github.com/espressif/esp-idf",
    "wiki_url": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/",
    "manual_url": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32-c3-devkitc-02.html",
    "examples_url": "https://github.com/espressif/esp-idf/tree/master/examples",
    "notes": "Carte de développement populaire, bonne pour débuter avec l'ESP32-C3"
  },
  
  "links": {
    "buy_link": "https://www.aliexpress.com/wholesale?SearchText=esp32-c3-devkitc-02",
    "manufacturer_page": "https://www.espressif.com/en/products/modules/esp32-c3",
    "github_projects": [
      "https://github.com/topics/esp32-c3"
    ]
  }
}
```

## Comment ajouter cette carte

### Option 1 : Via l'interface GitHub

1. Allez sur `database/boards.json`
2. Cliquez sur l'icône ✏️ (Edit)
3. Copiez le JSON ci-dessus
4. Commitez avec le message : `feat: Add Espressif ESP32-C3-DevKitC-02`

### Option 2 : Via Git/CLI

```bash
# 1. Clone et setup
git clone https://github.com/novaeco/liste-carte-esp32-risc-v.git
cd liste-carte-esp32-risc-v

# 2. Éditez database/boards.json
# Ajoutez le JSON ci-dessus au tableau []

# 3. Validez
python scripts/validate_boards.py

# 4. Commitez et poussez
git add database/boards.json
git commit -m "feat: Add Espressif ESP32-C3-DevKitC-02"
git push

# 5. Ouvrez une PR
```

## Champs requis vs optionnels

### ✅ Requis
- `id` : Identifiant unique (lowercase, slugified)
- `manufacturer` : Nom du fabricant
- `reference` : Numéro exact de référence
- `soc` : Information sur le SoC
- `memory` : Configuration mémoire
- `connectivity` : Capacités de connectivité
- `interfaces` : GPIO, UART, etc.
- `software_support` : Support logiciel
- `documentation` : Sources et liens

### ❓ Optionnels (peuvent être `null`)
- `commercial_name` : Nom commercial
- `revision` : Numéro de révision
- `release_date` : Date de sortie
- `price_usd` : Prix
- `display.*` : Si pas d'écran
- Tous les champs individuels peuvent être `null` si inconnu

## Bonnes pratiques

### ✓ À FAIRE
```json
"price_usd": 12.99,
"flash_mb": 4,
"display": { "enabled": false }
```

### ✗ À ÉVITER
```json
"price_usd": "environ 13",
"flash_mb": "4 MB",
"display": null
```

## Sources fiables (par ordre de préférence)

1. **Datasheet officielle** du fabricant
2. **GitHub officiel** du fabricant
3. **Documentation officielle** sur docs.espressif.com
4. **Schéma PCB** fourni par le fabricant
5. **Wiki/documentation** sur GitHub
6. **Forums officiels** et discussions
7. Wikipedia et articles de blog *(à vérifier)*

## Besoin d'aide ?

- 📖 Voir [CONTRIBUTING.md](../../CONTRIBUTING.md)
- 💬 [Ouvrir une Discussion](https://github.com/novaeco/liste-carte-esp32-risc-v/discussions)
- 🐛 [Signaler un problème](https://github.com/novaeco/liste-carte-esp32-risc-v/issues)

---

**Notes** : Cet exemple est complet mais basé sur des données de 2024. Vérifiez toujours les sources officielles pour les informations à jour !

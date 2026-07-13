#!/usr/bin/env python3
"""
Génère des fiches Markdown pour chaque carte
Une fiche par carte dans docs/boards/
"""

import json
import sys
from pathlib import Path

def load_json(filepath):
    """Charge un fichier JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def bool_to_emoji(value):
    """Convertit un booléen en emoji"""
    return "✅" if value else "❌"

def generate_board_markdown(board):
    """
    Génère le contenu Markdown pour une carte
    """
    md = []
    
    # Titre
    md.append(f"# {board['commercial_name'] or board['reference']}")
    md.append(f"_{board['manufacturer']} - {board['reference']}_\n")
    
    # Résumé
    md.append("## 📋 Résumé")
    md.append(f"- **Fabricant**: {board['manufacturer']}")
    md.append(f"- **Référence**: {board['reference']}")
    md.append(f"- **Status**: {board['status']}")
    md.append(f"- **Prix**: ${board.get('price_usd', 'N/A')}")
    md.append(f"- **Date de sortie**: {board.get('release_date', 'N/A')}\n")
    
    # Processeur
    soc = board['soc']
    md.append("## 🔧 Processeur")
    md.append(f"- **SoC**: {soc['name']}")
    md.append(f"- **Architecture**: {soc['architecture']}")
    md.append(f"- **Cœurs**: {soc['cores']}")
    md.append(f"- **Fréquence**: {soc['frequency_mhz']} MHz")
    md.append(f"- **RISC-V ISA**: {soc.get('riscv_isa', 'N/A')}\n")
    
    # Mémoire
    memory = board['memory']
    md.append("## 💾 Mémoire")
    md.append(f"- **Flash**: {memory['flash_mb']} MB")
    md.append(f"- **PSRAM**: {memory['psram_mb']} MB")
    md.append(f"- **SRAM**: {memory['sram_mb']} MB\n")
    
    # Affichage
    display = board['display']
    if display['enabled']:
        md.append("## 📺 Affichage")
        md.append(f"- **Taille**: {display['size_inches']} pouces")
        md.append(f"- **Résolution**: {display['resolution']}")
        md.append(f"- **Type**: {display['type']}")
        md.append(f"- **Interface**: {display['interface']}")
        md.append(f"- **Couleurs**: {display.get('colors', 'N/A')}")
        md.append(f"- **Tactile**: {bool_to_emoji(display['touchscreen'])}")
        if display['touchscreen']:
            md.append(f"- **Type tactile**: {display['touch_type']}")
            md.append(f"- **Contrôleur**: {display.get('touch_controller', 'N/A')}")
        md.append()
    else:
        md.append("## 📺 Affichage")
        md.append("Aucun écran intégré\n")
    
    # Connectivité
    conn = board['connectivity']
    md.append("## 📡 Connectivité")
    md.append(f"- **Wi-Fi**: {bool_to_emoji(conn['wifi'])}")
    md.append(f"- **Wi-Fi 6**: {bool_to_emoji(conn['wifi6'])}")
    md.append(f"- **Bluetooth**: {bool_to_emoji(conn['bluetooth'])}")
    md.append(f"- **BLE**: {bool_to_emoji(conn['ble'])}")
    md.append(f"- **Zigbee**: {bool_to_emoji(conn['zigbee'])}")
    md.append(f"- **Thread**: {bool_to_emoji(conn['thread'])}")
    md.append(f"- **Matter**: {bool_to_emoji(conn['matter'])}")
    md.append(f"- **Ethernet**: {bool_to_emoji(conn['ethernet'])}\n")
    
    # Interfaces
    ifaces = board['interfaces']
    md.append("## 🔌 Interfaces")
    md.append(f"| Interface | Nombre |")
    md.append(f"|-----------|--------|")
    md.append(f"| GPIO | {ifaces['gpio_count']} |")
    md.append(f"| UART | {ifaces['uart']} |")
    md.append(f"| SPI | {ifaces['spi']} |")
    md.append(f"| I2C | {ifaces['i2c']} |")
    md.append(f"| I2S | {ifaces['i2s']} |")
    md.append(f"| USB | {ifaces['usb']} ({ifaces.get('usb_type', 'N/A')}) |")
    md.append(f"| JTAG | {bool_to_emoji(ifaces['jtag'])} |")
    md.append(f"| CAN | {bool_to_emoji(ifaces['can'])} |")
    md.append(f"| microSD | {bool_to_emoji(ifaces['microsd'])} |\n")
    
    # Multimédia
    mm = board['multimedia']
    if any([mm.get(k) for k in ['camera', 'microphone', 'speaker']]):
        md.append("## 🎬 Multimédia")
        md.append(f"- **Caméra**: {bool_to_emoji(mm['camera'])}")
        if mm.get('camera'):
            md.append(f"  - MIPI CSI: {bool_to_emoji(mm['mipi_csi'])}")
            md.append(f"  - DVP: {bool_to_emoji(mm['dvp'])}")
        md.append(f"- **Microphone**: {bool_to_emoji(mm['microphone'])}")
        md.append(f"- **Haut-parleur**: {bool_to_emoji(mm['speaker'])}")
        if mm.get('audio_codec'):
            md.append(f"- **Codec audio**: {mm['audio_codec']}")
        md.append()
    
    # Support logiciel
    sw = board['software_support']
    md.append("## 💻 Support Logiciel")
    md.append(f"- **ESP-IDF**: {bool_to_emoji(sw['esp_idf'])}")
    md.append(f"- **Arduino**: {bool_to_emoji(sw['arduino'])}")
    md.append(f"- **PlatformIO**: {bool_to_emoji(sw['platformio'])}")
    md.append(f"- **Zephyr**: {bool_to_emoji(sw['zephyr'])}")
    md.append(f"- **MicroPython**: {bool_to_emoji(sw['micropython'])}")
    md.append(f"- **LVGL**: {bool_to_emoji(sw['lvgl'])}")
    md.append(f"- **Rust**: {bool_to_emoji(sw['rust'])}\n")
    
    # Documentation
    docs = board['documentation']
    md.append("## 📚 Documentation")
    if docs.get('datasheet_url'):
        md.append(f"- [📄 Datasheet]({docs['datasheet_url']})")
    if docs.get('schematic_url'):
        md.append(f"- [📐 Schéma]({docs['schematic_url']})")
    if docs.get('pinout_url'):
        md.append(f"- [📌 Pinout]({docs['pinout_url']})")
    if docs.get('github_repo'):
        md.append(f"- [🐙 GitHub]({docs['github_repo']})")
    if docs.get('wiki_url'):
        md.append(f"- [📖 Wiki]({docs['wiki_url']})")
    if docs.get('examples_url'):
        md.append(f"- [💡 Exemples]({docs['examples_url']})")
    md.append()
    
    # Liens d'achat
    links = board['links']
    md.append("## 🛒 Achat")
    if links.get('buy_link'):
        md.append(f"- [🛍️ Acheter]({links['buy_link']})")
    if links.get('manufacturer_page'):
        md.append(f"- [🏢 Page fabricant]({links['manufacturer_page']})")
    md.append()
    
    # Notes
    if docs.get('notes'):
        md.append("## 📝 Notes")
        md.append(f"{docs['notes']}\n")
    
    md.append("---")
    md.append(f"*Fiche mise à jour automatiquement par script*")
    
    return "\n".join(md)

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    boards_dir = script_dir / "docs" / "boards"
    
    # Créer le répertoire s'il n'existe pas
    boards_dir.mkdir(parents=True, exist_ok=True)
    
    print("📝 Génération des fiches Markdown...")
    print(f"📁 Source: {boards_file}")
    print(f"💾 Destination: {boards_dir}\n")
    
    try:
        boards = load_json(boards_file)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return 1
    
    if not boards:
        print("⚠️  Aucune carte trouvée")
        return 1
    
    try:
        for board in boards:
            board_id = board['id']
            md_file = boards_dir / f"{board_id}.md"
            
            content = generate_board_markdown(board)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {board_id}.md")
        
        print(f"\n✅ {len(boards)} fiches générées!")
        print(f"📍 Répertoire: {boards_dir}")
        print("\n✅ Export réussi!")
        return 0
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

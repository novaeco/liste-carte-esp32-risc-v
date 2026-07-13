#!/usr/bin/env python3
"""
Génère un export CSV depuis la base de données JSON
Format: UTF-8, semicolon-separated pour Excel
"""

import json
import csv
import sys
from pathlib import Path
from collections import OrderedDict

def load_json(filepath):
    """Charge un fichier JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def flatten_board(board):
    """
    Convertit un board JSON en dictionnaire plat pour le CSV
    """
    flat = OrderedDict()
    
    # Identification
    flat['ID'] = board.get('id', '')
    flat['Manufacturer'] = board.get('manufacturer', '')
    flat['Reference'] = board.get('reference', '')
    flat['Commercial Name'] = board.get('commercial_name', '')
    flat['Status'] = board.get('status', '')
    flat['Price USD'] = board.get('price_usd', '')
    flat['Release Date'] = board.get('release_date', '')
    
    # SoC
    soc = board.get('soc', {})
    flat['SoC'] = soc.get('name', '')
    flat['Architecture'] = soc.get('architecture', '')
    flat['Cores'] = soc.get('cores', '')
    flat['Frequency MHz'] = soc.get('frequency_mhz', '')
    flat['RISC-V ISA'] = soc.get('riscv_isa', '')
    
    # Memory
    memory = board.get('memory', {})
    flat['Flash MB'] = memory.get('flash_mb', '')
    flat['PSRAM MB'] = memory.get('psram_mb', '')
    flat['SRAM MB'] = memory.get('sram_mb', '')
    
    # Display
    display = board.get('display', {})
    flat['Has Display'] = display.get('enabled', False)
    flat['Display Size'] = display.get('size_inches', '')
    flat['Display Resolution'] = display.get('resolution', '')
    flat['Display Type'] = display.get('type', '')
    flat['Display Interface'] = display.get('interface', '')
    flat['Touchscreen'] = display.get('touchscreen', False)
    flat['Touch Type'] = display.get('touch_type', '')
    flat['Touch Controller'] = display.get('touch_controller', '')
    
    # Connectivity
    conn = board.get('connectivity', {})
    flat['Wi-Fi'] = conn.get('wifi', False)
    flat['Wi-Fi 6'] = conn.get('wifi6', False)
    flat['Bluetooth'] = conn.get('bluetooth', False)
    flat['BLE'] = conn.get('ble', False)
    flat['Zigbee'] = conn.get('zigbee', False)
    flat['Thread'] = conn.get('thread', False)
    flat['Matter'] = conn.get('matter', False)
    flat['Ethernet'] = conn.get('ethernet', False)
    
    # Interfaces
    ifaces = board.get('interfaces', {})
    flat['GPIO Count'] = ifaces.get('gpio_count', '')
    flat['UART'] = ifaces.get('uart', '')
    flat['SPI'] = ifaces.get('spi', '')
    flat['I2C'] = ifaces.get('i2c', '')
    flat['I2S'] = ifaces.get('i2s', '')
    flat['USB Ports'] = ifaces.get('usb', '')
    flat['USB Type'] = ifaces.get('usb_type', '')
    flat['JTAG'] = ifaces.get('jtag', False)
    flat['CAN/TWAI'] = ifaces.get('can', False)
    flat['microSD'] = ifaces.get('microsd', False)
    
    # Multimedia
    mm = board.get('multimedia', {})
    flat['Camera'] = mm.get('camera', False)
    flat['MIPI CSI'] = mm.get('mipi_csi', False)
    flat['DVP'] = mm.get('dvp', False)
    flat['Microphone'] = mm.get('microphone', False)
    flat['Speaker'] = mm.get('speaker', False)
    flat['Audio Codec'] = mm.get('audio_codec', '')
    
    # Software Support
    sw = board.get('software_support', {})
    flat['ESP-IDF'] = sw.get('esp_idf', False)
    flat['Arduino'] = sw.get('arduino', False)
    flat['PlatformIO'] = sw.get('platformio', False)
    flat['Zephyr'] = sw.get('zephyr', False)
    flat['MicroPython'] = sw.get('micropython', False)
    flat['LVGL'] = sw.get('lvgl', False)
    flat['Rust'] = sw.get('rust', False)
    
    # Documentation
    docs = board.get('documentation', {})
    flat['Datasheet URL'] = docs.get('datasheet_url', '')
    flat['GitHub Repo'] = docs.get('github_repo', '')
    flat['Wiki URL'] = docs.get('wiki_url', '')
    flat['Notes'] = docs.get('notes', '')
    
    # Links
    links = board.get('links', {})
    flat['Buy Link'] = links.get('buy_link', '')
    flat['Manufacturer Page'] = links.get('manufacturer_page', '')
    
    return flat

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    csv_file = script_dir / "database" / "boards.csv"
    
    print("📊 Génération du CSV...")
    print(f"📁 Source: {boards_file}")
    print(f"💾 Destination: {csv_file}\n")
    
    try:
        boards = load_json(boards_file)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return 1
    
    if not boards:
        print("⚠️  Aucune carte trouvée")
        return 1
    
    # Générer le CSV
    try:
        flat_boards = [flatten_board(b) for b in boards]
        
        with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=flat_boards[0].keys(), delimiter=';')
            writer.writeheader()
            writer.writerows(flat_boards)
        
        print(f"✅ CSV généré: {len(flat_boards)} cartes")
        print(f"📍 Fichier: {csv_file.name}")
        print(f"📏 Colonnes: {len(flat_boards[0])}")
        print("\n✅ Export réussi!")
        return 0
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

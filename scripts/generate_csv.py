#!/usr/bin/env python3
"""
Export script: CSV generation for ESP32 RISC-V boards
Génère un export CSV depuis la base JSON
"""

import json
import csv
import sys
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    csv_file = script_dir / "database" / "boards.csv"
    
    print("📊 Génération du CSV...")
    
    # Charger les boards
    try:
        with open(boards_file, 'r', encoding='utf-8') as f:
            boards = json.load(f)
    except FileNotFoundError:
        print(f"❌ Erreur: {boards_file} non trouvé")
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ Erreur JSON: {e}")
        return 1
    
    if not boards:
        print("⚠️  Aucun board dans la base de données")
        return 0
    
    # Préparer les données
    rows = []
    for board in boards:
        row = {
            'ID': board.get('id', ''),
            'Manufacturer': board.get('manufacturer', ''),
            'Reference': board.get('reference', ''),
            'Commercial Name': board.get('commercial_name', ''),
            'Status': board.get('status', ''),
            'Price (USD)': board.get('price_usd', ''),
            'SoC': board.get('soc', {}).get('name', ''),
            'Cores': board.get('soc', {}).get('cores', ''),
            'Frequency (MHz)': board.get('soc', {}).get('frequency_mhz', ''),
            'Flash (MB)': board.get('memory', {}).get('flash_mb', ''),
            'PSRAM (MB)': board.get('memory', {}).get('psram_mb', ''),
            'SRAM (MB)': board.get('memory', {}).get('sram_mb', ''),
            'Display': 'Yes' if board.get('display', {}).get('enabled') else 'No',
            'Display Size': board.get('display', {}).get('size_inches', ''),
            'Display Resolution': board.get('display', {}).get('resolution', ''),
            'Display Type': board.get('display', {}).get('type', ''),
            'Touchscreen': 'Yes' if board.get('display', {}).get('touchscreen') else 'No',
            'Wi-Fi': 'Yes' if board.get('connectivity', {}).get('wifi') else 'No',
            'Wi-Fi 6': 'Yes' if board.get('connectivity', {}).get('wifi6') else 'No',
            'Bluetooth': 'Yes' if board.get('connectivity', {}).get('bluetooth') else 'No',
            'BLE': 'Yes' if board.get('connectivity', {}).get('ble') else 'No',
            'Zigbee': 'Yes' if board.get('connectivity', {}).get('zigbee') else 'No',
            'Thread': 'Yes' if board.get('connectivity', {}).get('thread') else 'No',
            'Matter': 'Yes' if board.get('connectivity', {}).get('matter') else 'No',
            'GPIO': board.get('interfaces', {}).get('gpio_count', ''),
            'UART': board.get('interfaces', {}).get('uart', ''),
            'SPI': board.get('interfaces', {}).get('spi', ''),
            'I2C': board.get('interfaces', {}).get('i2c', ''),
            'I2S': board.get('interfaces', {}).get('i2s', ''),
            'USB': board.get('interfaces', {}).get('usb', ''),
            'JTAG': 'Yes' if board.get('interfaces', {}).get('jtag') else 'No',
            'microSD': 'Yes' if board.get('interfaces', {}).get('microsd') else 'No',
            'ESP-IDF': 'Yes' if board.get('software_support', {}).get('esp_idf') else 'No',
            'Arduino': 'Yes' if board.get('software_support', {}).get('arduino') else 'No',
            'MicroPython': 'Yes' if board.get('software_support', {}).get('micropython') else 'No',
            'LVGL': 'Yes' if board.get('software_support', {}).get('lvgl') else 'No',
            'Datasheet URL': board.get('documentation', {}).get('datasheet_url', ''),
            'Manufacturer Page': board.get('links', {}).get('manufacturer_page', ''),
        }
        rows.append(row)
    
    # Écrire le CSV
    try:
        fieldnames = list(rows[0].keys()) if rows else []
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"✅ CSV généré: {csv_file}")
        print(f"   {len(rows)} boards exportés")
        return 0
    except Exception as e:
        print(f"❌ Erreur lors de la génération du CSV: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

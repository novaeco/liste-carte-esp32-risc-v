#!/usr/bin/env python3
"""
Validation script for ESP32 RISC-V boards database
Valide le schéma JSON et détecte les doublons
"""

import json
import sys
from pathlib import Path
import jsonschema
from collections import defaultdict

def load_json(filepath):
    """Charge un fichier JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_schema(boards, schema):
    """Valide les boards contre le schéma"""
    errors = []
    for i, board in enumerate(boards):
        try:
            jsonschema.validate(instance=board, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Board {i} ({board.get('id', 'UNKNOWN')}): {e.message}")
    return errors

def check_duplicates(boards):
    """Détecte les doublons"""
    duplicates = defaultdict(list)
    ids_seen = {}
    refs_seen = {}
    
    for i, board in enumerate(boards):
        board_id = board.get('id')
        ref = f"{board.get('manufacturer', 'UNKNOWN')}/{board.get('reference', 'UNKNOWN')}"
        
        # Check ID
        if board_id in ids_seen:
            duplicates['id_duplicates'].append({
                'id': board_id,
                'indices': [ids_seen[board_id], i]
            })
        else:
            ids_seen[board_id] = i
        
        # Check manufacturer + reference
        if ref in refs_seen:
            duplicates['ref_duplicates'].append({
                'reference': ref,
                'indices': [refs_seen[ref], i]
            })
        else:
            refs_seen[ref] = i
    
    return duplicates

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    schema_file = script_dir / "database" / "schema.json"
    
    print("🔍 Validation de la base de données ESP32 RISC-V...")
    print(f"📁 Boards: {boards_file}")
    print(f"📋 Schema: {schema_file}\n")
    
    # Charger les fichiers
    try:
        boards = load_json(boards_file)
        schema = load_json(schema_file)
    except FileNotFoundError as e:
        print(f"❌ Erreur: Fichier non trouvé: {e}")
        return 1
    except json.JSONDecodeError as e:
        print(f"❌ Erreur JSON: {e}")
        return 1
    
    # Validation du schéma
    print("✓ Validant le schéma JSON...")
    schema_errors = validate_schema(boards, schema)
    
    if schema_errors:
        print(f"❌ {len(schema_errors)} erreur(s) de schéma détectée(s):")
        for error in schema_errors:
            print(f"  - {error}")
        return 1
    else:
        print(f"✅ Schéma valide ({len(boards)} boards)")
    
    # Détection des doublons
    print("\n✓ Vérification des doublons...")
    duplicates = check_duplicates(boards)
    
    has_duplicates = any(v for v in duplicates.values() if v)
    
    if has_duplicates:
        print("⚠️  Doublons détectés:")
        if duplicates.get('id_duplicates'):
            print(f"  IDs dupliqués: {duplicates['id_duplicates']}")
        if duplicates.get('ref_duplicates'):
            print(f"  Références dupliquées: {duplicates['ref_duplicates']}")
        return 1
    else:
        print("✅ Aucun doublon détecté")
    
    # Statistiques
    print(f"\n📊 Statistiques:")
    print(f"  - Boards: {len(boards)}")
    
    manufacturers = set(b.get('manufacturer') for b in boards)
    socs = set(b.get('soc', {}).get('name') for b in boards if 'soc' in b)
    
    print(f"  - Fabricants: {len(manufacturers)}")
    print(f"  - SoCs: {len(socs)}")
    
    boards_with_display = sum(1 for b in boards if b.get('display', {}).get('enabled'))
    print(f"  - Cartes avec écran: {boards_with_display}")
    
    print("\n✅ Validation réussie!")
    return 0

if __name__ == "__main__":
    sys.exit(main())

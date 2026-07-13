#!/usr/bin/env python3
"""
Vérifie que tous les URLs sont valides (HTTP status)
"""

import json
import sys
from pathlib import Path
import time

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("❌ requests not installed. Run: pip install requests")
    sys.exit(1)

def load_json(filepath):
    """Charge un fichier JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_session():
    """Crée une session requests avec retry"""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504)
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def check_url(url, session, timeout=5):
    """Vérifie si une URL est accessible"""
    if not url:
        return None, "Empty URL"
    
    try:
        response = session.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code, None
    except requests.RequestException as e:
        return None, str(e)

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    
    print("🔗 Vérification des liens...")
    print(f"📁 Source: {boards_file}\n")
    
    try:
        boards = load_json(boards_file)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return 1
    
    session = create_session()
    broken_links = []
    checked = 0
    
    print("Vérification en cours...\n")
    
    for board in boards:
        docs = board.get('documentation', {})
        links = board.get('links', {})
        
        urls = [
            ('datasheet', docs.get('datasheet_url')),
            ('github', docs.get('github_repo')),
            ('wiki', docs.get('wiki_url')),
            ('buy', links.get('buy_link')),
            ('manufacturer', links.get('manufacturer_page')),
        ]
        
        for link_type, url in urls:
            if not url:
                continue
            
            status, error = check_url(url, session)
            checked += 1
            
            if status is None:
                broken_links.append({
                    'board': board['id'],
                    'type': link_type,
                    'url': url,
                    'error': error
                })
                print(f"❌ {board['id']}: {link_type} - {error}")
            elif status >= 400:
                broken_links.append({
                    'board': board['id'],
                    'type': link_type,
                    'url': url,
                    'error': f"HTTP {status}"
                })
                print(f"⚠️  {board['id']}: {link_type} - HTTP {status}")
            else:
                print(f"✅ {board['id']}: {link_type} - OK")
            
            time.sleep(0.5)  # Rate limiting
    
    session.close()
    
    print(f"\n📊 Résumé:")
    print(f"  - URLs vérifiées: {checked}")
    print(f"  - Liens cassés: {len(broken_links)}")
    
    if broken_links:
        print(f"\n⚠️  Liens cassés:")
        for item in broken_links:
            print(f"  - {item['board']}: {item['type']} - {item['error']}")
        return 1
    else:
        print(f"\n✅ Tous les liens sont valides!")
        return 0

if __name__ == "__main__":
    sys.exit(main())

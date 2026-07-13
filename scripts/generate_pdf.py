#!/usr/bin/env python3
"""
Génère un rapport PDF complet avec toutes les cartes
Utilise reportlab pour la génération
"""

import json
import sys
from pathlib import Path
from datetime import datetime

try:
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Preformatted
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
except ImportError:
    print("❌ reportlab not installed. Run: pip install reportlab")
    sys.exit(1)

def load_json(filepath):
    """Charge un fichier JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def bool_to_text(value):
    """Convertit un booléen en texte"""
    return "✓" if value else "✗"

def main():
    script_dir = Path(__file__).parent.parent
    boards_file = script_dir / "database" / "boards.json"
    pdf_file = script_dir / "database" / "boards.pdf"
    
    print("📄 Génération du PDF...")
    print(f"📁 Source: {boards_file}")
    print(f"💾 Destination: {pdf_file}\n")
    
    try:
        boards = load_json(boards_file)
    except Exception as e:
        print(f"❌ Erreur lors du chargement: {e}")
        return 1
    
    if not boards:
        print("⚠️  Aucune carte trouvée")
        return 1
    
    try:
        # Créer le PDF
        doc = SimpleDocTemplate(str(pdf_file), pagesize=landscape(A4))
        story = []
        styles = getSampleStyleSheet()
        
        # Style personnalisé
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1F4E78'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1F4E78'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        
        # Titre du document
        story.append(Paragraph("ESP32 RISC-V Board Encyclopedia", title_style))
        story.append(Paragraph(f"Complete Database - {datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
        story.append(Spacer(1, 0.5*cm))
        
        # Statistiques
        manufacturers = set(b.get('manufacturer') for b in boards)
        socs = set(b.get('soc', {}).get('name') for b in boards if 'soc' in b)
        boards_with_display = sum(1 for b in boards if b.get('display', {}).get('enabled'))
        
        stats_text = f"""<b>Statistics:</b><br/>
        • Total Boards: {len(boards)}<br/>
        • Manufacturers: {len(manufacturers)}<br/>
        • SoC Types: {len(socs)}<br/>
        • Boards with Display: {boards_with_display}
        """
        story.append(Paragraph(stats_text, styles['Normal']))
        story.append(Spacer(1, 0.5*cm))
        
        # Tableau principal
        story.append(Paragraph("Complete Board List", heading_style))
        
        data = [[
            "Manufacturer",
            "Reference",
            "SoC",
            "Flash",
            "PSRAM",
            "Display",
            "Wi-Fi 6",
            "Zigbee",
            "Matter",
            "Price"
        ]]
        
        for board in boards:
            data.append([
                board.get('manufacturer', ''),
                board.get('reference', '')[:20],
                board.get('soc', {}).get('name', ''),
                f"{board.get('memory', {}).get('flash_mb', '')}MB",
                f"{board.get('memory', {}).get('psram_mb', '')}MB",
                "Yes" if board.get('display', {}).get('enabled') else "No",
                bool_to_text(board.get('connectivity', {}).get('wifi6')),
                bool_to_text(board.get('connectivity', {}).get('zigbee')),
                bool_to_text(board.get('connectivity', {}).get('matter')),
                f"${board.get('price_usd', 'N/A')}"
            ])
        
        # Créer le tableau
        table = Table(data, colWidths=[2*cm, 3*cm, 2*cm, 1.2*cm, 1.2*cm, 1.2*cm, 1*cm, 1*cm, 1*cm, 1.2*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E78')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 7),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 0.5*cm))
        
        # Fabricants
        story.append(PageBreak())
        story.append(Paragraph("Boards by Manufacturer", heading_style))
        
        manufacturers_dict = {}
        for board in boards:
            mfg = board.get('manufacturer', 'Unknown')
            if mfg not in manufacturers_dict:
                manufacturers_dict[mfg] = []
            manufacturers_dict[mfg].append(board)
        
        for mfg in sorted(manufacturers_dict.keys()):
            boards_list = manufacturers_dict[mfg]
            mfg_text = f"<b>{mfg}</b> ({len(boards_list)} boards)<br/>"
            for board in boards_list[:5]:  # Limiter à 5 par page
                mfg_text += f"  • {board['reference']}<br/>"
            if len(boards_list) > 5:
                mfg_text += f"  ... and {len(boards_list) - 5} more<br/>"
            story.append(Paragraph(mfg_text, styles['Normal']))
        
        # Footer
        story.append(Spacer(1, 1*cm))
        story.append(Paragraph("---", styles['Normal']))
        story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Project: liste-carte-esp32-risc-v", styles['Normal']))
        
        # Générer le PDF
        doc.build(story)
        
        print(f"✅ PDF généré: {len(boards)} cartes")
        print(f"📍 Fichier: {pdf_file.name}")
        print("\n✅ Export réussi!")
        return 0
        
    except Exception as e:
        print(f"❌ Erreur lors de la génération: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ==================== CONFIG ====================
TEMPLATE_FILE = "Void Hacks () 8.0 ppt.pptx"
OUTPUT_FILE = "CodeBlack_VoidHacks8.pptx"

NEON_GREEN = RGBColor(0x00, 0xFF, 0xAA)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RED = RGBColor(0xFF, 0x33, 0x55)
CYAN = RGBColor(0x00, 0xD4, 0xFF)
DARK = RGBColor(0x05, 0x07, 0x0F)
MUTED = RGBColor(0xCC, 0xCC, 0xCC)

# ==================== LOAD TEMPLATE ====================
prs = Presentation(TEMPLATE_FILE)
print(f"✅ Template loaded: {len(prs.slides)} slides")

# ==================== HELPER ====================
def add_textbox(slide, left, top, width, height, text, size=12, color=WHITE, bold=False, align=PP_ALIGN.LEFT):
    """Add a textbox to slide"""
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = "Calibri"
    p.alignment = align
    return tb

def add_multiline(slide, left, top, width, height, lines):
    """Add multiline textbox — lines = [(text, size, color, bold), ...]"""
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, (text, size, color, bold) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = text
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.font.name = "Calibri"
    return tb

def add_card(slide, left, top, width, height, border_color=NEON_GREEN, fill_color=None):
    """Add a rounded rectangle card"""
    card = slide.shapes.add_shape(5, Inches(left), Inches(top), Inches(width), Inches(height))
    if fill_color:
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
    else:
        card.fill.background()
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    return card

# ==================== SLIDE 2: PROPOSED SOLUTION ====================
print("📝 Filling Slide 2 — Proposed Solution...")
slide2 = prs.slides[1]

# Problem section (left)
add_textbox(slide2, 0.5, 0.9, 6, 0.4, "🎯 THE PROBLEM", 16, RED, True)
add_multiline(slide2, 0.5, 1.4, 6, 2.5, [
    ("• 7,000+ cyber fraud complaints in Indore (2026)", 12, WHITE, False),
    ("• ₹60+ Crore loss — recovery below 1%", 12, WHITE, False),
    ("• IO receives 5+ fragmented artifacts per case", 12, WHITE, False),
    ("• Manual triage takes 3-4 days", 12, WHITE, False),
    ("• No correlation engine for entities", 12, WHITE, False),
])

# Solution section (right)
add_textbox(slide2, 6.7, 0.9, 6, 0.4, "💡 OUR SOLUTION — DRISHTI-X", 16, NEON_GREEN, True)
add_multiline(slide2, 6.7, 1.4, 6, 2.5, [
    ("✓ Multi-Source Ingestion (CDR, Bank, Chat, .eml, APK)", 11, WHITE, False),
    ("✓ Entity Extraction (Phone, UPI, IMEI, IP, MAC)", 11, WHITE, False),
    ("✓ Isolation Forest ML — Real AI Anomaly Detection", 11, WHITE, False),
    ("✓ Auditable Risk Scoring (0-100 with reasoning)", 11, WHITE, False),
    ("✓ Interactive Network Graph", 11, WHITE, False),
    ("✓ Forensic Exports (TXT, JSON, PDF)", 11, WHITE, False),
])

# Differentiators (bottom)
add_textbox(slide2, 0.5, 4.1, 12, 0.4, "🎯 WHY DRISHTI-X IS DIFFERENT", 14, CYAN, True)
add_multiline(slide2, 0.5, 4.6, 12.3, 2.5, [
    ("1. REAL ML — Isolation Forest (not just rules)", 12, WHITE, False),
    ("2. AUDITABLE — every risk score shows weighted reasoning", 12, WHITE, False),
    ("3. OFFLINE-CAPABLE — works on police workstation", 12, WHITE, False),
    ("4. FORENSIC INTEGRITY — SHA-256 content hashing", 12, WHITE, False),
    ("5. HUMAN-IN-LOOP — IO approval required", 12, WHITE, False),
    ("6. FAST — under 10 seconds end-to-end", 12, WHITE, False),
])

# ==================== SLIDE 3: TECHNICAL APPROACH ====================
print("📝 Filling Slide 3 — Technical Approach...")
slide3 = prs.slides[2]

# Tech stack (left)
add_textbox(slide3, 0.5, 1.0, 6, 0.4, "🛠️ TECH STACK", 14, NEON_GREEN, True)
add_multiline(slide3, 0.5, 1.5, 6, 3.5, [
    ("Frontend: Streamlit (Python)", 11, WHITE, False),
    ("AI/ML: scikit-learn Isolation Forest", 11, WHITE, False),
    ("Features: amount, hour, sender freq,", 10, MUTED, False),
    ("         late-night flag, velocity ratio", 10, MUTED, False),
    ("Graph Engine: NetworkX + Plotly", 11, WHITE, False),
    ("PDF Generator: reportlab", 11, WHITE, False),
    ("Database: SQLite (case history)", 11, WHITE, False),
    ("Integrity: SHA-256 content hashing", 11, WHITE, False),
])

# Performance (right)
add_textbox(slide3, 6.7, 1.0, 6, 0.4, "⚡ PERFORMANCE METRICS", 14, CYAN, True)
add_multiline(slide3, 6.7, 1.5, 6, 3.5, [
    ("• 1,000 records parsed: < 0.3 seconds", 11, WHITE, False),
    ("• Isolation Forest training: < 1 second", 11, WHITE, False),
    ("• End-to-end: under 10 seconds", 11, WHITE, False),
    ("• Anomaly rate: 15% (tunable)", 11, WHITE, False),
    ("• Entity cross-linking: automatic", 11, WHITE, False),
    ("", 8, WHITE, False),
    ("🔒 EVIDENTIARY INTEGRITY", 12, NEON_GREEN, True),
    ("• SHA-256 content hashing", 11, WHITE, False),
    ("• Immutable audit trail", 11, WHITE, False),
    ("• BNSS 2023 Section 63 aligned", 11, WHITE, False),
])

# Pipeline (bottom)
add_textbox(slide3, 0.5, 5.2, 12, 0.4, "🔄 5-STAGE PIPELINE", 14, RED, True)
add_textbox(slide3, 0.5, 5.7, 12, 0.5,
            "📁 INGESTED  →  🔍 PARSED  →  🔗 CORRELATED  →  🤖 AI SCORED  →  📄 REPORTED",
            14, NEON_GREEN, True, PP_ALIGN.CENTER)

# ==================== SLIDE 4: FEASIBILITY ====================
print("📝 Filling Slide 4 — Feasibility & Viability...")
slide4 = prs.slides[3]

add_textbox(slide4, 0.5, 0.9, 6, 0.4, "✅ FEASIBILITY", 14, NEON_GREEN, True)
add_multiline(slide4, 0.5, 1.4, 6, 3, [
    ("• Live prototype on Streamlit Cloud", 11, WHITE, False),
    ("• 5 artifact types supported", 11, WHITE, False),
    ("• Real AI trains in <1 second", 11, WHITE, False),
    ("• Offline-capable", 11, WHITE, False),
    ("• 4GB RAM (standard workstation)", 11, WHITE, False),
    ("• Zero configuration", 11, WHITE, False),
])

add_textbox(slide4, 6.7, 0.9, 6, 0.4, "📋 LEGAL ALIGNMENT", 14, CYAN, True)
add_multiline(slide4, 6.7, 1.4, 6, 3, [
    ("📋 BNSS 2023 Section 63 — Hash verification", 11, WHITE, False),
    ("📋 IT Act 2000 Section 65B — Forensic handling", 11, WHITE, False),
    ("📋 I4C Guidelines — Mule account SOP", 11, WHITE, False),
    ("📋 NCRP Standards — Reporting format", 11, WHITE, False),
])

add_textbox(slide4, 0.5, 4.5, 12, 0.4, "🛡️ RISK MITIGATION", 14, RED, True)
add_multiline(slide4, 0.5, 5.0, 12, 2, [
    ("AI Overreliance  →  Human verification required before seizure", 12, WHITE, False),
    ("Data Loss        →  Auto-save case history (SQLite)", 12, WHITE, False),
    ("False Linking    →  Multi-source confirmation required", 12, WHITE, False),
    ("Model Drift      →  Retraining on each new dataset", 12, WHITE, False),
])

# ==================== SLIDE 5: IMPACT ====================
print("📝 Filling Slide 5 — Impact & Benefits...")
slide5 = prs.slides[4]

# Impact columns
add_textbox(slide5, 0.5, 0.9, 4, 0.4, "🚔 LAW ENFORCEMENT", 13, NEON_GREEN, True)
add_multiline(slide5, 0.5, 1.4, 4, 2.5, [
    ("• Faster investigation", 11, WHITE, False),
    ("• 3-4 days → under 10 sec", 11, WHITE, False),
    ("• 150+ cases/officer/day", 11, WHITE, False),
    ("• Offline-capable", 11, WHITE, False),
])

add_textbox(slide5, 4.7, 0.9, 4, 0.4, "👵 VICTIMS", 13, CYAN, True)
add_multiline(slide5, 4.7, 1.4, 4, 2.5, [
    ("• Faster recovery", 11, WHITE, False),
    ("• Golden Hour response", 11, WHITE, False),
    ("• Digital arrest protection", 11, WHITE, False),
    ("• Quick freeze decisions", 11, WHITE, False),
])

add_textbox(slide5, 9.0, 0.9, 4, 0.4, "🏛️ INDORE POLICE", 13, RED, True)
add_multiline(slide5, 9.0, 1.4, 4, 2.5, [
    ("• Aligned with operations", 11, WHITE, False),
    ("• I4C/NCRP ready", 11, WHITE, False),
    ("• Scalable to MP districts", 11, WHITE, False),
])

# Metrics comparison
add_textbox(slide5, 0.5, 4.2, 12, 0.4, "📊 KEY METRICS COMPARISON", 14, NEON_GREEN, True)
metrics = [
    ("Time per case", "3-4 days", "< 10 seconds"),
    ("Entity linking", "Manual", "Automatic"),
    ("Forensic report", "Hours", "Instant PDF"),
    ("Audit trail", "Weak", "SHA-256"),
    ("Scale", "1 case/day", "150+ cases"),
]
y = 4.7
for metric, old, new in metrics:
    add_textbox(slide5, 0.7, y, 4, 0.35, metric, 11, WHITE, True)
    add_textbox(slide5, 5.0, y, 3, 0.35, old, 11, RED)
    add_textbox(slide5, 8.5, y, 3, 0.35, new, 11, NEON_GREEN, True)
    y += 0.35

# ==================== SLIDE 6: REFERENCES ====================
print("📝 Filling Slide 6 — References...")
slide6 = prs.slides[5]

add_textbox(slide6, 0.5, 0.9, 6, 0.4, "📚 RESEARCH & REFERENCES", 13, NEON_GREEN, True)
add_multiline(slide6, 0.5, 1.4, 6, 3, [
    ("• I4C — Mule Account SOP", 11, WHITE, False),
    ("• NCRP — Guidelines", 11, WHITE, False),
    ("• BNSS 2023 — Section 63", 11, WHITE, False),
    ("• IT Act 2000 — Section 65B", 11, WHITE, False),
    ("• RBI MuleHunter.AI", 11, WHITE, False),
    ("• scikit-learn ML Documentation", 11, WHITE, False),
])

add_textbox(slide6, 6.7, 0.9, 6, 0.4, "🔗 TECHNICAL LINKS", 13, CYAN, True)
add_multiline(slide6, 6.7, 1.4, 6, 3, [
    ("💻 GitHub Repository:", 11, WHITE, True),
    ("github.com/Ajaydangi1509/abhedya-mulenet", 10, NEON_GREEN, False),
    ("", 6, WHITE, False),
    ("🌐 Live Application:", 11, WHITE, True),
    ("code-black-abhedya-mulenet.streamlit.app", 10, NEON_GREEN, False),
])

add_textbox(slide6, 0.5, 4.5, 12, 0.4, "📦 DELIVERABLES SUBMITTED", 13, NEON_GREEN, True)
add_multiline(slide6, 0.5, 5.0, 12, 1.5, [
    ("✅ Working Prototype (Streamlit Cloud)   ✅ Source Code (GitHub)", 11, WHITE, False),
    ("✅ Sample Dataset (5 types)              ✅ Demo Video (3 min)", 11, WHITE, False),
    ("✅ Technical Documentation (README)", 11, WHITE, False),
])

# ==================== SLIDE 7: DEMO VIDEO ====================
print("📝 Filling Slide 7 — Demo Video...")
slide7 = prs.slides[6]

add_textbox(slide7, 0.5, 2.5, 12, 0.5, "🎬 DEMO VIDEO LINK", 16, NEON_GREEN, True, PP_ALIGN.CENTER)
add_textbox(slide7, 0.5, 3.2, 12, 0.6,
            "[YouTube / Loom Unlisted Link — to be inserted]",
            14, WHITE, False, PP_ALIGN.CENTER)
add_textbox(slide7, 0.5, 4.2, 12, 0.5,
            "3-minute walkthrough: ingestion → entity linking → graph → report",
            12, MUTED, False, PP_ALIGN.CENTER)

# ==================== SLIDE 8: DELETE INSTRUCTION SLIDE ====================
print("🗑️ Deleting instructions slide...")
# Delete slide 8 (index 7)
xml_slides = prs.slides._sldIdLst
slides_list = list(xml_slides)
if len(slides_list) >= 8:
    xml_slides.remove(slides_list[7])
    print("✅ Instruction slide removed")

# ==================== SAVE ====================
prs.save(OUTPUT_FILE)
print(f"\n✅ Final PPT saved: {OUTPUT_FILE}")
print(f"📊 Total slides: {len(prs.slides)}")
print(f"📍 Location: dhrshti/{OUTPUT_FILE}")
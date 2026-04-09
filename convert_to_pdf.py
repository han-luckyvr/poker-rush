import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ── Colour palette ──────────────────────────────────────────────
NAVY   = colors.HexColor("#0f3460")
RED    = colors.HexColor("#e94560")
DARK   = colors.HexColor("#16213e")
LIGHT  = colors.HexColor("#f4f7fc")
MID    = colors.HexColor("#dde3ec")
WHITE  = colors.white
BLACK  = colors.black
GREY   = colors.HexColor("#888888")
CODE_BG = colors.HexColor("#1a1a2e")
CODE_FG = colors.HexColor("#a8d8ea")
QUOTE_BG = colors.HexColor("#f0f4ff")

# ── Styles ───────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()
    s = {}

    s["title"] = ParagraphStyle(
        "title", fontName="Helvetica-Bold", fontSize=36,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=4,
        letterSpacing=2
    )
    s["subtitle"] = ParagraphStyle(
        "subtitle", fontName="Helvetica", fontSize=13,
        textColor=RED, alignment=TA_CENTER, spaceAfter=30,
        letterSpacing=1
    )
    s["h1"] = ParagraphStyle(
        "h1", fontName="Helvetica-Bold", fontSize=20,
        textColor=NAVY, spaceBefore=28, spaceAfter=8,
        borderPadding=(0, 0, 4, 0)
    )
    s["h2"] = ParagraphStyle(
        "h2", fontName="Helvetica-Bold", fontSize=14,
        textColor=DARK, spaceBefore=20, spaceAfter=6,
        leftIndent=10,
        borderPadding=(0, 0, 0, 0)
    )
    s["h3"] = ParagraphStyle(
        "h3", fontName="Helvetica-Bold", fontSize=12,
        textColor=NAVY, spaceBefore=14, spaceAfter=4
    )
    s["h4"] = ParagraphStyle(
        "h4", fontName="Helvetica-Bold", fontSize=10,
        textColor=RED, spaceBefore=10, spaceAfter=4,
    )
    s["body"] = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=10,
        textColor=BLACK, leading=16, spaceAfter=8
    )
    s["bullet"] = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=10,
        textColor=BLACK, leading=15, leftIndent=16,
        bulletIndent=4, spaceAfter=3
    )
    s["code"] = ParagraphStyle(
        "code", fontName="Courier", fontSize=8.5,
        textColor=CODE_FG, backColor=CODE_BG,
        leading=13, leftIndent=8, rightIndent=8,
        spaceBefore=8, spaceAfter=8,
        borderPadding=8
    )
    s["blockquote"] = ParagraphStyle(
        "blockquote", fontName="Helvetica-Oblique", fontSize=9.5,
        textColor=colors.HexColor("#444444"), backColor=QUOTE_BG,
        leading=14, leftIndent=12, rightIndent=8,
        spaceBefore=6, spaceAfter=6,
        borderPadding=8
    )
    s["toc"] = ParagraphStyle(
        "toc", fontName="Helvetica", fontSize=10,
        textColor=NAVY, leading=18, leftIndent=16
    )
    return s

# ── Table helpers ─────────────────────────────────────────────────
def make_table(rows):
    if not rows:
        return None
    col_count = max(len(r) for r in rows)
    page_w = A4[0] - 36*mm
    col_w = page_w / col_count

    t = Table(rows, colWidths=[col_w] * col_count, repeatRows=1)
    style = TableStyle([
        # Header row
        ("BACKGROUND",  (0,0), (-1,0), NAVY),
        ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
        ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",    (0,0), (-1,0), 9),
        ("BOTTOMPADDING",(0,0),(-1,0), 7),
        ("TOPPADDING",  (0,0), (-1,0), 7),
        # Body rows
        ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
        ("FONTSIZE",    (0,1), (-1,-1), 9),
        ("TOPPADDING",  (0,1), (-1,-1), 5),
        ("BOTTOMPADDING",(0,1),(-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0), (-1,-1), 10),
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
        # Alternating rows
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, LIGHT]),
        # Grid
        ("LINEBELOW",   (0,0), (-1,-1), 0.4, MID),
        ("BOX",         (0,0), (-1,-1), 0.6, MID),
    ])
    t.setStyle(style)
    return t

# ── Markdown parser ───────────────────────────────────────────────
def parse_md(text, styles):
    """Very lightweight Markdown → ReportLab flowables converter."""
    flowables = []
    lines = text.splitlines()
    i = 0

    is_title_done = False

    while i < len(lines):
        line = lines[i]

        # ── Fenced code block ─────────────────────────────────────
        if line.strip().startswith("```"):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code_text = "\n".join(code_lines)
            # Escape for paragraph
            code_text = code_text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
            code_text = code_text.replace("\n", "<br/>").replace(" ", "&nbsp;")
            flowables.append(Paragraph(code_text, styles["code"]))
            i += 1
            continue

        # ── Horizontal rule ───────────────────────────────────────
        if re.match(r'^-{3,}$', line.strip()) or re.match(r'^\*{3,}$', line.strip()):
            flowables.append(Spacer(1, 4))
            flowables.append(HRFlowable(width="100%", thickness=1.5, color=RED))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # ── Table ─────────────────────────────────────────────────
        if "|" in line and line.strip().startswith("|"):
            table_lines = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip().startswith("|"):
                row = lines[i].strip().strip("|")
                cells = [c.strip() for c in row.split("|")]
                table_lines.append(cells)
                i += 1
            # Remove separator row (---)
            table_lines = [r for r in table_lines if not all(re.match(r'^[-:]+$', c) for c in r if c)]
            if table_lines:
                # Convert cells to Paragraphs
                para_rows = []
                for ri, row in enumerate(table_lines):
                    style = ParagraphStyle(
                        f"cell_{ri}", fontName="Helvetica-Bold" if ri == 0 else "Helvetica",
                        fontSize=9, textColor=WHITE if ri == 0 else BLACK, leading=13
                    )
                    para_rows.append([Paragraph(escape_inline(c), style) for c in row])
                t = make_table(para_rows)
                if t:
                    flowables.append(Spacer(1, 6))
                    flowables.append(t)
                    flowables.append(Spacer(1, 6))
            continue

        # ── Headings ──────────────────────────────────────────────
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            level = len(m.group(1))
            text_content = escape_inline(m.group(2).strip())
            if level == 1:
                if not is_title_done:
                    flowables.append(Spacer(1, 30*mm))
                    flowables.append(Paragraph(text_content, styles["title"]))
                    is_title_done = True
                else:
                    flowables.append(PageBreak())
                    flowables.append(HRFlowable(width="100%", thickness=3, color=RED, spaceAfter=6))
                    flowables.append(Paragraph(text_content, styles["h1"]))
            elif level == 2:
                # First h2 after the title (subtitle)
                if flowables and isinstance(flowables[-1], Paragraph) and flowables[-1].style == styles["title"]:
                    flowables.append(Paragraph(text_content, styles["subtitle"]))
                else:
                    flowables.append(Paragraph(text_content, styles["h2"]))
                    flowables.append(HRFlowable(width=4*mm, thickness=4, color=RED, spaceAfter=4))
            elif level == 3:
                flowables.append(Paragraph(text_content, styles["h3"]))
            elif level == 4:
                flowables.append(Paragraph(text_content, styles["h4"]))
            i += 1
            continue

        # ── Blockquote ────────────────────────────────────────────
        if line.strip().startswith(">"):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            bq_text = " ".join(bq_lines)
            flowables.append(Paragraph(escape_inline(bq_text), styles["blockquote"]))
            continue

        # ── Bullet list ───────────────────────────────────────────
        if re.match(r'^(\s*[-*+])\s+', line):
            while i < len(lines) and re.match(r'^(\s*[-*+])\s+', lines[i]):
                item = re.sub(r'^\s*[-*+]\s+', '', lines[i])
                flowables.append(Paragraph(f"• {escape_inline(item)}", styles["bullet"]))
                i += 1
            continue

        # ── Numbered list ─────────────────────────────────────────
        if re.match(r'^\d+\.\s+', line):
            num = 1
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i]):
                item = re.sub(r'^\d+\.\s+', '', lines[i])
                flowables.append(Paragraph(f"{num}. {escape_inline(item)}", styles["bullet"]))
                num += 1
                i += 1
            continue

        # ── Blank line ────────────────────────────────────────────
        if not line.strip():
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # ── Normal paragraph ──────────────────────────────────────
        para_lines = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^#{1,4}\s', lines[i]) \
              and not lines[i].strip().startswith("|") and not re.match(r'^[-*+]\s', lines[i]) \
              and not re.match(r'^\d+\.\s', lines[i]) and not lines[i].strip().startswith(">") \
              and not lines[i].strip().startswith("```") and not re.match(r'^-{3,}$', lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            full = " ".join(para_lines)
            flowables.append(Paragraph(escape_inline(full), styles["body"]))

    return flowables


def escape_inline(text):
    """Handle bold/italic/code inline markdown and XML escaping."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<font name="Courier" size="9">\1</font>', text)
    # Strip markdown links [text](url) → text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text


# ── Page number footer ────────────────────────────────────────────
def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GREY)
    page_num = canvas.getPageNumber()
    canvas.drawRightString(A4[0] - 18*mm, 12*mm, str(page_num))
    canvas.drawString(18*mm, 12*mm, "Poker Rush — Game Design Document v0.1")
    canvas.setStrokeColor(MID)
    canvas.line(18*mm, 16*mm, A4[0] - 18*mm, 16*mm)
    canvas.restoreState()


# ── Main ──────────────────────────────────────────────────────────
def main():
    md_path  = "D:/Claude Jam II/Game Design Document - Poker Rush.md"
    pdf_path = "D:/Claude Jam II/Game Design Document - Poker Rush.pdf"

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    styles = build_styles()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=20*mm, bottomMargin=24*mm,
        title="Poker Rush — Game Design Document",
        author="Claude Jam II",
    )

    flowables = parse_md(md_text, styles)
    doc.build(flowables, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF saved to: {pdf_path}")


if __name__ == "__main__":
    main()

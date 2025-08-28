#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import sys, textwrap

def render(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    x, y = 2*cm, height-2*cm
    for para in text.split('\n\n'):
        wrapped = textwrap.wrap(para, width=95)
        for line in wrapped:
            if y < 3*cm:
                c.showPage(); y = height-2*cm
            c.drawString(x, y, line)
            y -= 14
        y -= 10
    c.save()

if __name__ == '__main__':
    md = sys.argv[1] if len(sys.argv)>1 else 'reports/templates/weekly_report.md'
    pdf = sys.argv[2] if len(sys.argv)>2 else 'reports/Weekly_Climate_Report.pdf'
    render(md, pdf)
    print('Wrote', pdf)

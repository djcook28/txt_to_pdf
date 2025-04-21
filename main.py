from pathlib import Path
import glob
from fpdf import FPDF

filepaths = glob.glob("Text Files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem


    pdf.set_font(family="Times", size=16, style='B')
    pdf.set_text_color(0, 0, 0)

    pdf.add_page()
    pdf.cell(w=50, h=16, txt=f'{filename.title()}', ln=1)

    with open(filepath, "r") as file:
        pdf.set_font(family="Times", size=8, style='B')
        pdf.multi_cell(w=0, h=8, txt=file.read())

pdf.output("PDFs/output.pdf")
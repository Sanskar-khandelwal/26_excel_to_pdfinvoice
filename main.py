import pandas as pd 
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath)
    pdf = FPDF(
        orientation="P",
        unit="mm",
        format="A4"
    )
    pdf.add_page()
    filename = Path(filepath).stem 
    invoice_no = filename.split("-")[0].split(" ")[1]
    pdf.set_font(family="helvetica", style="B", size=16)
    pdf.cell(w=55, h= 10, border=1, ln=1, align="L", txt=f"Invoice No:{invoice_no}")
    pdf.output(f"PDFs/{filename}.pdf")
   
    
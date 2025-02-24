import pandas as pd 
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    
    pdf = FPDF(
        orientation="P",
        unit="mm",
        format="A4"
    )
    pdf.add_page()
    
    filename = Path(filepath).stem 
    invoice_no, date = filename.split("-")
    

    pdf.set_font(family="helvetica", style="B", size=16)
    pdf.cell(w=65, h= 10, ln=1, align="L", txt=f"Invoice No:{invoice_no}")
    pdf.cell(w=55, h= 10, ln=1, align="L", txt=f"Date:{date}")
    
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(list(df.columns))
    for index, item in enumerate(list(df.columns)):
        pdf.set_font(family="Helvetica", size=9, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(h=8, w=60 if index == 1 else 32, txt=item.replace("_", " ").title(), border=1, ln= 1 if index == 4 else 0)
        

    for index, row in df.iterrows():
        pdf.set_font(family="Helvetica", size=9)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=32, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=60, h= 8, txt=row["product_name"], border=1)
        pdf.cell(w=32, h= 8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=32, h= 8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=32, h= 8, txt=str(row["total_price"]), border=1, ln=1)
    
    total_price =  df["total_price"].sum()
    pdf.cell(w=32, h=8, txt='', border=1)
    pdf.cell(w=60, h= 8, txt="", border=1)
    pdf.cell(w=32, h= 8, txt="", border=1)
    pdf.cell(w=32, h= 8, txt="", border=1)
    pdf.set_font(family="Helvetica", size=9, style="B")
    pdf.cell(w=32, h= 8, txt=str(total_price), border=1, ln=1)

    pdf.set_font(family="Helvetica", size=12, style="B")
    pdf.cell(w=30, h=16, txt=f"The Total price is {total_price}", ln=1 )

    pdf.set_font(family="Helvetica", size=15, style="B")
    pdf.cell(w=30, ln=1, h=20)
    pdf.cell(w=30, h=8, txt=f"Maruty Polymath")

    pdf.output(f"PDFs/{filename}.pdf")
    
        
     
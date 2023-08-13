from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv', sep=',')

pdf = FPDF(orientation='portrait', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L',
             ln=1)
    pdf.line(10, 21, 200, 21)

    #Set footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=str(1), align='R')

    page_num = 2

    for i in range(row['Pages']-1):
        pdf.add_page()

        # Set footer
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=str(page_num), align='R')
        page_num += 1

pdf.output('output_file.pdf')

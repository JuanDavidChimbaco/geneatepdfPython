from fpdf import FPDF

pdf = FPDF('P', 'mm', 'letter')
# (P=vertical L=horizontal, medidas, tipo de hoja)
pdf.add_page()
pdf.image('logoSena.png',180,10,20)
# ('Ruta', eje x,eje y, tamaño)
pdf.set_font('Arial','B',16)
pdf.cell(40,10,'Hola Mundo',1,0,'R')
pdf.ln()
pdf.set_font('Arial','',22)
pdf.set_fill_color(255,0,255)
pdf.set_text_color(255,255,255)
pdf.cell(80,10,'Hello Word',1,0,'L',True) # el true es para aplicar el color

pdf.set_y(-21)
pdf.set_text_color(0,0,0)
pdf.set_font('Arial','',10)
pdf.cell(0, 0, 'Powered by FPDF.', 0, 1, 'C')
# (x,y, 'texto', borde , y , justificacion)
pdf.output('tuto.pdf','F')
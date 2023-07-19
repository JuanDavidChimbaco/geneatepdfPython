from fpdf import FPDF

class PDF(FPDF):
    
    def tabla1(self):
        # encabezado
        self.set_font('Arial', 'B', 10)
        self.cell(20,15,"CODIGO",1,0,'C')
        self.cell(40,15,"PRODUCTO",1,0,'C')
        self.cell(20,15,"PRECIO",1,0,'C')
        
        # datos
        for i in range(1,4):
            self.ln()
            self.cell(20,15,"12345",1,0,'C')
            self.cell(40,15,"TV LG",1,0,'L')
            self.cell(20,15,"1500000",1,0,'R')
            
    def tabla2(self):
        # encabezado
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(0,150,80)
        self.set_text_color(255,255,250)
        self.cell(20,15,"CODIGO",1,0,'C',True)
        self.cell(40,15,"PRODUCTO",1,0,'C',True)
        self.cell(20,15,"PRECIO",1,0,'C',True)
        
        # datos
        for i in range(1,4):
            self.ln()
            self.set_text_color(0,0,0)
            self.cell(20,15,"12345",1,0,'C')
            self.cell(40,15,"TV LG",1,0,'L')
            self.cell(20,15,"1500000",1,0,'R')
        
        
pdf = PDF()

pdf.add_page()

pdf.tabla2()
pdf.set_author('David Chimbaco')
pdf.output('tabla.pdf','F')
from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self.header()
        self.body(name)

    def header(self):
        self._pdf.set_text_color(0,0,0)
        self._pdf.set_font("Times", size=30)
        # Printing title:
        self._pdf.cell(0, 0, text="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        # Performing a line break:
        self._pdf.ln(20)

    def body(self, name):
        self._pdf.set_text_color(255,255,255)
        self._pdf.set_font("Times", size=30)

        # Rendering image:
        self._pdf.image("shirtificate.png",'C', w=self._pdf.epw)

        # Printing on shirt:
        self._pdf.cell(0, -250, text=f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')

    def out(self,shirt):
        self._pdf.output(shirt)

name = input("Name: ")
shirt = PDF(name)
shirt.out("shirtificate.pdf")

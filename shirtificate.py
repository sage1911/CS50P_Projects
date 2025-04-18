from fpdf import FPDF
from fpdf.enums import XPos, YPos

class Shirtificate(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)

def create_shirtificate(name):
    pdf = Shirtificate()
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    
    # Add shirt image
    image_path = "shirtificate.png"
    pdf.image(image_path, x=30, y=70, w=150)
    
    # Add name text
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.text(x=65, y=140, text=f"{name} took CS50")
    
    # Output PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("Name: ")
    create_shirtificate(name)

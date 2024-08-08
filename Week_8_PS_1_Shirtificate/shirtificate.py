from fpdf import FPDF

name = input("Name: ")                                                  # taking input 
pdf = FPDF(orientation="P", unit="mm", format="A4")                     # Creating pdf 
pdf.add_page()                                                          # Adding page 
pdf.set_font('helvetica', 'B', 45)                                      # setting up the font,size and style 
# Writting up the Title
pdf.cell(190, 62, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
pdf.image("shirtificate.png", w=pdf.epw)                                # Adding shirt picture 
pdf.set_font_size(28)                                                   # setting up the size of text
pdf.set_text_color(255, 255, 255)                                       # setting up the color of text                
pdf.text(50, 150, text=f"{name} took CS50")                             # writting the text
pdf.output("shirtificate.pdf")                                          # Saving the pdf  

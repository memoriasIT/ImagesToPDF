from fpdf import FPDF
from PIL import Image
from datetime import date
from os import listdir

print("Selecting images:")
imagelist = listdir("images")
print(str(len(imagelist)) + " images selected")

cover = Image.open("images/" + imagelist[0])
width, height = cover.size
pdf = FPDF(unit = "pt", format = [width, height])

for image in imagelist:
    pdf.add_page()
    pdf.image("images/" + image,0,0)

pdf.output(date.today().strftime("%d-%m-%Y")+" OUTPUT.pdf", "F")
print("File was created successfully!")

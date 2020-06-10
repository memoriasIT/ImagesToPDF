from fpdf import FPDF
from PIL import Image
from datetime import date
from os import listdir

imagelist = listdir("images")
print(imagelist)

cover = Image.open("images/" + imagelist[0])
width, height = cover.size
pdf = FPDF(unit = "pt", format = [width, height])

for image in imagelist:
    pdf.add_page()
    pdf.image("images/" + image,0,0)
    print("image/" + image)

pdf.output(date.today().strftime("%d-%m-%Y")+" OUTPUT.pdf", "F")

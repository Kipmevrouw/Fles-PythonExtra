from PIL import Image, ImageFont, ImageDraw

afbeelding = Image.open("peanut.jpg")

breedte = afbeelding.width
hoogte = afbeelding.height

lettertype = ImageFont.truetype("impact.ttf", 40)

tekengebied = ImageDraw.Draw(afbeelding)

tekst = "Hoi\npeanut"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))
afbeelding.show()
afbeelding.save("peanut.jpg")

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))

tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

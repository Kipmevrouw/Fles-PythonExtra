from PIL import Image

afbeelding = Image.open("WIT_PNG.PNG")

afbeelding.show()

breedte = afbeelding.width
hoogte = afbeelding.height

print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + "pixels hoog")

print(afbeelding.format, afbeelding.size, afbeelding.mode)

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

nieuwe_afmeting = (helft_breedte, helft_hoogte)


kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)


kleinere_afbeelding.save('WIT_KLEIN.PNG')


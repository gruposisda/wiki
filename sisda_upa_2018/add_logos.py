from PIL import Image

input_image = 'tologo.jpg'

photo = Image.open(input_image)
logo_upa = Image.open('logos/upa.png')
logo_upa.thumbnail((164,162),Image.ANTIALIAS)
logo_sisda = Image.open('logos/sisda.png')
logo_sisda.thumbnail((164,162),Image.ANTIALIAS)
logo_feagri = Image.open('logos/feagri.png')

photo.paste(logo_sisda,(280,2200))
photo.paste(logo_feagri,(1780,2200))
photo.paste(logo_upa,(3000,2200))

photo.save('logoed.jpg')

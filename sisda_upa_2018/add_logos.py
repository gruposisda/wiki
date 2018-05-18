from PIL import Image

print('Horas:')
hour = input()
print('Minutos:')
minute = input()
img_base_name = './out/image_{}-{}.jpg'
input_image = img_base_name.format(str(hour),str(minute))


photo = Image.open(input_image)
logo = Image.open('logos/logos_red.png')
photo.paste(logo,(2208,2150))

output_image = './out/image_{}-{}.'
output_image = output_image.format(str(hour),str(minute))+'_logo.jpg'
photo.save(output_image)

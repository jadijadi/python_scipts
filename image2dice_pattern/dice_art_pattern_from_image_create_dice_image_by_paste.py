from PIL import Image, ImageOps, ImageDraw

dicew = 300
quality = 6 # minimum = 1, maximum = resolution of your dice image / dicesize
im = Image.open("image.png")
im = ImageOps.grayscale(im)
im = ImageOps.equalize(im)

diceh = im.height / im.width * dicew

dicesize = int(im.width / dicew)

nim = Image.new("L", (im.width * quality, im.height * quality), 'white')
# nimd = ImageDraw.Draw(nim)

dices = []
for i in range(1, 7):
    dim = Image.open("dice/" + str(i) + ".jpg")
    dim = dim.resize((dicesize * quality, dicesize * quality), Image.ANTIALIAS)
    dim = ImageOps.equalize(dim)
    dices.append(dim)

for y in range(0, im.height-dicesize, dicesize):
    for x in range(0, im.width-dicesize, dicesize):
        thisSectorColor = 0
        for dicex in range(0, dicesize):
            for dicey in range(0, dicesize): 
                thisSectorColor += im.getpixel((x+dicex, y+dicey))
        thisSectorColor = thisSectorColor / (dicesize **2 )
        
        #nimd.rectangle(((x, y),(x+dicesize, y+dicesize)), thisSectorColor)
        diceNumber = (255-thisSectorColor) * 5 / 255 + 1
        #print (x, y, thisSectorColor, diceNumber)
        # print diceNumber,
        nim.paste(dices[diceNumber - 1], (x * quality, y * quality))
    # print
nim.save("diceimage.png")
# nim.show()

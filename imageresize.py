
from PIL import Image, ImageFilter

# open the image
image = Image.open('testimg.webp')

# resize image to 500 x 228
image = image.resize((500, 228))

# paste image in middle of new image
new_image = Image.new('RGB', (500, 228))
new_image.paste(image, (int(500/2 - image.width/2), int(228/2 - image.height/2)))

# apply gaussian blur with a radius of 5
#new_image = new_image.filter(ImageFilter.GaussianBlur(radius = 5))

# save the new image
new_image.save('new_image.webp')





def blur_image(imagename):
    from PIL import Image, ImageFilter

    # open the image
    image = Image.open(imagename + '.webp')

    # resize image to 500 x 228
    image = image.resize((500, 228))

    # paste image in middle of new image
    new_image = Image.new('RGB', (500, 228))
    new_image.paste(image, (int(500/2 - image.width/2), int(228/2 - image.height/2)))

    # apply gaussian blur with a radius of 5
    #new_image = new_image.filter(ImageFilter.GaussianBlur(radius = 5))

    # save the new image
    new_image.save(imagename + '.webp')
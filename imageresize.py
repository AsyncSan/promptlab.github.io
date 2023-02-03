
#from PIL import Image, ImageFilter
# open the image
#image = Image.open('testimg.webp')
# resize image to 500 x 228
#image = image.resize((500, 228))
# paste image in middle of new image
#new_image = Image.new('RGB', (500, 228))
#new_image.paste(image, (int(500/2 - image.width/2), int(228/2 - image.height/2)))
# apply gaussian blur with a radius of 5
#new_image = new_image.filter(ImageFilter.GaussianBlur(radius = 5))
# save the new image
#new_image.save('new_image.webp')

###
'''
#############
# Rewrite
import glob
from PIL import Image, ImageFilter

for filename in glob.glob('*.jpg')+glob.glob('*.png'): # Look for all files that are jpg or png in the working directory 
    image = Image.open(filename) # open the image
    image = image.resize((800 , 450)) # resize image to 800 x 450
    new_image = Image.new('RGB', (800 , 450)) # paste image in middle of new image
    new_image.paste(image, (int(800 /2 - image.width/2), int(450/2 - image.height/2))) # apply gaussian blur with a radius of 5
    #new_image = new_image.filter(ImageFilter.GaussianBlur(radius = 5))
    new_image.save(filename, 'webp', quality=70) # save the new image as webp with 70% quality
'''

# Rewrite
import glob
from PIL import Image, ImageFilter
import os
#Loop over the files in the current directory
for filename in os.listdir("."): 
   #Check if the file is a JPEG image
   print(filename)
   if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
     #Open and resize the image (800 x 450)
     image = Image.open(filename) 
     image = image.resize((800 , 450))   
     #Save it as webp, compressed 70%        
     image.save(filename + ".webp", optimize=True, quality=70)
     os.remove(filename)

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
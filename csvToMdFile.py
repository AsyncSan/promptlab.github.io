import csv
import io
import requests
from PIL import Image
import os
import replicate
import json
from PIL import Image, ImageFilter


def download_and_convert_image(image_url, title, filename):

    print("Image title:  " + title)

    title = title.replace(' ', '-')
    title = ''.join(e for e in title if e.isalnum())

    # Use requests to download the image from the link
    response = requests.get(image_url)
    open(f"assets\\img\\blogtitleimages\\{title}.png", "wb").write(response.content)
    # Open the image using Pillow
    img = Image.open(f"assets\\img\\blogtitleimages\\{title}.png")

    # resize image to 500 x 228
    img = img.resize((500, 228))

    # paste image in middle of new image
    new_image = Image.new('RGB', (500, 228))
    new_image.paste(img, (int(500/2 - img.width/2), int(228/2 - img.height/2)))


    # Convert the image to webp format
    new_image.save(f"assets\\img\\blogtitleimages\\{title}.webp", "webp")
    # Write the image to md_file with the relative link
    #with io.open(filename, 'a', encoding='utf-8') as md_file:
    #    md_file.write(f"![{title}](assets\\img\blogtitleimages\\{title}.webp)\n")
    # Delete the PNG image
    os.remove(f"assets\\img\\blogtitleimages\\{title}.png")

    return (f"/assets/img/blogtitleimages/{title}.webp")



#Dont forget to save your API key as global variable
def get_image_link(prompt):
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")
    img_url = version.predict(prompt=prompt)
    img_url_string = ''.join(img_url)
    print(img_url_string)
    return img_url_string



def blur_image(imagename):
    # open the image{title}.png"
    image = Image.open(f"assets\\img\\blogtitleimages\\{imagename}.webp")

    # resize image to 500 x 228
    image = image.resize((500, 228))

    # paste image in middle of new image
    new_image = Image.new('RGB', (500, 228))
    new_image.paste(image, (int(500/2 - image.width/2), int(228/2 - image.height/2)))

    # apply gaussian blur with a radius of 5
    #new_image = new_image.filter(ImageFilter.GaussianBlur(radius = 5))

    # save the new image
    new_image.save(imagename + '.webp')



with open('input.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        act = row[0]
        prompt = row[1]
        
        #filename = f"{act}.md"
        filename = f"2023-01-24-{act}.md".replace("/", "")
        filename = filename.replace(" ", "-")

        try:
            # Get the image link
            img_url_string = get_image_link(prompt)
        except:
            # Skip the current iteration
            continue

        image_url = get_image_link(act)

        image_location = download_and_convert_image(image_url, act, filename)
        print("Image location:  " + image_location)
        #blur_image(imagename)

        with io.open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write("---\n")
            md_file.write("date: 2023-01-24 00:26:50\n")
            md_file.write("layout: post\n")
            md_file.write(f"title: Behave as a {act}\n")
            md_file.write(f"subtitle: Prompt to make the Chatbot behave like a {act}\n")
            md_file.write(f"description: Prompt to make the Chatbot behave like a {act}\n")
            md_file.write(f"image: {image_location}\n")
            md_file.write(f"optimized_image: {image_location}\n")
            md_file.write("category: fun/impersonation\n")
            md_file.write("tags:\n")
            md_file.write("  - act\n")
            md_file.write("  - acting\n")
            md_file.write("  - impersonation\n")
            md_file.write("  - interaction\n")
            md_file.write("  - fun\n")
            md_file.write("  - Chatbot Prompt\n")
            md_file.write("author: rene\n")
            md_file.write("paginate: true\n")
            md_file.write("---\n")
            md_file.write(f"> Want to have some fun or teach your students in a new way?\nUse this prompt to make learning as interactive like never before.\n\n")
            md_file.write(f"{prompt}\n")

'''
        with io.open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write("---\n")
            md_file.write("date: 2023-01-24 00:26:50\n")
            md_file.write("layout: post\n")
            md_file.write(f"title: Behave as a {act}\n")
            md_file.write(f"subtitle: Prompt to make the Chatbot behave like a {act}\n")
            md_file.write(f"description: Prompt to make the Chatbot behave like a {act}\n")
            md_file.write(f"image: {image_location}\n")
            md_file.write(f"optimized_image: {image_location}\n")
            md_file.write("category: fun/impersonation\n")
            md_file.write("tags:\n")
            md_file.write("  - act\n")
            md_file.write("  - acting\n")
            md_file.write("  - impersonation\n")
            md_file.write("  - interaction\n")
            md_file.write("  - fun\n")
            md_file.write("  - Chatbot Prompt\n")
            md_file.write("author: rene\n")
            md_file.write("paginate: true\n")
            md_file.write("---\n")
            md_file.write(f"> Want to have some fun or teach your students in a new way?\nUse this prompt to make learning as interactive like never before.\n\n")
            md_file.write(f"{prompt}\n")
## Heading 2
            
'''
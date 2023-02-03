import csv
import io
import requests
from PIL import Image
import os
import replicate
import json
from datetime import datetime
from PIL import Image, ImageFilter
import openai
import time


def get_promptanswer_from_openai(prompt):
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    # Use join() to concatenate the API endpoint
    api_endpoint = '/'.join(["https://api.openai.com/v1/engines/text-davinci-003/completions"])

    prompt = prompt + " (if you return a list, format it as a html list)"

    # Define the parameters for the API call
    params = {
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7,
        "frequency_penalty": 0.2,
        "presence_penalty": 0.65
    }

    # Set up the headers for the API call
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Send the API request and store the response
    response = requests.post(api_endpoint, json=params, headers=headers)
    response_dict = response.json()
    print(response_dict)
    answer_text = response_dict['choices'][0]['text']

    return answer_text


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



with open('promptstopost.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        title = row[0]
        prompt = row[1]
        answer = row[2]
        category = row[3]
        tags = row[4]

        list_of_tags = tags.split(",")
        list_of_tags = [item.strip() for item in list_of_tags if item.strip()]


        #filename = f"{title}.md"
        filename = f"2023-02-02-{title}.md".replace("/", "")
        filename = filename.replace(" ", "-")


        try:
            answer = get_promptanswer_from_openai(prompt)
        except:
            print("Skipped current because of openAI error")
            time.sleep(10)

        try:
            # Get the image link
            img_url_string = get_image_link(prompt)
        except:
            # Skip the current iteration
            print("Skipped current because of image gen error")
            continue

        image_url = get_image_link(title)

        image_location = download_and_convert_image(image_url, title, filename)
        print("Image location:  " + image_location)
        #blur_image(imagename)


        # Get the current time
        current_time = datetime.utcnow()

        # Format the time as a string in the desired format
        current_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        with io.open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write("---\n")
            md_file.write(f"date: {current_time}\n")
            md_file.write("layout: post\n")
            md_file.write(f"title: {title}\n")
            md_file.write(f"subtitle: A prompt to accelerate your {category}\n")
            md_file.write(f"description: Prompt to help you with {category} \n")
            md_file.write(f"image: {image_location}\n")
            md_file.write(f"optimized_image: {image_location}\n")
            md_file.write(f"category: {category}\n")
            md_file.write("tags:\n")
            for element in list_of_tags:
                md_file.write("  - {}\n".format(element))
            md_file.write("author: rene\n")
            md_file.write("---\n\n")
            md_file.write("## Prompt\n\n")
            md_file.write("  <div class='promptinnerdivtop'>\n")
            md_file.write("    <div class='prompttextdiv'>\n")
            md_file.write(f"    <p>{prompt}</p>\n")
            md_file.write("    </div>\n")
            md_file.write("  </div>\n\n\n")
            md_file.write("## Example answer\n")
            md_file.write("  <div class='promptinnerdivbottom' >\n")
            md_file.write("    <div class='prompttextdiv'>\n")
            md_file.write(f"    <p>{answer}</p>\n")
            md_file.write("    </div>\n")
            md_file.write("  </div>\n")


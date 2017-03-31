import os
from PIL import Image, ImageDraw, ImageFont
import csv
SQUARE_FIT_SIZE = 100
LOGO_FILENAME = 'csvconfv3.png'
font_file = '/Library/Fonts/FiraSans-Regular.otf'
font = ImageFont.truetype(font_file, 48)
logoIm = Image.open(LOGO_FILENAME).convert("RGBA")
logoWidth, logoHeight = logoIm.size


bg_filename = 'bluebackground.jpg'

with open('speakers-2017.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        name = row[0]
        title = row[1]
        link = row[2]

        if ".jpeg" in link:
            ext = '.jpeg'
        elif '.png' in link:
            ext = '.png'
        else:
            ext = '.jpg'
            
        filename = name + ext 
        print "filename", filename
        if link != "":

            im = Image.open(bg_filename).convert("RGBA")
            headshot = Image.open('speakers-2017/resize_image/' + filename).convert("RGBA")
            width = 800
            height = 200
            draw = ImageDraw.Draw(im)
            if len(title) <= 65:
                smaller_font_size = 18
            elif len(title) >= 83:
                smaller_font_size = 13
            elif len(title) > 66 and len(title) < 82:
                smaller_font_size = 14
            else:
                smaller_font_size = 16
            smaller_font = ImageFont.truetype(font_file, smaller_font_size)
            # Add logo.
            print 'Adding %s to %s...' %(headshot, bg_filename)
            new_width = width - logoWidth - 10
            print new_width
            new_height = height - logoHeight
            print new_height

            draw.text((210, 20),name,(255,255,255),font=font)
            draw.text((210,80), title, (255,255,255),font=smaller_font)
            im.paste(headshot,(40,20), headshot)
            im.paste(logoIm, (new_width, new_height), logoIm)
            im.resize((400,100), Image.ANTIALIAS)
            im.show()
            # Save changes.
            im.save('twitter/'+'tcard_'+ filename)
        else:
            continue
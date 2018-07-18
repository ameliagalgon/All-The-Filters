from PIL import Image

def load_img(file):
    return Image.open(file)

def show_img(image):
    image.show()

def save_img(image, filename):
    image.save(filename)

def obamicon(image):
    print("In obamicon")
    #pixels = image.getdata()
    #print(pixels)
    for i in range(image.height):
        for j in range(image.width):
            #print(image.getpixel((j,i)))
            pixel_sum = image.getpixel((j,i))[0] + image.getpixel((j,i))[1] + image.getpixel((j,i))[2]
            if (pixel_sum > 500):
                print(pixel_sum)

            if(pixel_sum < 182):
                #make the pixel a dark blue
                image.putpixel( (j,i), (0, 51, 76) )
            elif(pixel_sum >= 182 & pixel_sum < 364):
                #make the pixel a red
                image.putpixel( (j,i), (217, 26, 33) )
            elif(pixel_sum >= 364 & pixel_sum < 545):
                #make the pixel a light blue
                image.putpixel( (j,i), (112, 150, 158) )
            else: #greater or equal to 545
                #make the pixel a yellow
                image.putpixel( (j,i), (252, 227, 166) )

    return image

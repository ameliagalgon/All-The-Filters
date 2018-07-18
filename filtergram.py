import filters
def main():
    image = filters.load_img("owl.jpg")
    filters.save_img(image, "owl_2.jpg")

    filter_image = filters.obamicon(image)
    filters.show_img(filter_image)

    #save the image
    #filters.save_img(filter_image, "filtered_image.jpg")

if __name__ == "__main__":
    main()

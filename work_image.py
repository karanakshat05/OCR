from PIL import Image
print(5)
img_file="data/page_01.jpg"
img = Image.open(img_file)
print(img)
print(img.size)
img.show()
img.save("temp/page_01.jpg")
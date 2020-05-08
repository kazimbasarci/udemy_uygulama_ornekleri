from PIL import Image
img = Image.open('python.jpg').convert('L')
img.save('python_ignore.jpg')


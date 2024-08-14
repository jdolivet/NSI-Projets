from captcha.image import ImageCaptcha
from random import choice
from PIL import Image

n = int(input("Captcha amount > "))
l = int(input("Captcha length > "))
w = int(input("Captcha width > "))
h = int(input("Captcha height > "))

captchas = {}

for i in range(n):
    string = ""
    for i in range(l):
        string += choice("1234567890qwertyuiopasdfghjklzxcvbnm")
    captchas[string] = ImageCaptcha(width = w, height = h, fonts=["arial.ttf"])
    captchas[string].generate(string)
    captchas[string].write(string, f'{string}.png')
    img = Image.open(f'{string}.png').convert('L')
    img.save(f'{string}.png')
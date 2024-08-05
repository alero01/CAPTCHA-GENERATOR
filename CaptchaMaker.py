from captcha.image import ImageCaptcha

import random
import string

N = 7
 
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
 
# print result in terminal
print("The generated random string : " + str(res))
 
# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)
 
# Image captcha text
captcha_text = res
 
# generate the image of the given text
data = image.generate(captcha_text)  
 
# write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA.png')

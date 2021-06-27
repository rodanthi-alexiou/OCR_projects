from PIL import Image
import io
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# This portion is part of my test code
byteImgIO = io.BytesIO()
byteImg = Image.open("C:/Users/Rodanthi/Documents/GitHub/OCR_projects/song1.jpg")
byteImg.save(byteImgIO, "PNG")
byteImgIO.seek(0)
byteImg = byteImgIO.read()


dataBytesIO = io.BytesIO(byteImg)
Image.open(dataBytesIO)
#plt.figure(figsize=(5, 5))
#ax = plt.imshow(byteImgIO, alpha=0.5)
#plt.show()
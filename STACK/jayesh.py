import os

from pptx import Presentation
from pptx.util import Inches
os.chdir('E:\python\python_script')
from wand.display import display
def convert(i):
    with Image(filename = img[i]) as nike :
        nike.transform(resize = 'x200')
        nike.save(filename='nike.png')
        display(nike)
        
    slide1 = jayesh.slides.add_slide(slide_layout)
    title = slide1.shapes.title
    subtitle = slide1.placeholders[1]
    title.text = "Hello, World!"
    subtitle.text = img[i]
    
#     title = slide1.shapes.title
#     subtitle = slide1.placeholders[1]
#     title.text = "Hello, World!"
#     subtitle.text = "python-pptx was here!"
        
    

img = ['image1.jpg','image2.jpg' , 'image3.jpg']
for i in range(len(img)) :
    convert(i)

from pptx import Presentation
from pptx.util import Inches
jayesh = Presentation()
slide_layout = jayesh.slide_layouts[1]
##slide = jayesh.slides.add_slide(slide_layout)




jayesh.save('jayesh.pptx')
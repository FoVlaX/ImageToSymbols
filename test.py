from PIL import Image, ImageDraw, ImageFont
import sys

symbols = [' ','`','.','-','+','=','*','i','u','v','o','g','w','&','%','@','#']

#symbols = ['贝','非','给','得','也','用','热','赛','伊']
s = sys.argv[1]
im = Image.open(s)

width = int(im.size[0] / 8)
height = int(im.size[1] / 8)
newim = im.resize((width,height),Image.ANTIALIAS)
vpix = newim.load()
newim = newim.convert('L')



pix = newim.load()

f = open(s.split('.')[0]+'.txt','w')

saveim = Image.new('RGB',(15*width,15*height),(0,0,0))

font = ImageFont.truetype('ariblk.ttf',15)

draw = ImageDraw.Draw(saveim)


for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        f.write(symbols[ind]+symbols[ind])
    f.write('\n')

if (len(sys.argv) > 2 and sys.argv[2] == "1"):
    for i in range(height):
        for j in range(width):
            ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
            draw.rectangle([j*15,i*15,j*15+15,i*15+15],fill = (int(vpix[j,i][0]/6),int(vpix[j,i][1]/6),int(vpix[j,i][2]/6)))
            
for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        draw.text((j*15,i*15),symbols[ind],font = font,fill = vpix[j,i],stroke_fill = vpix[j,i])



saveim.save(s.split('.')[0]+'result.jpg')
print("complite")
f.close()


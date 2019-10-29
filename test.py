from PIL import Image, ImageDraw, ImageFont
import sys

symbols = [' ','`','.','-','+','=','*','i','u','v','o','g','w','&','%','@','#']

#symbols = ['贝','非','给','得','也','用','热','赛','伊']
s = sys.argv[1]
sybolsize = int(sys.argv[2])
imagesize = float(sys.argv[3])

im = Image.open(s)




kkk = imagesize/float(im.size[1])/sybolsize;


width = int(im.size[0] * kkk)
height = int(im.size[1] * kkk)
newim = im.resize((width,height),Image.ANTIALIAS)
vpix = newim.load()
newim = newim.convert('L')



pix = newim.load()

f = open(s.split('.')[0]+'.txt','w')

saveim = Image.new('RGB',(sybolsize*width,sybolsize*height),(255,255,255))

font = ImageFont.truetype('ariblk.ttf',sybolsize)

draw = ImageDraw.Draw(saveim)


for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        f.write(symbols[ind]+symbols[ind])
    f.write('\n')

if (len(sys.argv) > 4 and sys.argv[4] == "1"):
    for i in range(height):
        for j in range(width):
            ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
            draw.rectangle([j*sybolsize,i*sybolsize,j*sybolsize+sybolsize,i*sybolsize+sybolsize],fill = (int(vpix[j,i][0]/6),int(vpix[j,i][1]/6),int(vpix[j,i][2]/6)))
            
for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        draw.text((j*sybolsize,i*sybolsize),symbols[ind],font = font,fill = vpix[j,i],stroke_fill = vpix[j,i])



saveim.save(s.split('.')[0]+'result.jpg')
print("complite")
f.close()


from PIL import Image, ImageDraw, ImageFont
import sys

symbols = [' ','`','.','-','+','=','*','i','u','v','o','g','w','&','%','@','#']

#symbols = ['贝','非','给','得','也','用','热','赛','伊']


def imtosy(s, sybolsize, imagesize):

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
                
    for i in range(height):
        for j in range(width):
            ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
            draw.text((j*sybolsize,i*sybolsize),symbols[ind],font = font,fill = vpix[j,i],stroke_fill = vpix[j,i])

    saveim.save(s.split('.')[0]+'result.jpg')
    f.close()




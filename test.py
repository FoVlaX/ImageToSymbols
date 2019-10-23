from PIL import Image, ImageDraw, ImageFont
symbols = [' ','`','.','-','+','=','*','i','u','v','o','g','w','&','%','@','#']
im = Image.open("test2.jpg")

width = int(im.size[0] / 2)
height = int(im.size[1] / 2)
newim = im.resize((width,height),Image.ANTIALIAS).convert('L')
pix = newim.load()

mn = pix[0,0]
mx = pix[0,0]

for i in range(width):
    for j in range(height):
        mn = min(mn,pix[i,j])
        mx = max(mx,pix[i,j])

print(mn,' ',mx)

f = open('test.txt','w')

saveim = Image.new('L',(15*width,15*height),255)

font = ImageFont.truetype('arial.ttf',15)

draw = ImageDraw.Draw(saveim)


for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        f.write(symbols[ind]+symbols[ind])
    f.write('\n')


for i in range(height):
    for j in range(width):
        ind = len(symbols)-1 - int(pix[j,i]/256*len(symbols))
        draw.text((j*15,i*15),symbols[ind],font = font)
saveim.save("result.jpg")
f.close()


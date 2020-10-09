from PIL import Image

im_fn = Image.open(input('Enter Image Name : '))
px = im_fn.load()
threshold = int(input('Enter threshold : '))
mod = Image.new(mode='RGB',size=im_fn.size)

def funct1(a,b):
    p = px[a,b]
    return (p[0]+p[1]+p[2])/3
A = []
for i in range(im_fn.size[0]):
    B = []
    for j in range(im_fn.size[1]):
        thr = 0
        x = int(-1)
        while x<=1:
            y = int(-1)
            if i+x < 0 or i+x == im_fn.size[0]:
                x+=1
                continue
            while y<=1:
                if j+y < 0 or j+y == im_fn.size[1]:
                    y+=1
                    continue
                if thr < funct1(i+x,j+y):
                    thr = funct1(i+x,j+y)
                y+=1
            x+=1
        thr = abs(funct1(i,j)-thr)
        if thr > threshold:
            B.append((255,255,255))
        else :
            B.append((0,0,0))
    A.append(B)

for i in range(im_fn.size[0]):
    for j in range(im_fn.size[1]):
        px[i,j] = A[i][j]

                
                

im_fn.save('new_'+str(im_fn.filename)+'.'+str(im_fn.format))


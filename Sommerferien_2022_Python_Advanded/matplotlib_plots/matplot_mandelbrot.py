
import numpy
import time

##from numba import autojit
import matplotlib.pyplot as plt
import datetime

ct = datetime.datetime.now()
file_extension = str(ct.year)+str(ct.month).zfill(2)+str(ct.day).zfill(2)+"_"+str(ct.hour).zfill(2)+str(ct.minute).zfill(2)+"_"+str(ct.second).zfill(2)


def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
##        print(f"i:{i} - z:{z} - c:{c}")
        z = z * z + c
        if(z.real*z.real + z.imag*z.imag) >=4:
            return i
    return max_iter

#resolution of the image
columns = 800
rows = 800
start = time.time()
result = numpy.zeros([rows, columns])
for row_index, Re in enumerate(numpy.linspace(-2,1, num=rows)):
    for column_index, Im in enumerate(numpy.linspace(-1,1, num=columns)):
        result[row_index, column_index]= mandelbrot(Re, Im, 200)

plt.figure(dpi=100)
#https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
plt.imshow(result.T, cmap='afmhot', interpolation='bilinear' ,extent=[-2,1,-1,1])
plt.xlabel('Re')
plt.ylabel('Im')
end = time.time()
print(end - start)
plt.savefig("mandelbrot"+file_extension+".png")

plt.show()

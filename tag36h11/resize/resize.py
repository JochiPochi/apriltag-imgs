from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

start_id = 24
num_x_plot = 4
num_y_plot = 6
plot_size_x = 8.0
plot_size_y = 8.0
tag_size_x = 7.0
tag_size_y = 7.0
plot_dpi = 300
plot_margin = 0
fig, axs = plt.subplots(num_y_plot, num_x_plot)
fig.set_size_inches((num_x_plot*plot_size_x,num_y_plot*plot_size_y))
for iy in range(num_y_plot):
    for ix in range(num_x_plot):
        tag_id = start_id + ix + iy*num_x_plot
        if num_y_plot == 1:
            ax = axs[ix]
        else:
            ax = axs[iy,ix]
        
        tag_str = ""
        if tag_id < 10:
            tag_str += "0000"+str(tag_id)
        elif tag_id < 100:
            tag_str += "000"+str(tag_id)
        elif tag_id < 1000:
            tag_str += "00"+str(tag_id)
        else:
            tag_str += "0"+str(tag_id)
        img = np.array(plt.imread("../tag36_11_{}.png".format(tag_str)))
        img_resize = np.zeros(( int(plot_size_x*plot_dpi) + 2*plot_margin, int(plot_size_y*plot_dpi) + 2*plot_margin, 4))
        #np.set_printoptions(threshold=np.inf)
        #print(img_resize)
        for i in range(10):
            for j in range(10):
                img_resize[plot_margin+i*16*9:plot_margin+(i+1)*16*9,plot_margin+j*16*9:plot_margin+(j+1)*16*9,:] = img[i,j,:]
        
        ax.imshow(img_resize)
        
        plt.imsave("test.png",img_resize, dpi=plot_dpi)
        #ax.set_title("tag_id: {}".format(tag_str), y=1.02, fontsize='30')

plt.subplots_adjust(hspace=10.0)
plt.tight_layout()
plt.savefig("./apriltag_sample.pdf", format="pdf")
plt.plot()

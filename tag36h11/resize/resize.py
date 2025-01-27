from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

start_id = 24
num_x_plot = 4
num_y_plot = 1
plot_size_x = 8.0
plot_size_y = 8.0
tag_size = 7.0
plot_dpi = 300
fig, axs = plt.subplots(num_x_plot, num_y_plot)
fig.set_size_inches((num_y_plot*plot_size_y,num_x_plot*plot_size_x))
#img_group = np.zeros(( int(plot_size_x*plot_dpi*num_x_plot), int(plot_size_y*plot_dpi)))
for iy in range(num_y_plot):
    #img_group.fill(255)
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
        img_resize = np.zeros(( int(plot_size_x*plot_dpi), int(plot_size_y*plot_dpi), num_x_plot))
        #np.set_printoptions(threshold=np.inf)
        #print(img_resize)
        for i in range(1,9):
            for j in range(1,9):
                margin = int((plot_size_x-tag_size)*plot_dpi/2)
                x_range = int(tag_size*plot_dpi/8)
                y_range = int(tag_size*plot_dpi/8)
                img_resize[margin+(i-1)*x_range: margin+(i)*x_range, margin+(j-1)*y_range: margin+(j)*y_range,:] = img[i,j,:]
        
        ax.imshow(img_resize)
        
        plt.imsave("test.png",img_resize, dpi=plot_dpi)
        #img_group.fill(255)
        #a = int(plot_size_x*plot_dpi)
        #img_group[a:a+a,:] = img_resize[:,:,ix]
        #plt.imshow(img_group)
        #plt.imsave("test2.png",img_group, dpi=plot_dpi)
        #ax.set_title("tag_id: {}".format(tag_str), y=1.02, fontsize='30')

plt.setp(axs, xticks=[], yticks=[])
#plt.tight_layout()
plt.subplots_adjust(left=0, wspace=0, hspace=0)
#plt.figure(frameon=False)
plt.savefig("./apriltag_sample.pdf",pad_inches=0,dpi = 300, format="pdf")
plt.plot()



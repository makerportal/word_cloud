import random
import matplotlib
import matplotlib.pyplot as plt
from gifly import gif_maker
import numpy as np

# function for live-plotting
def live_plotter(ax,words,x_loc,y_loc,color,size_input,rotation):
    if ax==[]:
        plt.ion()
        fig = plt.figure(figsize=(11,6),facecolor='#3b3b3b')
        ax = fig.add_subplot(111,frameon=False)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        annot1 = []
        plt.show()
        return ax,annot1
    
    annot1 = ax.annotate(words,xy=(x_loc,y_loc),fontsize=size_input,xycoords='figure pixels',color=color,rotation=rotation)
    plt.pause(0.01)
    
    return ax,annot1

# initialize the figure so that we can loop and add words
ax = []
font_pixel_density = 20
ax,annot1 = live_plotter(ax,' ',0.0,0.0,'k',font_pixel_density,0)
fig = ax.get_figure()
fig_size = fig.get_dpi()*fig.get_size_inches()
# choose colormap
cmap = matplotlib.cm.get_cmap('tab20c')

# random word vector
lorem_ipsum = """Maecenas vitae diam facilisis, facilisis ex in,
tincidunt sem. Sed ornare bibendum dolor eu consectetur. In accumsan
viverra mauris. In mi mauris, scelerisque feugiat maximus blandit,
mattis vel turpis. Interdum et malesuada fames ac ante ipsum primis
in faucibus. Etiam aliquet justo a justo egestas euismod. Suspendisse
pretium tincidunt nibh in viverra. Nullam venenatis augue nibh.
Sed magna massa, ornare ac tincidunt id, elementum eget justo.
Suspendisse congue lectus ipsum, vitae maximus ipsum bibendum mattis.
Praesent dapibus dui eu nulla consectetur malesuada. Praesent
pellentesque dui id nibh vulputate, vitae eleifend nibh scelerisque.
Aenean mattis, lacus eleifend mattis venenatis, nisl nulla tempus diam,
sit amet maximus enim metus a lectus. Cras sit amet arcu ultricies,
semper tortor porta, faucibus nisl. Phasellus ac lectus luctus, suscipit
purus in, sollicitudin est. Phasellus venenatis diam non dui porta aliquam.
Vivamus vestibulum urna vitae erat placerat, id bibendum massa sagittis.
Aenean gravida tincidunt risus imperdiet congue. Fusce blandit purus
laoreet pellentesque interdum. Aliquam urna sem, pellentesque quis diam
a, pellentesque mattis velit. Donec aliquam gravida convallis. Sed tempus,
orci sit amet egestas scelerisque, lectus lectus tristique tellus, nec
laoreet nulla diam eget nisl. Aenean eu consequat dui. Cras ac eros
hendrerit, viverra nibh sit amet, finibus lacus."""

# splitting word based on spaces
words_for_cloud = (lorem_ipsum.strip(',')).split(' ')
# loop through words
for ii in range(0,len(words_for_cloud)):
    annot_text = words_for_cloud[ii]
    # find the size of the word in pixels
    annot_x_size = len(words_for_cloud[ii])*font_pixel_density
    # randomize the location of the word
    zoom_ratio = 0.95
    x_loc = random.uniform(0.0+zoom_ratio,1.0-zoom_ratio)*(fig_size[0]-annot_x_size)
    y_loc = random.uniform(0.0+zoom_ratio,1.0-zoom_ratio)*(fig_size[1]-font_pixel_density)

    # randomize the color,rotation angle, and size of the word text
    color =  matplotlib.cm.colors.to_hex(cmap(np.random.rand(1))[0])
    rotation = random.uniform(-1, 1)*30
    size_var = random.uniform(0.4,1)*font_pixel_density

    # here is the loop for checking whether the new annotation interferes with others - if it does
    # we remove the old text
    prev_children = ax.get_children()
    ax,annot1 = live_plotter(ax,annot_text,x_loc,y_loc,color,size_var,rotation)
    for ii in prev_children:        
        try:
            jj = (annot1.get_window_extent()).extents

            if jj[2]-ii.get_window_extent().extents[0]>=0 and ii.get_window_extent().extents[2]-jj[0]>=0 and\
               jj[3]-ii.get_window_extent().extents[1]>=0 and ii.get_window_extent().extents[3]-jj[1]>=0:
                ii.remove()                
        except:
            pass

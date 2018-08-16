import random
import matplotlib
import matplotlib.pyplot as plt
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
lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Elit
ut aliquam purus sit amet luctus venenatis lectus. Tempor orci eu lobortis
elementum nibh tellus molestie nunc non. Sed arcu non odio euismod lacinia
at quis risus sed. Dapibus ultrices in iaculis nunc sed augue. Quis commodo
odio aenean sed adipiscing diam donec adipiscing. Hac habitasse platea dictumst
vestibulum rhoncus est pellentesque. Posuere lorem ipsum dolor sit amet. Urna
id volutpat lacus laoreet. Tempor orci eu lobortis elementum nibh tellus
molestie nunc non. Vitae tempus quam pellentesque nec nam aliquam sem et
tortor. Elit pellentesque habitant morbi tristique senectus. Fermentum iaculis
eu non diam phasellus vestibulum. Est ullamcorper eget nulla facilisi etiam
dignissim diam quis enim. Platea dictumst vestibulum rhoncus est pellentesque
elit ullamcorper dignissim. Rhoncus urna neque viverra justo nec ultrices dui
sapien. Amet mattis vulputate enim nulla aliquet porttitor lacus luctus.
Ut enim blandit volutpat maecenas volutpat blandit aliquam. Integer feugiat
scelerisque varius morbi enim nunc faucibus a. Elementum integer enim neque
volutpat ac tincidunt. Vestibulum mattis ullamcorper velit sed ullamcorper
morbi. Donec enim diam vulputate ut pharetra. Non odio euismod lacinia at quis.
Congue quisque egestas diam in arcu cursus. Sit amet nulla facilisi morbi
tempus iaculis. At erat pellentesque adipiscing commodo elit at imperdiet.
Id aliquet lectus proin nibh nisl condimentum id. Ut tristique et egestas
quis ipsum suspendisse ultrices. Egestas erat imperdiet sed euismod. Donec
enim diam vulputate ut pharetra sit amet. Commodo viverra maecenas accumsan
lacus vel facilisis. Fringilla phasellus faucibus scelerisque eleifend donec
pretium vulputate sapien. Convallis a cras semper auctor neque vitae tempus
quam pellentesque. Sit amet mattis vulputate enim nulla aliquet. Proin nibh
nisl condimentum id. Pharetra et ultrices neque ornare aenean euismod.
Iaculis at erat pellentesque adipiscing. Convallis convallis tellus id
interdum velit laoreet id donec. Mattis vulputate enim nulla aliquet porttitor
lacus luctus. Diam maecenas sed enim ut. Nulla pellentesque dignissim enim
sit amet venenatis. Enim diam vulputate ut pharetra. Tincidunt dui ut ornare
lectus sit. Egestas integer eget aliquet nibh praesent tristique. Tellus id
interdum velit laoreet id donec ultrices tincidunt. Feugiat pretium nibh ipsum
consequat nisl vel pretium lectus. Arcu non sodales neque sodales ut. Eu feugiat
pretium nibh ipsum consequat. Elementum pulvinar etiam non quam lacus suspendisse
faucibus interdum posuere. """

# splitting word based on spaces
words_for_cloud = (lorem_ipsum.strip('.')).split(' ')
# loop through words
for ii in range(0,len(words_for_cloud)):
    annot_text = words_for_cloud[ii]
    # find the size of the word in pixels
    annot_x_size = len(words_for_cloud[ii])*font_pixel_density
    # randomize the location of the word
    size_weight_x = ((ii)/len(words_for_cloud))*0.8
    size_weight_y = ((ii)/len(words_for_cloud))*0.8
    spiral_speed = 0.1
    x_loc = (fig_size[0]/2)+(random.choice([random.uniform(-size_weight_x-spiral_speed,0),random.uniform(0,size_weight_x+spiral_speed)])*(fig_size[0]/2))
    y_loc = (fig_size[1]/2)+(random.choice([random.uniform(-size_weight_y-spiral_speed,0),random.uniform(0,size_weight_y+spiral_speed)])*(fig_size[1]/2))

    # randomize the color,rotation angle, and size of the word text
    color =  matplotlib.cm.colors.to_hex(cmap(np.random.rand(1))[0])
##    rotation = random.uniform(-1, 1)*30
    rotation = random.choice([-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])*90
    size_var = (random.uniform(0.4,1)*font_pixel_density)
    
    # here is the loop for checking whether the new annotation interferes with others - if it does
    # we remove the old text
    prev_children = ax.get_children()
    ax,annot1 = live_plotter(ax,annot_text,x_loc,y_loc,color,size_var,rotation)
    for kk in prev_children:
        if isinstance(kk, matplotlib.text.Annotation):            
            kk_extents = kk.get_window_extent().extents
            jj = (annot1.get_window_extent()).extents

            if kk_extents[2]-jj[0]>0 and jj[2]-kk_extents[0]>0 and kk_extents[3]-jj[1]>0 and\
                  jj[3]-kk_extents[1]>0:
                annot1.remove()
                break
            elif jj[2]>fig_size[0]:
                annot1.set_position((fig_size[0]-jj[2],jj[3]))
            elif jj[3]>fig_size[1]:
                annot1.set_position((jj[2],fig_size[1]-jj[3]))

plt.savefig('word_cloud_spiral.png',facecolor=fig.get_facecolor(), edgecolor='none',dpi=95)

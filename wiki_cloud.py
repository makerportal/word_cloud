import requests,random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def html_crawl(key1,content):

    stock_indx_1 = [i+len(key1) for i, j in enumerate(content) if content[i:i+len(key1)] == key1]

    wiki_date = []
    end_key = '">'
    for ii,indx in enumerate(stock_indx_1):
        for mm in range(0,200):
            if content[indx+mm:indx+mm+len(end_key)]==end_key:
                wiki_date.append(content[indx:indx+mm])
                break

    return wiki_date

def wiki_crawl():
    page = requests.get('https://en.wikipedia.org/wiki/Special:RecentChanges?hidebots=0&hidecategorization=1&hideWikibase=1&hidelog=1&limit=50&days=1&urlversion=1')
    content = page.text
    key1 = 'class="mw-changeslist-diff" title="'

    wiki_edit_dates = html_crawl(key1,content)
    return wiki_edit_dates


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

ax = []
font_pixel_density = 17 #16px per character
wiki_vals = wiki_crawl() 
ax,annot1 = live_plotter(ax,' ',0.0,0.0,'k',font_pixel_density,0.0)
fig = ax.get_figure()
fig_size = fig.get_dpi()*fig.get_size_inches()
cmap = matplotlib.cm.get_cmap('Set1')
while True:
    wiki_vals = wiki_crawl()
    
    for ii in range(0,len(wiki_vals)):
        
        annot_text = wiki_vals[ii]
        # find the size of the word in pixels
        annot_x_size = len(wiki_vals[ii])*font_pixel_density
        # randomize the location of the word
        zoom_ratio = 0.95
        x_loc = random.uniform(0.0+zoom_ratio,1.0-zoom_ratio)*(fig_size[0]-annot_x_size)
        y_loc = random.uniform(0.0+zoom_ratio,1.0-zoom_ratio)*(fig_size[1]-font_pixel_density)

        # randomize the color,rotation angle, and size of the word text
        color =  matplotlib.cm.colors.to_hex(cmap(np.random.rand(1))[0])
##        rotation = random.uniform(-1, 1)*30
        rotation = 0.0
        size_var = random.uniform(0.4,1)*font_pixel_density
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

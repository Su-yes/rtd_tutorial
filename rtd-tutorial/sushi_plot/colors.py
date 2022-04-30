# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 01:02:43 2020

@author: bhatt
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)

# Refrence: schemecolor.com

save = "yes" # yes or anything

def plot_color(name, pallet):
    '''Prints the color pallet'''
    num = len(pallet)
    a = range(num)
    b = np.ones(num)
    #
    plt.figure()
    fig, ax = plt.subplots()
    ax.bar(a, b, width = 0.8, color = pallet)
    ax.set_axis_off()
    ax.set_title(name, size = 15)
    #
    plt.savefig(name + '.png', dpi=1200)


falling_leaves = np.array(["#7A372D", "#551E48", "#C03E21", "#568B18", "#ED9C29", "#E3CF3A"])
autumn_vibrant = np.array(["#DF3C42", "#7926CC", "#E06C1E", "#EFA414","#6FB63B","#F4D910" ])
sale_in_autumn = np.array(["#93344B","#BB6553","#D3453F","#518F66","#F9B653","#F7D886"])
feast_your_heart = np.array(["#604B8A", "#E15D47", "#FFD46B", "#55ADFF"])
nothing_normal = np.array(["#A5E75A", "#7254AD", "#FFD606", "#FF093D"])
blue_orange = np.array(["#1655F2", "#0F1EAF", "#FD641F", "#FDBD29"])
combo = np.array(["#1655F2","#FD641F","#568B18","#FF093D","#FDBD29"])
rainbow = np.array(["#EC3445","#51BC37", "#1582FD", "#FCDD30", "#733294", "#FB761F" ])

# Make a library 
colors = {"Falling Leaves": falling_leaves, "Autumn Vibrant": autumn_vibrant, "Autumn Sale": sale_in_autumn, "Feast Your Heart": feast_your_heart, "Nothing Normal": nothing_normal, "Blue Orange Feelings": blue_orange, "rainbow": rainbow, "Combo": combo}


if __name__ == "__main__":
    # Print and save all the pallets
    if save.lower() == "yes":
        for i, j in colors.items():
            plot_color(i, j)
    else: 
        pass
else:
    # Option to display colors from external scripts
    def display_color(name):
        ''' Accepts name from external script and displays them.
            Also can display the entire collection. 
        '''
        if name.lower() == "colors":
            for i, j in colors.items():
                plot_color(i, j)
        elif name.title() in colors:
            plot_color(name.title(), colors[name.title()])
        else:
            print("The color does not exist. Available colors: ")
            for i ,j  in colors.items():
                print(i)
    
    def get_color(name):
        ''' Return an array of colors in the theme.'''
        if name.title() in colors:
            return colors[name.title()]
        else:
            print("The color does not exist. Available colors: ")
            for i ,j  in colors.items():
                print(i)
    
# =============================================================================
# Notes and Extra codes
# plt.scatter(a, b, marker = 'o', s = 800, c = Falling_leaves) # use c instead or 'color' to map a sequence of color. s = size
# ax.set_axis_off()
# =============================================================================

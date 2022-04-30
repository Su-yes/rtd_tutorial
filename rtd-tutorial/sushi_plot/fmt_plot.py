import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)

def reset_plot():
    plt.rcParams.update(plt.rcParamsDefault)

# =============================================================================

def latex_plot(val):
    '''
    Runs the commands to activate latex formating for plots.
    
    Positional Req:
        True (bool) -- Activate the latex format
        False (bool) -- Reset the matplotlib paramters to default.
    
    '''  
    
    if val == True:
    # adjust matplotlib parameters

        plt.rcParams['text.usetex'] = True
        plt.rcParams['font.size'] = 10
        plt.rcParams['font.family'] = "serif"
        
    elif val == False:
        plt.rcParams.update(plt.rcParamsDefault)
    else:
        pass

# =============================================================================

def save_plot(name, size):
    '''
    Saves the plot in a png format.

    Positional Req:
        name (str)
        size (int) -- Dots Per Inch (DPI)    

    '''
    plt.tight_layout()
    plt.savefig(name + ".png", dpi = size)
    # plt.savefig(name + ".pdf")
    
# =============================================================================

def xlabel(axes, name, size = 12):
    '''
    Sets the xlabel and the font size. 
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object. 
        name (str) -- name of the x axis. 
    
    Positional Opt:
        size (int)[12] -- Font size of the label. 
        
    '''
    
    axes.set_xlabel(name, fontsize = size)
    
def ylabel(axes, name, size = 12):
    '''
    Sets the xlabel and the font size. 
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object. 
        name (str) -- name of the x axis. 
    
    Positional Opt:
        size (int)[12] -- Font size of the label. 
        
    '''
    
    axes.set_ylabel(name, fontsize = size)
    
def title(axes, name, size = 15):
    '''
    Sets the title and the font size. 
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object. 
        name (str) -- title 
    
    Positional Opt:
        size (int)[15] -- Font size of the title. 
        
    '''
    
    axes.set_title(name, fontsize = size)

# =============================================================================

def tick_label_size(axes, axis, size=10, **kwargs):
    '''
    Change the appearance of ticks and tick labels. 

    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object. 
        axis (str) -- Axis on which to operate.
        {'x', 'y', 'both'}
        
    Keyword Opt:
        size (int)[10] -- Label size. 
        kwargs -- Same as tick_params()
        See matplotlib.axes.Axes.tick_params
    '''
        
    axes.tick_params(axis, labelsize = size, **kwargs)


# =============================================================================

def ticks(axes, major_size = 5, minor_size = 3, wide = 1):
    '''
    Turn on the ticks and change the appreance.
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object. 
        
    Positional Opt:
        major_size (float)[5] -- Size of the major ticks. 
        minor_size (float)[3] -- Size of the minor ticks. 
        wide (float)[1] -- Width of the ticks. Both Major and minor. 
        
    Notes:
        Default is fine most of the time. 
    '''
    
    axes.xaxis.set_tick_params(which = 'major', size = major_size, width = wide, direction='in', top='on')
    axes.xaxis.set_tick_params(which = 'minor', size = minor_size, width = wide, direction='in', top='on')
    axes.yaxis.set_tick_params(which = 'major', size = major_size, width = wide, direction='in', right='on')
    axes.yaxis.set_tick_params(which = 'minor', size = minor_size, width = wide, direction='in', right='on')

# =============================================================================

def minor_ticks(axes, *args):
    '''
    Turns on the tick marks for both the x and y axis.
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object
    
    Positional Opt:
        arg 1 (str) -- Axis Direction. 'x' or 'y'
        arg 2 (int) -- Number of ticks. 
    
    Notes:
        Positional bc arg1 must be followed by arg2. 
        Eg. disp_ticks(ax1, "x", 3, "y", 2).
        Accepts input for one or both axes. Not case sensitive.
        
    '''
    
    if len(args) == 0:
        pass
    else:
        
        # lower all input strings. 
        args = [x.lower() if type(x) == str else x for x in args ]
        
        # iterate over args list to apply the conditions. 
        if "x" in args or "y" in args:
            for i, j in enumerate(args):
                if j == "x":
                    axes.xaxis.set_minor_locator(AutoMinorLocator(args[i+1]))
                elif j == "y":
                    axes.yaxis.set_minor_locator(AutoMinorLocator(args[i+1]))
                else:
                    pass
        else:
            print("\nInvalid input.")
    
def major_ticks(axes, *args):
    '''
    Sets the distance for the major ticks.

    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object

    Positional Opt:
        arg 1 (str) -- Axis Direction. 'x' or 'y'
        arg 2 (float) -- The ticks will be placed at the multiples of the value provided.      
    
    Notes:
        Positional bc arg1 must be followed by arg2. 
        Eg. major_ticks(ax1, "x", 50, "y", 0.005).
 
    '''
    if len(args) == 0:
        pass
    else:
        
        # lower all input strings. 
        args = [x.lower() if type(x) == str else x for x in args ]
        
        # iterate over args list to apply the conditions. 
        if "x" in args or "y" in args:
            for i, j in enumerate(args):
                if j == "x":
                    axes.xaxis.set_major_locator(MultipleLocator(args[i+1]))
                elif j == "y":
                    axes.yaxis.set_major_locator(MultipleLocator(args[i+1]))
                else:
                    pass
        else:
            print("\nInvalid input.")
    
# =============================================================================

def tick_label_fmt(axes, **kwargs):
    '''
    Change the number fomrat of the x or y axis labels. 
    Uses an old-style ('%' operator) format string to format the tick.
    
    Positional Req:
        axes (matplotlib.axes._subplots.AxesSubplot) -- Axes object
        
    Keyword Opt:
        arg (dict) -- String format for x or y direction. 
        
    Notes:
        Eg. tick_label_fmt(x = "%0.3f", y = "%0.3f")
        Order doesn't matter.    
    '''
    
    if len(kwargs) == 0:
        pass
    else:
        # iterate over kwargs dict to apply the conditions. 
        for key, value in kwargs.items():
            if key.lower() == "x":
                axes.xaxis.set_major_formatter(FormatStrFormatter(value))
            if key.lower() == "y":
                axes.yaxis.set_major_formatter(FormatStrFormatter(value))

# =============================================================================
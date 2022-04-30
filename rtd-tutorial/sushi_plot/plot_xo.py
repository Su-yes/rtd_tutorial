#
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)
from matplotlib.colors import ListedColormap

from sushi_plot.fmt_plot import major_ticks, latex_plot, save_plot

def plot_xo(mat, freq_test = [], freq_analysis = [],**kwargs):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    The return type must be duplicated in the docstring to comply
    with the NumPy docstring style.

    Parameters
    ----------
    param1
        The first parameter.
    param2
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    """


def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Parameters`` section.
    The name of each parameter is required. The type and description of each
    parameter is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name : type
            description

            The description may span multiple lines. Following lines
            should be indented to match the first line of the description.
            The ": type" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : :obj:`str`, optional
        The second parameter.
    *args
        Variable length argument list.
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    bool
        True if successful, False otherwise.

        The return type is not optional. The ``Returns`` section may span
        multiple lines and paragraphs. Following lines should be indented to
        match the first line of the description.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError
        If `param2` is equal to `param1`.

    """
    
    # default values
    ap_ratio = 1
    font_size = 6
    color_map = False
    save = False
    plot_size_x = 7.5
    
    # Establish custom color map
    # Get the colormap colors, multiply them with the factor "a", and create new colormap
    cmap_len = plt.cm.BuGn.N
    my_cmap = plt.cm.BuGn(np.arange(cmap_len))
    # limit color range
    my_cmap = my_cmap[0:int(cmap_len*0.65),:]
    # add white for 0 values
    foo = np.insert(my_cmap,0,[1,1,1,1], axis= 0)
    my_cmap = ListedColormap(foo)
    
    # Make a white color map for default case
    white_cmap = ListedColormap(np.ones(shape = (1,4)))
    
    # =============================================================================
    
    def write_xo_val(mat):
        
        # Write out the values 
        for i in range(0,len(mat)):
            for j in range(0,len(mat)):
                c = mat[j,i]
                ax.text(i, j, str(c), va='center', ha='center', size = font_size)
    
    
    
    def get_xticklabels(freq, len_mat):
        
        # empty list is considered false
        if freq:
            labels = [str(freq[i][0]+1) + "\n" + str(freq[i][1]) + " Hz" for i in range(0,len(freq))]
            return labels
        else:
            # Default
            return list(range(1,len_mat+1))
    
    
    
    def get_yticklabels(freq, len_mat):

        if freq:
            
            # Find the longest number's length
            num_list = [str(freq[i][1]) for i in range(0, len(freq))]
            length = len(max(num_list, key = len))
            
            # Use the difference between the longest length and
            # number's length to offset the mode number
            labels = [str(freq[i][0]+1) + " - " + "  "*(length-len(str(freq[i][1]))) + str(freq[i][1]) + " Hz" for i in range(0,len(freq))]
            return labels
        else:
            # Default
            return list(range(1,len_mat+1))



    def plot_format():
        
        major_ticks(ax, "x",1, "y",1)
    
        ax.tick_params(bottom = False)
        ax.set_xlabel("Test Modes")
        ax.xaxis.set_label_position('top') 
        ax.set_ylabel("Analysis Modes")
        
        # Must start at 0, so add 1 to the length of the mat. 
        ax.set_xticks(range(0,len(mat)))
        ax.set_yticks(range(0,len(mat)))
        
        ax.set_xticklabels(get_xticklabels(freq_test,len(mat)))
        ax.set_yticklabels(get_yticklabels(freq_analysis, len(mat)))
        
        
        if save:
            save_plot("xo", 1200)
        
        plt.show()
        
    # =============================================================================
    
    if len(kwargs) == 0:
        # Default plot
        plt.figure()
        fig,ax = plt.subplots()
        
        ax.matshow(abs(mat), cmap = white_cmap)
        write_xo_val(mat)
        plot_format()
    else:        
        for key, value in kwargs.items():
            if key.lower() == "font_size":
                font_size = value
            if key.lower() == "aspect":
                ap_ratio = value
            if key.lower() == "latex":
                latex = value
                latex_plot(value)
            if key.lower() == "cmap":
                color_map = value
            if key.lower() == "save":
                save = value
            if key.lower() == "plot_size":
                plot_size_x = value
    
        plt.figure()
        fig,ax = plt.subplots(figsize = (plot_size_x,7.5))    
        
    if color_map:
        ax.matshow(abs(mat), aspect=ap_ratio, cmap = my_cmap)
    else:
        ax.matshow(abs(mat), aspect=ap_ratio, cmap = white_cmap)
        
    write_xo_val(mat)
    
    plot_format()
    
    # End
    # =============================================================================
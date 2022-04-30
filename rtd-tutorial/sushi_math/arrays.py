# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:29:48 2020

@author: Suyash Bhattarai

A collection of the math routines. 

"""

import math
import numpy as np

from sushi_utils.utils import print_warn

class rotate:
    
    @staticmethod
    def x(vector,angle):
        theta = math.radians(angle)
        rx = np.array([[1,0,0],[0, math.cos(theta), -math.sin(theta)],[0, math.sin(theta), math.cos(theta)]])
        v = np.array(vector)
        return np.dot(v,rx).round(3)
    
    @staticmethod
    def y(vector,angle):
        theta = math.radians(angle)
        rx = np.array([[math.cos(theta), 0, math.sin(theta)], [0,1,0], [-math.sin(theta), 0, math.cos(theta)]])
        v = np.array(vector)
        return np.dot(v,rx).round(3)
    
    @staticmethod
    def z(vector,angle):
        theta = math.radians(angle)
        rx = np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0,0, 1]])
        v = np.array(vector)
        return np.dot(rx,v).round(3)

# =============================================================================

def reorder_array (mat, key, group = 1, axis = 0, return_key = False):
    '''
    Positional Req:
        mat (ndarray): Matrix or vector you are trying to sort.
        key (list or ndarray): Key use to sort the matrix.
    
    Keyword Opt:
        group (int)[1]: The number of rows or columns to group and shift together.
        axis (int)[0]: axis = 0 for reordering rows. 
        axis = 1 for reordering columns. 
        return_key (bool)[False]: If True, returns the sorted key as well. 
        
    Returns:
        mat_sorted [ndarray]: Sorted Array. 
        key_sorted [list]: Sorted Key. 
        
    Notes:
        Sorted key will/should be in assending order. 
        Updated: March 15, 2022

    '''
    
    m, n = mat.shape
    mat_grouped = []
    mat_dict = {}
        
    if axis == 0:
        # sort the rows 
        
        # Check for exact # of groups
        if m % group != 0:
            print_warn()
            print("There must be an exact number of groups.\nCheck the size of matrix and the number of groups.\n")
        
        
        # Group rows
        for i in range(0, m, group):
            mat_grouped.append(mat[i:i+group,:])


        # make a dictionary {row: row vec}
        # or, {nodes: phi}
        for i in range(0, len(key)):
            mat_dict[key[i]] = mat_grouped[i]
        
        # Sort the dictionary
        temp = dict(sorted(mat_dict.items()))
        
        key_sorted = list(temp.keys())
        mat_sorted = np.concatenate(list(temp.values()), axis = 0)
        
        if return_key:
            return mat_sorted, key_sorted
        else:
            return mat_sorted
     
    elif axis == 1:
        # sort the columns 
        
       
        # Check for exact # of groups
        if n % group != 0:
            print_warn()
            print("There must be an exact number of groups.\nCheck the size of matrix and the number of groups.\n")
        
        # Group columns
        for i in range(0, n, group):
            mat_grouped.append(mat[:,i:i+group])
        
        # make a dictionary {column number: col vec}
        # or, {mode number: DOF values}
        for i in range(0, n, group):
            mat_dict[key[i]] = mat_grouped[i]
            
        
        # Sort the dictionary
        temp = dict(sorted(mat_dict.items()))
        
        key_sorted = list(temp.keys())
        mat_sorted = np.column_stack(list(temp.values()))
        
        if return_key:
            return mat_sorted, key_sorted
        else:
            return mat_sorted
        
    
    
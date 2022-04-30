# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:29:48 2020

@author: Suyash Bhattarai

A collection of the math routines. 

"""

import math
import numpy as np
import tables
import matplotlib.pyplot as plt

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

def reorder_array (a):
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
    
    if a == 2:
      return a   
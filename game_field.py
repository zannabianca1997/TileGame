# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:00:46 2017

@author: zanna
"""
import numpy as np

walls_types = None
floors_types = None

def init(setup_data):
    pass

class Tile:
    """Implement a general thing that's bound to a Tile"""
    def __init__(self, tile_data):
        """Actually doing nothing. Head of the super() calls"""
        super().__init__()
    
class SpriteTile(Tile):
    """Represent a tile object, drawable. Contains sprite data."""
    def __init__(self, tile_data):
        """Extracting sprite data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.sprite = tile_data["sprite"]
    #TODO: loading procedure
    
class BasicWall(SpriteTile):
    """Represent an overground object. Contains strongness"""
    def __init__(self, tile_data):
        """Extracting strongness data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.strongness = tile_data["strongness"]
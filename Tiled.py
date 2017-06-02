# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 01:10:24 2017

@author: zanna
"""

# --- super classes of various things ---

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
        self.sprite = tile_data["sprite"]  # sprite file. will be substituted with the loaded sprite
    #TODO: loading procedure
    
        
class Activable(Tile):
    """Represent a destructible object. Contains strongness"""
    # --- interface ---
    def __init__(self, tile_data):
        """Extracting strongness data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        # create the action dictionary. Initially, every action is bound to an error code
        self.actions = tile_data["actions"]
        #TODO: check next line. it has to be written different
        #self._action_dict = {action:(labda (blk, ent, env):self._errate_action(action)) for action in self.actions}
        
    def action(self, block_memory, action, entity, enviroment):
        if action in self.actions:
            self.actions[action](block_memory, entity, enviroment)
        else:
            self._errate_action(action, block_memory, entity, enviroment)
                
    # --- inside methods ---
    
    #TODO: Check all down. You written this on train, no internet, smoked and tired. Please check.
    @classmethod
    def _undef_action(cls, action):
        """Called if performed an action that has a name but no code"""
        raise NotImplementedError #TODO: logs an error
    @classmethod
    def _errate_action(cls, entity, enviroment):
        """Called if performed an illegal action"""
        raise NotImplementedError #TODO: logs a warning
    

class Destructible(Activable):
    """Represent a destructible object. Contains strongness"""
    def __init__(self, tile_data):
        """Extracting strongness data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.strongness = tile_data["strongness"]  # durability of the tile
        self.add_action()
        
# --- classes for normal blocks ---

class BasicWall(SpriteTile, Destructible):
    """Represent an overground object. Contains dimension."""
    def __init__(self, tile_data):
        """Extracting strongness data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.dimension = tile_data["dimension"]  # dimension. 
        #If 1 the block is impassable. If 0, it offers no resistance
        #If 0<dimnsion<1, then entity cam occupy this tile, but the dimension 
        #cap is no 1, but (1 - dimension).

class BasicFloor(SpriteTile, Destructible):
    """Represent the floor of a cell. Contains strongness and walking speed"""
    def __init__(self, tile_data):
        """Extracting walk_speed data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.walk_speed = tile_data["walk_speed"] # the speed multiplier if a entity wander on this block
        
# --- the next classes are to implement for special blocks --- 
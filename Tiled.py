# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 01:10:24 2017

@author: zanna
"""
import logging

# logging setup
logger = logging.getLogger(__name__)

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
        self._action_dict = {
            action: (lambda blk, ent, env: self._errate_action(action, blk, ent, env))
            for action in self.actions}
        
    def action(self, block_memory, action, entity, enviroment):
        if action in self.actions:
            self.actions[action](block_memory, entity, enviroment)
        else:
            self._errate_action(action, block_memory, entity, enviroment)
                
    # --- inside methods ---

    @classmethod
    def _undef_action(cls, action, block_memory, entity, enviroment):
        """Called if performed an action that has a name but no code"""
        logger.error("An action was performed, but no code specified.\n\tclass_name:{}\n\taction:{}".format(cls.__name__, action),)

    @classmethod
    def _errate_action(cls, action, block_memory, entity, enviroment):
        """Called if performed an illegal action"""
        logger.warning("An action was performed, but on a tile that don't support it.\n\tclass_name:{}\n\taction:{}".format(cls.__name__, action))
    

class Destructible(Activable):
    """Represent a destructible object. Contains strongness"""
    def __init__(self, tile_data):
        """Extracting strongness data from tile_data, passing on super() the rest"""
        super().__init__(tile_data)
        self.strongness = tile_data["strongness"]  # durability of the tile
        self._add_action("break", self._break)

    @classmethod
    def _break(cls, block_memory, entity, enviroment):
        """Break the block"""


        
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
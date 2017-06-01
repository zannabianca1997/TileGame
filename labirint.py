# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:00:46 2017

@author: zanna
"""
import json
import game_field

SETUPFILE = "setup.json"


if __name__ == "__main__":
    with open(SETUPFILE) as setup_file:
        setups = json.load(setup_file)
        game_field.init(setups["game"])
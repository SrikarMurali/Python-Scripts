# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import choice
def get_description():
    """Return random weather, just like the pros"""
    possibilities = ['rain', 'snow', 'sun', 'sleet', 'fog', 'who knows']
    return choice(possibilities)


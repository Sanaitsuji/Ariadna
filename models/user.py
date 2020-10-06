# -*- codingÑ utf-8 -*-
# -----------------------------
# Name: Login
# Author: Oscar Velasco
# Creation: 18/05/2020
# Modified: 18/05/2020
# ------------------------------

__version__ = "1.0"

"""
Here you will find the design for the user class
"""


class User(object):

    def __init__(self):
        self.id = 0
        self.name = ""

    def create(self, vals):
        for key in vals.keys():
            if key == 'id':
                self.id = vals['id']
            if key == 'name':
                self.name = vals['name']

        return self

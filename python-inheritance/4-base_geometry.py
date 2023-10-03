#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""

class BaseMetaClass(type):
    
    '''
    Class: 
    '''
    
    def __dir__(cls):
        
        '''
        This is to exclude an attribute from printing
        '''

        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseMetaClass):

    """Represent base geometry."""

    def __dir__(cls):

        '''
        This is to exclude an attribute from printing
        '''

        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):

        """Not implemented."""
        
        raise Exception("area() is not implemented")
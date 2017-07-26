__author__ = 'cjm'

import logging
import requests

from scigraph.renderers.Renderer import Renderer

# TODO: different implementations for different types

class EntityAnnotationRenderer(Renderer):
    """
    straight up
    """


    def __init__(self):
        Renderer.__init__(self)

    def render(self, resultset):
        for s in resultset.spans:
            token = s.token
            if token.id.startswith("GO:"):
            	print('{0: <3} \t {1: <3} \t {2: <16}  {3: <25} \t "{4}"'.format(s.start, s.end, token.id, ",".join(token.terms), s.text))

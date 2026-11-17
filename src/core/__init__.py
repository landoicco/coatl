"""
Main package for Coatl.
Provides UI and Gameplay utilities.
"""

__author__ = "Lando Icaza C."

from .configs import *
from .game import Game
from .splash import *

__version__ = VERSION

__all__ = ["Color", "Configs", "Font", "Game", "show_splash_screen"]

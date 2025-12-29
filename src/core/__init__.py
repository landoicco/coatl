"""
Main package for Coatl.
Provides UI and Gameplay utilities.
"""

__version__ = "1.0.0"
__author__ = "Lando Icaza C."

from .splash import show_splash_screen
from .configs import Configs, Color
from .game import Game

__all__ = ["Configs", "Color", "Game", "show_splash_screen"]

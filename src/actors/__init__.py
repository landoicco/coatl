"""
Actors package for Coatl.
Provides classes implementing the behavior of all actors that appear in the game.
"""

__version__ = "1.0.0"
__author__ = "Lando Icaza C."

from .snake import Snake
from .fruit import Fruit

__all__ = ["Snake", "Fruit"]

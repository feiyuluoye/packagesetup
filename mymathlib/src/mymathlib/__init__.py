"""
MyMathLib - 一个强大的数学运算库
版本: 1.0.0

提供基本的数学运算、高级数学函数和常用数学常量。
"""

from .core import MathOperations, Calculator
from .advanced import AdvancedMath, Statistics
from .constants import MathConstants, PI, E, GOLDEN_RATIO

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    'MathOperations',
    'Calculator',
    'AdvancedMath',
    'Statistics',
    'MathConstants',
    'PI',
    'E',
    'GOLDEN_RATIO'
]
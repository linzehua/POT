# -*- coding: utf-8 -*-
"""

This module provides GPU implementation for several OT solvers and utility 
functions. The GPU backend in handled by `cupy 
<https://cupy.chainer.org/>`_.

By default, the functions in this module accept and return numpy arrays 
in order to proide drop-in replacement for the other POT function but
the transfer between CPU en GPU comes with a significant overhead.

In order to get the best erformances, we recommend to given only cupy 
arrays to the functions and desactivate the conversion to numpy of the 
result of the function with parameter ``to_numpy=False``.




"""

from . import bregman
from . import da
from .bregman import sinkhorn
from .da import sinkhorn_lpl1_mm

from . import utils
from .utils import dist, to_gpu, to_np


# Author: Remi Flamary <remi.flamary@unice.fr>
#         Leo Gautheron <https://github.com/aje>
#
# License: MIT License

__all__ = ["utils", "dist", "sinkhorn",
           "sinkhorn_lpl1_mm", 'bregman', 'da', 'to_gpu', 'to_np']

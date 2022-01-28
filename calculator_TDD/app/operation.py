from .div_operation import division
from .min_operation import minus_op
from .mul_operation import multiply
from .sum_operation import sumition


class OP:
    """OP is a Facade"""
    
    div = division
    min = minus_op
    mul = multiply
    sum = sumition
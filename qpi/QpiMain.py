'''
QPI Package
-------------------------------------------
Authors : Zackriya Solutions
Year    : 2022
Version : V 0.0.1
-------------------------------------------
The main classes and functions for QPI Rest
'''
class Qpi:
    '''
    The main class for QPI Rest contains the functions to
    Take model and parameters as input and output the 
    REST API endpoint
    '''    
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.sum = self.summer(self.a, self.b)
    
    def summer(a, b):
        sum = a + b
        return sum

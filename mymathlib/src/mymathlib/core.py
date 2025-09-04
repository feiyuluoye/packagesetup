"""
核心数学运算模块
"""

class MathOperations:
    """基础数学运算类"""
    
    def __init__(self, precision=2):
        self.precision = precision
    
    def add(self, *numbers):
        """加法运算，支持多个参数"""
        result = sum(numbers)
        return round(result, self.precision)
    
    def subtract(self, a, b):
        """减法运算"""
        result = a - b
        return round(result, self.precision)
    
    def multiply(self, *numbers):
        """乘法运算，支持多个参数"""
        result = 1
        for num in numbers:
            result *= num
        return round(result, self.precision)
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("除数不能为0")
        result = a / b
        return round(result, self.precision)

class Calculator:
    """计算器类，提供链式操作"""
    
    def __init__(self, initial_value=0, precision=2):
        self.result = initial_value
        self.precision = precision
        self.history = []
    
    def add(self, value):
        """加法操作"""
        self.result += value
        self.history.append(f"+ {value}")
        return self
    
    def subtract(self, value):
        """减法操作"""
        self.result -= value
        self.history.append(f"- {value}")
        return self
    
    def multiply(self, value):
        """乘法操作"""
        self.result *= value
        self.history.append(f"* {value}")
        return self
    
    def divide(self, value):
        """除法操作"""
        if value == 0:
            raise ValueError("除数不能为0")
        self.result /= value
        self.history.append(f"/ {value}")
        return self
    
    def get_result(self):
        """获取当前结果"""
        return round(self.result, self.precision)
    
    def clear(self):
        """清除计算历史"""
        self.result = 0
        self.history = []
        return self
    
    def get_history(self):
        """获取计算历史"""
        return self.history
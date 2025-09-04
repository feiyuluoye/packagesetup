"""
高级数学函数模块
"""

import math

class AdvancedMath:
    """高级数学运算类"""
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n < 0:
            raise ValueError("阶乘只能计算非负整数")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    @staticmethod
    def is_prime(n):
        """判断质数"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    @staticmethod
    def fibonacci(n):
        """生成斐波那契数列"""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
        return fib_sequence
    
    @staticmethod
    def power(base, exponent):
        """幂运算"""
        return base ** exponent
    
    @staticmethod
    def sqrt(n):
        """平方根"""
        if n < 0:
            raise ValueError("不能计算负数的平方根")
        return math.sqrt(n)

class Statistics:
    """统计运算类"""
    
    @staticmethod
    def mean(numbers):
        """计算平均值"""
        if not numbers:
            raise ValueError("数字列表不能为空")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def median(numbers):
        """计算中位数"""
        if not numbers:
            raise ValueError("数字列表不能为空")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]
    
    @staticmethod
    def mode(numbers):
        """计算众数"""
        from collections import Counter
        if not numbers:
            raise ValueError("数字列表不能为空")
        counter = Counter(numbers)
        max_count = max(counter.values())
        return [num for num, count in counter.items() if count == max_count]
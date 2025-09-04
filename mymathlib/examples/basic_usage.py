#!/usr/bin/env python3
"""
MyMathLib基本使用示例
"""

from mymathlib import MathOperations, Calculator, AdvancedMath, Statistics, PI

def main():
    print("===== MyMathLib基本使用示例 =====\n")
    
    # 基础运算
    print("1. 基础数学运算")
    ops = MathOperations(precision=4)
    print(f"   加法: {ops.add(1.2345, 2.3456)}")
    print(f"   减法: {ops.subtract(5.5, 2.2)}")
    print(f"   乘法: {ops.multiply(3, 4, 5)}")
    print(f"   除法: {ops.divide(10, 3)}")
    print()
    
    # 链式计算器
    print("2. 链式计算器")
    calc = Calculator(10)
    result = calc.add(5).multiply(2).subtract(3).divide(4).get_result()
    print(f"   计算结果: {result}")
    print(f"   计算历史: {calc.get_history()}")
    print()
    
    # 高级函数
    print("3. 高级数学函数")
    print(f"   5的阶乘: {AdvancedMath.factorial(5)}")
    print(f"   17是质数: {AdvancedMath.is_prime(17)}")
    print(f"   斐波那契数列前10项: {AdvancedMath.fibonacci(10)}")
    print(f"   2的10次方: {AdvancedMath.power(2, 10)}")
    print(f"   16的平方根: {AdvancedMath.sqrt(16)}")
    print()
    
    # 统计计算
    print("4. 统计计算")
    numbers = [1, 2, 3, 4, 5, 5, 6]
    print(f"   数据集: {numbers}")
    print(f"   平均值: {Statistics.mean(numbers)}")
    print(f"   中位数: {Statistics.median(numbers)}")
    print(f"   众数: {Statistics.mode(numbers)}")
    print()
    
    # 数学常量
    print("5. 数学常量")
    print(f"   圆周率: {PI}")
    
if __name__ == "__main__":
    main()
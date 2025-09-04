#!/usr/bin/env python3
"""
MyMathLib高级使用示例
"""

from mymathlib import MathConstants, AdvancedMath, Statistics, MathOperations

def main():
    print("===== MyMathLib高级使用示例 =====\n")
    
    # 使用常量类
    print("1. 使用常量类")
    constants = MathConstants()
    print(f"   光速: {constants.LIGHT_SPEED} m/s")
    print(f"   黄金比例: {constants.GOLDEN_RATIO}")
    print(f"   欧拉-马歇罗尼常数: {constants.EULER_MASCHERONI}")
    print()
    
    # 错误处理
    print("2. 错误处理示例")
    try:
        result = AdvancedMath.sqrt(-1)
    except ValueError as e:
        print(f"   错误: {e}")
    
    try:
        result = AdvancedMath.factorial(-5)
    except ValueError as e:
        print(f"   错误: {e}")
    
    try:
        ops = MathOperations()
        result = ops.divide(10, 0)
    except ValueError as e:
        print(f"   错误: {e}")
    print()
    
    # 批量处理
    print("3. 批量处理示例")
    numbers_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    primes = [num for num in numbers_to_check if AdvancedMath.is_prime(num)]
    print(f"   检查数字: {numbers_to_check}")
    print(f"   质数: {primes}")
    print()
    
    # 复杂统计分析
    print("4. 复杂统计分析")
    # 生成一个包含多个峰值的数据集
    dataset = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9]
    print(f"   数据集: {dataset}")
    print(f"   平均值: {Statistics.mean(dataset):.2f}")
    print(f"   中位数: {Statistics.median(dataset):.2f}")
    print(f"   众数: {Statistics.mode(dataset)}")
    print()
    
    # 组合使用多个类
    print("5. 组合使用多个类")
    # 计算一组数据的统计信息，并使用MathOperations进行进一步计算
    stats_data = [10, 20, 30, 40, 50]
    mean_value = Statistics.mean(stats_data)
    ops = MathOperations(precision=2)
    # 计算平均值的平方
    squared_mean = ops.multiply(mean_value, mean_value)
    print(f"   数据集: {stats_data}")
    print(f"   平均值: {mean_value}")
    print(f"   平均值的平方: {squared_mean}")
    print()
    
    # 性能测试示例
    print("6. 性能测试示例")
    import time
    start_time = time.time()
    fib_result = AdvancedMath.fibonacci(30)
    end_time = time.time()
    print(f"   计算斐波那契数列前30项耗时: {end_time - start_time:.6f} 秒")
    print(f"   第30个斐波那契数: {fib_result[-1]}")

if __name__ == "__main__":
    main()
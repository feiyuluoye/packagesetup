# Python 第三方自定义库开发与使用教程

## 1. 创建可发布的库项目结构

首先创建完整的项目结构：

```
mymathlib/
├── src/
│   └── mymathlib/
│       ├── __init__.py
│       ├── core.py
│       ├── advanced.py
│       └── constants.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_advanced.py
│   └── test_constants.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── docs/
│   └── getting_started.md
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── requirements.txt
```

## 2. 核心代码实现

### 2.1 `src/mymathlib/__init__.py`
```python
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
```

### 2.2 `src/mymathlib/core.py`
```python
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
```

### 2.3 `src/mymathlib/advanced.py`
```python
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
```

### 2.4 `src/mymathlib/constants.py`
```python
"""
数学常量模块
"""

class MathConstants:
    """数学常量类"""
    
    PI = 3.141592653589793
    E = 2.718281828459045
    GOLDEN_RATIO = 1.618033988749895
    EULER_MASCHERONI = 0.5772156649015329
    LIGHT_SPEED = 299792458  # m/s

# 导出常用常量
PI = MathConstants.PI
E = MathConstants.E
GOLDEN_RATIO = MathConstants.GOLDEN_RATIO
```

## 3. 配置打包文件

### 3.1 `setup.py`
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="mymathlib",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive mathematical operations library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mymathlib",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    keywords="math, mathematics, calculator, statistics",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/mymathlib/issues",
        "Source": "https://github.com/yourusername/mymathlib",
        "Documentation": "https://github.com/yourusername/mymathlib/wiki",
    },
)
```

### 3.2 `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mymathlib"
version = "1.0.0"
description = "A comprehensive mathematical operations library"
readme = "README.md"
requires-python = ">=3.7"
license = {file = "LICENSE"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["math", "mathematics", "calculator", "statistics"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/yourusername/mymathlib"
Documentation = "https://github.com/yourusername/mymathlib/wiki"
Repository = "https://github.com/yourusername/mymathlib"
Issues = "https://github.com/yourusername/mymathlib/issues"
```

## 4. 安装和使用教程

### 4.1 本地安装开发版本

```bash
# 在项目根目录
pip install -e .

# 或者使用setup.py
python setup.py develop
```

### 4.2 打包和发布

```bash
# 安装打包工具
pip install setuptools wheel twine

# 构建包
python setup.py sdist bdist_wheel

# 检查包
twine check dist/*

# 上传到PyPI（需要先注册账号）
twine upload dist/*
```

### 4.3 第三方使用

```bash
# 从PyPI安装
pip install mymathlib

# 或者指定版本
pip install mymathlib==1.0.0
```

## 5. 使用示例

### 5.1 基本使用
```python
from mymathlib import MathOperations, Calculator, AdvancedMath, Statistics, PI

# 基础运算
ops = MathOperations(precision=4)
print(f"加法: {ops.add(1.2345, 2.3456)}")
print(f"乘法: {ops.multiply(3, 4, 5)}")

# 链式计算器
calc = Calculator(10)
result = calc.add(5).multiply(2).subtract(3).divide(4).get_result()
print(f"计算结果: {result}")
print(f"计算历史: {calc.get_history()}")

# 高级函数
print(f"5的阶乘: {AdvancedMath.factorial(5)}")
print(f"17是质数: {AdvancedMath.is_prime(17)}")
print(f"斐波那契数列: {AdvancedMath.fibonacci(10)}")

# 统计计算
numbers = [1, 2, 3, 4, 5, 5, 6]
print(f"平均值: {Statistics.mean(numbers)}")
print(f"中位数: {Statistics.median(numbers)}")
print(f"众数: {Statistics.mode(numbers)}")

# 数学常量
print(f"圆周率: {PI}")
```

### 5.2 高级使用
```python
from mymathlib import MathConstants, AdvancedMath

# 使用常量类
constants = MathConstants()
print(f"光速: {constants.LIGHT_SPEED} m/s")
print(f"黄金比例: {constants.GOLDEN_RATIO}")

# 错误处理
try:
    result = AdvancedMath.sqrt(-1)
except ValueError as e:
    print(f"错误: {e}")

# 批量处理
numbers_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = [num for num in numbers_to_check if AdvancedMath.is_prime(num)]
print(f"质数: {primes}")
```

## 6. 完整的测试用例

### 6.1 `tests/test_core.py`
```python
import unittest
from mymathlib.core import MathOperations, Calculator

class TestCoreFunctions(unittest.TestCase):
    
    def setUp(self):
        self.ops = MathOperations(precision=4)
        self.calc = Calculator()
    
    def test_addition(self):
        self.assertEqual(self.ops.add(1, 2), 3)
        self.assertEqual(self.ops.add(1.5, 2.5), 4.0)
        self.assertEqual(self.ops.add(1, 2, 3, 4), 10)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.ops.divide(10, 0)
    
    def test_calculator_chain(self):
        result = self.calc.add(5).multiply(3).subtract(2).divide(4).get_result()
        self.assertEqual(result, 3.25)
    
    def test_calculator_history(self):
        self.calc.add(10).multiply(2)
        self.assertEqual(len(self.calc.get_history()), 2)
        self.calc.clear()
        self.assertEqual(len(self.calc.get_history()), 0)

if __name__ == '__main__':
    unittest.main()
```

### 6.2 运行测试
```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定测试文件
python -m pytest tests/test_core.py -v

# 生成测试覆盖率报告
python -m pytest tests/ --cov=src/mymathlib
```

## 7. 文档和示例

### 7.1 `README.md`
```markdown
# MyMathLib

一个功能强大的数学运算库，提供基础运算、高级函数和统计计算。

## 安装

```bash
pip install mymathlib
```

## 快速开始

```python
from mymathlib import MathOperations, AdvancedMath

# 基础运算
ops = MathOperations()
result = ops.add(1, 2, 3, 4)

# 高级函数
factorial = AdvancedMath.factorial(5)
```

## 功能特性

- 基础四则运算
- 链式计算器
- 高级数学函数
- 统计计算
- 数学常量
```

## 8. 版本管理和发布

### 8.1 版本控制
```bash
# 更新版本号
# 在 setup.py 和 __init__.py 中更新版本号

# 创建新版本标签
git tag v1.0.0
git push origin v1.0.0
```

### 8.2 发布到PyPI
```bash
# 清理旧构建
rm -rf dist/ build/ *.egg-info/

# 构建新版本
python setup.py sdist bdist_wheel

# 上传到PyPI
twine upload dist/*

# 或者上传到测试PyPI
twine upload --repository testpypi dist/*
```

这个完整的教程展示了如何创建一个专业的、可发布的第三方Python库，包括项目结构、代码组织、测试、文档和发布流程。

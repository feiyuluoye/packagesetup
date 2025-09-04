# MyMathLib 入门指南

## 1. 安装

MyMathLib 可以通过 pip 安装：

```bash
pip install mymathlib
```

如果要安装特定版本：

```bash
pip install mymathlib==1.0.0
```

对于开发人员，可以从源代码安装开发版本：

```bash
# 克隆仓库后在项目根目录执行
pip install -e .
```

## 2. 快速开始

安装完成后，可以通过以下简单示例开始使用 MyMathLib：

```python
from mymathlib import MathOperations, AdvancedMath

# 创建基础运算实例
ops = MathOperations()

# 执行基本运算
result = ops.add(1, 2, 3, 4)  # 返回: 10

# 使用高级数学函数
factorial = AdvancedMath.factorial(5)  # 返回: 120
```

## 3. 核心功能

### 3.1 基础数学运算 (MathOperations)

`MathOperations` 类提供基本的四则运算功能：

```python
from mymathlib import MathOperations

# 创建实例，设置精度为4位小数
ops = MathOperations(precision=4)

# 加法
sum_result = ops.add(1.2345, 2.3456)  # 返回: 3.5801

# 减法
sub_result = ops.subtract(5.5, 2.2)  # 返回: 3.3

# 乘法（支持多个参数）
mul_result = ops.multiply(2, 3, 4)  # 返回: 24

# 除法
div_result = ops.divide(10, 3)  # 返回: 3.3333
```

### 3.2 链式计算器 (Calculator)

`Calculator` 类提供链式操作的计算器功能：

```python
from mymathlib import Calculator

# 创建计算器实例，设置初始值为10
calc = Calculator(10)

# 链式操作
result = calc.add(5).multiply(2).subtract(3).divide(4).get_result()  # 返回: 5.75

# 获取计算历史
history = calc.get_history()  # 返回: ['+ 5', '* 2', '- 3', '/ 4']

# 清除计算器
calc.clear()
```

### 3.3 高级数学函数 (AdvancedMath)

`AdvancedMath` 类提供更复杂的数学函数：

```python
from mymathlib import AdvancedMath

# 阶乘计算
fact = AdvancedMath.factorial(5)  # 返回: 120

# 质数判断
is_prime = AdvancedMath.is_prime(17)  # 返回: True

# 斐波那契数列
fib = AdvancedMath.fibonacci(10)  # 返回: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 幂运算
power = AdvancedMath.power(2, 10)  # 返回: 1024

# 平方根
root = AdvancedMath.sqrt(16)  # 返回: 4.0
```

### 3.4 统计计算 (Statistics)

`Statistics` 类提供统计分析功能：

```python
from mymathlib import Statistics

# 数据集
data = [1, 2, 3, 4, 5, 5, 6]

# 平均值
mean = Statistics.mean(data)  # 返回: 3.7142857142857144

# 中位数
median = Statistics.median(data)  # 返回: 4

# 众数
mode = Statistics.mode(data)  # 返回: [5]
```

### 3.5 数学常量

MyMathLib 提供常用的数学常量：

```python
from mymathlib import PI, E, GOLDEN_RATIO, MathConstants

# 直接使用导出的常量
print(PI)  # 输出: 3.141592653589793
print(E)   # 输出: 2.718281828459045
print(GOLDEN_RATIO)  # 输出: 1.618033988749895

# 使用常量类
constants = MathConstants()
print(constants.LIGHT_SPEED)  # 输出: 299792458
print(constants.EULER_MASCHERONI)  # 输出: 0.5772156649015329
```

## 4. 错误处理

MyMathLib 在遇到无效输入时会抛出适当的异常，请确保在使用时进行错误处理：

```python
from mymathlib import MathOperations, AdvancedMath

try:
    # 尝试除以零
    ops = MathOperations()
    result = ops.divide(10, 0)
except ValueError as e:
    print(f"错误: {e}")

try:
    # 尝试计算负数的平方根
    result = AdvancedMath.sqrt(-1)
except ValueError as e:
    print(f"错误: {e}")
```

## 5. 示例代码

更多使用示例可以在项目的 `examples` 目录中找到：

- `basic_usage.py`: 基本功能的使用示例
- `advanced_usage.py`: 高级功能和组合使用的示例

## 6. 测试

MyMathLib 包含完整的测试套件，可以通过以下命令运行测试：

```bash
# 运行所有测试
python -m pytest tests/ -v

# 生成测试覆盖率报告
python -m pytest tests/ --cov=src/mymathlib
```

## 7. 反馈和贡献

如果您在使用 MyMathLib 过程中遇到问题或有改进建议，请访问项目的 GitHub 仓库：

- [GitHub 仓库](https://github.com/yourusername/mymathlib)
- [问题反馈](https://github.com/yourusername/mymathlib/issues)

我们欢迎并感谢您的贡献！

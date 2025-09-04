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

## 详细文档

请参阅 `docs/getting_started.md` 了解更详细的使用指南和示例。

## 使用示例

更多使用示例可以在 `examples` 目录中找到：

- `basic_usage.py`: 基本功能的使用示例
- `advanced_usage.py`: 高级功能和组合使用的示例

## 测试

MyMathLib 包含完整的测试套件，可以通过以下命令运行测试：

````bash
# 运行所有测试
python -m pytest tests/ -v
```bash
# 生成测试覆盖率报告
python -m pytest tests/ --cov=src/mymathlib
````

## 开发指南

### 环境准备

创建并激活虚拟环境：

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境 (macOS/Linux)
source venv/bin/activate

# Windows系统使用
# venv\Scripts\activate
```

安装项目的开发版本：

```bash
pip install -e .
```

安装测试依赖：

```bash
pip install pytest pytest-cov
```

### 运行测试

运行所有测试用例：

```bash
python -m pytest tests/ -v
```

生成测试覆盖率报告：

```bash
python -m pytest tests/ --cov=src/mymathlib
```

### 运行示例

执行基础使用示例：

```bash
python examples/basic_usage.py
```

执行高级使用示例：

```bash
python examples/advanced_usage.py
```

### 项目构建

构建可分发的包：

```bash
# 安装打包工具
pip install setuptools wheel twine

# 构建包
python setup.py sdist bdist_wheel

# 检查包
 twine check dist/*
```

## 版本历史

- v1.0.0: 初始版本发布

## 许可证

本项目采用 MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件

## 作者信息

- fengduke
- xingyaochenguang@163.com

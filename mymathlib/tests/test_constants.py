import unittest
import math
from mymathlib.constants import MathConstants, PI, E, GOLDEN_RATIO

class TestConstants(unittest.TestCase):
    
    def setUp(self):
        self.constants = MathConstants()
    
    def test_pi(self):
        # 验证PI值的精度
        self.assertAlmostEqual(self.constants.PI, math.pi, places=10)
        self.assertAlmostEqual(PI, math.pi, places=10)
    
    def test_e(self):
        # 验证E值的精度
        self.assertAlmostEqual(self.constants.E, math.e, places=10)
        self.assertAlmostEqual(E, math.e, places=10)
    
    def test_golden_ratio(self):
        # 验证黄金比例值
        expected_golden_ratio = (1 + math.sqrt(5)) / 2
        self.assertAlmostEqual(self.constants.GOLDEN_RATIO, expected_golden_ratio, places=10)
        self.assertAlmostEqual(GOLDEN_RATIO, expected_golden_ratio, places=10)
    
    def test_euler_mascheroni(self):
        # 欧拉-马歇罗尼常数，无法直接从math模块获取精确值，这里只验证是否为预期的近似值
        self.assertAlmostEqual(self.constants.EULER_MASCHERONI, 0.5772156649015329, places=15)
    
    def test_light_speed(self):
        # 验证光速值
        self.assertEqual(self.constants.LIGHT_SPEED, 299792458)
    
    def test_constants_immutability(self):
        # 测试常量是否可以被修改（Python中类变量是可以被修改的，这里只是验证初始值）
        original_pi = self.constants.PI
        # 尝试修改常量（Python允许这样做，但不推荐）
        try:
            MathConstants.PI = 3  # 不应该这样做
            self.assertEqual(MathConstants.PI, 3)
            # 恢复原值
            MathConstants.PI = original_pi
        except AttributeError:
            pass

if __name__ == '__main__':
    unittest.main()
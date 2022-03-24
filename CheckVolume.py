import unittest

def cube_volume(x):
    return x * x * x


class CheckVolume(unittest.TestCase):
    def test_volume_cube(self):
        x = 5.555
        result = cube_volume(5.555)
        self.assertAlmostEqual(result, x * x * x)

if __name__=="__main__":
    unittest.main()
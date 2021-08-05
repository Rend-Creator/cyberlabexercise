import unittest
import add_program

class TestProgram(unittest.TestCase):
    def test_program(self):
        result = add_program.add_values(10, 5)
        self.assertEqual(result, 15)
if __name__ == '__main__':
    unittest.main()
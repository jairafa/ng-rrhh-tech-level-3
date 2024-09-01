import unittest
from colisiones import contar_colisiones


class TestCountCollisions(unittest.TestCase):
    
    def test_example_cases(self):
        self.assertEqual(contar_colisiones('LR'), [0, 0])
        self.assertEqual(contar_colisiones('RL'), [1, 1])
        self.assertEqual(contar_colisiones('RRR'), [0, 0, 0])
        self.assertEqual(contar_colisiones('RRL'), [1, 2, 1])
        
    def test_no_collisions(self):
        self.assertEqual(contar_colisiones('LLL'), [0, 0, 0])
        self.assertEqual(contar_colisiones('RRRR'), [0, 0, 0, 0])
    
    def test_all_collisions(self):
        self.assertEqual(contar_colisiones('RLRLRL'), [1, 2, 3, 3, 2, 1])
    
    def test_additional_cases(self):
        self.assertEqual(contar_colisiones('RLRL'), [1, 2, 2, 1])
        self.assertEqual(contar_colisiones('RLLR'), [1, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()

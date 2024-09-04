import unittest
from polygon_area_calculator import Rectangle, Square

class TestPolygonAreaCalculator(unittest.TestCase):
    
    def test_rectangle(self):
        rect = Rectangle(3, 6)
        self.assertEqual(rect.get_area(), 18)
        self.assertEqual(rect.get_perimeter(), 18)
        self.assertEqual(rect.get_diagonal(), (3**2 + 6**2) ** 0.5)
        self.assertEqual(rect.get_picture(), "***\n***\n***\n***\n***\n***\n")

        rect.set_width(7)
        rect.set_height(3)
        self.assertEqual(rect.get_area(), 21)
        self.assertEqual(str(rect), "Rectangle(width=7, height=3)")

    def test_square(self):
        sq = Square(5)
        self.assertEqual(sq.get_area(), 25)
        self.assertEqual(sq.get_perimeter(), 20)
        self.assertEqual(sq.get_diagonal(), (5**2 + 5**2) ** 0.5)
        self.assertEqual(sq.get_picture(), "*****\n*****\n*****\n*****\n*****\n")

        sq.set_side(2)
        self.assertEqual(sq.get_area(), 4)
        self.assertEqual(str(sq), "Square(side=2)")

    def test_amount_inside(self):
        rect1 = Rectangle(10, 15)
        rect2 = Rectangle(3, 4)
        sq = Square(4)
        
        self.assertEqual(rect1.get_amount_inside(rect2), 12)
        self.assertEqual(rect1.get_amount_inside(sq), 6)
        self.assertEqual(sq.get_amount_inside(rect2), 0)

if __name__ == "__main__":
    unittest.main()

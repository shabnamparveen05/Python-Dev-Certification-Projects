import unittest
from budget_app import Category, create_spend_chart

class TestBudgetApp(unittest.TestCase):

    def setUp(self):
        self.food = Category("Food")
        self.entertainment = Category("Entertainment")
        self.business = Category("Business")

    def test_deposit(self):
        self.food.deposit(1000, "initial deposit")
        self.assertEqual(self.food.get_balance(), 1000)

    def test_withdraw(self):
        self.food.deposit(1000, "initial deposit")
        self.food.withdraw(10.15, "groceries")
        self.food.withdraw(15.89, "restaurant and more food")
        self.assertEqual(self.food.get_balance(), 973.96)

    def test_transfer(self):
        self.food.deposit(1000, "initial deposit")
        self.food.transfer(500, self.entertainment)
        self.assertEqual(self.food.get_balance(), 500)
        self.assertEqual(self.entertainment.get_balance(), 500)

    def test_check_funds(self):
        self.food.deposit(1000, "initial deposit")
        self.assertTrue(self.food.check_funds(100))
        self.assertFalse(self.food.check_funds(1001))

    def test_create_spend_chart(self):
        self.food.deposit(1000, "initial deposit")
        self.food.withdraw(10.15, "groceries")
        self.food.withdraw(15.89, "restaurant and more food")

        self.entertainment.deposit(1000, "initial deposit")
        self.entertainment.withdraw(15, "movies")
        self.entertainment.withdraw(20, "concerts")

        self.business.deposit(1000, "initial deposit")
        self.business.withdraw(50, "supplies")

        expected_output = (
            "Percentage spent by category\n"
            "100|          \n"
            " 90|          \n"
            " 80|          \n"
            " 70|          \n"
            " 60|          \n"
            " 50|    o     \n"
            " 40|    o     \n"
            " 30|    o     \n"
            " 20| o  o     \n"
            " 10| o  o  o  \n"
            "  0| o  o  o  \n"
            "    ----------\n"
            "     F  E  B  \n"
            "     o  n  u  \n"
            "     o  t  s  \n"
            "     d  e  i  \n"
            "        r  n  \n"
            "        t  e  \n"
            "        a  s  \n"
            "        i     \n"
            "        n     \n"
            "        m     \n"
            "        e     \n"
            "        n     \n"
            "        t     "
        )

        self.assertEqual(create_spend_chart([self.food, self.entertainment, self.business]), expected_output)

if __name__ == "__main__":
    unittest.main()


# Budget App

This is a simple budget app written in Python that allows users to track their expenses and create spending charts by category. The app includes functionality for depositing money, withdrawing money, transferring money between categories, and generating a spending chart.

## Usage

### Category Class

The `Category` class allows you to create budget categories, add deposits, withdrawals, and transfers, and check the balance.

#### Example

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
food.transfer(100, entertainment)

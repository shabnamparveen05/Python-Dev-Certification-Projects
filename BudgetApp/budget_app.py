class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []

    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_per_category.append(spent)
        total_spent += spent

    percentages = [(spent / total_spent * 100) // 10 * 10 for spent in spent_per_category]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| " + "  ".join("o" if percent >= i else " " for percent in percentages) + "  \n"
    chart += "    ----------\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     " + "  ".join(category.name[i] if i < len(category.name) else " " for category in categories) + "  \n"

    return chart.rstrip("\n")

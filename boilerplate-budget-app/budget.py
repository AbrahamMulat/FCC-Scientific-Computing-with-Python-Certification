class Category:
    def __init__(self, category):
        # self.description = description
        self.category = category
        self.ledger = []
        self.balance = 0.0

        # print("Title")
    def __str__(self):
        s = self.category.center(30, "*") + "\n"

        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            s += temp + "\n"

        s += "Total: " + str(self.get_balance())
        return s

    def deposit(self, amount, description=''):
        self.ledger.append(({"amount": amount, "description": description}))
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.balance - amount >= 0:
            # append to ledger
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        # return the current balance
        return self.balance

    def transfer(self, amount, bud_category):
        if self.balance > amount:
            self.withdraw(amount, "Transfer to {}".format(bud_category.category))
            bud_category.deposit(amount, "Transfer from {}".format(self.category))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
          return False


# 不是四舍五入，而是舍去个位！
def create_spend_chart(categories):
    s = "Percentage spent by category\n"
    sum = 0
    withdraws = {}
    for x in categories:
        withdraws[x.category] = 0
        for y in x.ledger:
            if y['amount'] < 0:
                withdraws[x.category] += y['amount']
        withdraws[x.category] = -withdraws[x.category]
    for x in withdraws:
        sum += withdraws[x]
    for x in withdraws:
        withdraws[x] = int(withdraws[x] / sum * 100)

    for i in range(100, -10, -10):
        s += str(i).rjust(3) + '| '
        for x in categories:
            if withdraws[x.category] >= i:
                s += 'o  '
            else:
                s += '   '
        s += '\n'
    s += ' ' * 4 + '-' * (1 + len(categories) * 3) + '\n'

    maxlen = 0
    for x in categories:
        if len(x.category) > maxlen:
            maxlen = len(x.category)
    for i in range(maxlen):
        s += ' ' * 5
        for x in categories:
            if len(x.category) > i:
                s += x.category[i] + '  '
            else:
                s += ' ' * 3
        s += '\n'
    return s[0:-1]


from datetime import datetime

class Transaction:
    def __init__(self,t_type,amount,category):
        self.t_type = t_type
        self.amount = amount
        self.category = category
        self.t_time = datetime.now()
    def __str__(self):
        return f"{self.t_type.title():<10} | ${self.amount:>10.2f} | {self.category.title():<20} | {self.t_time.strftime('%Y-%m-%d %H:%M:%S')}"
    
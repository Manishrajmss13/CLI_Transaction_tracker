class Budget:
    def __init__(self):
        self.budget_list = []
    def add_transaction(self,transaction):
        self.budget_list.append(transaction)
    def get_balance(self):
        bal = 0
        for t in self.budget_list:
            if t.t_type=='income':
                bal+=t.amount
            else:
                bal-=t.amount
        return bal
    def view_transactions(self):
        print(f"\n{'Type':<10} | ${'Amount':>10} | {'Category':<20} | {'Timestamp'}")
        print("-"*70)
        for t in self.budget_list:
            print(t)
    
    
from transaction import Transaction
from budget import Budget
import time
import sys

my_budget = Budget()

while True:
    print("""\n1.Add Income
2.Add Expense
3.View Balance
4.View All Transactions
5.Exit\n""")

    try:
        choice = int(input("Enter you choice : "))
    except ValueError:
        print('Invalid input! Enter a number between 1 between 5.')
        continue
    
    if choice==1:
        amount = float(input("Enter the amount : "))
        category = input("Enter the category : ").strip().lower()
        tr = Transaction("income",amount,category)
        my_budget.add_transaction(tr)
        
    elif choice==2:
        amount = float(input("Enter the amount : "))
        category = input("Enter the category : ").strip().lower()
        tr = Transaction("expense",amount,category)
        my_budget.add_transaction(tr)
        
    elif choice==3:
        balance = my_budget.get_balance()
        print(f'\nCurrent Balance : ${balance:.2f}')
    
    elif choice==4:
        my_budget.view_transactions()
            
    elif choice==5:
        print("Thanks for using this. Exiting the app...")
        for i in 'Bye Bye...':
            # sys.stdout.write(i+" ")
            # sys.stdout.flush()
            print(i,end=' ',flush=True) 
            time.sleep(0.5)           
        break
    
    else:
        print('Invalid choice. Enter a number between 1 and 5.')
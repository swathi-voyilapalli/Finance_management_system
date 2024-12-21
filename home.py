from transaction import add_transaction, get_transactions
from report import generate_report
from budget import set_budget

def finance_home(username):
    while True:
        choice = input("\n1. Make a Transaction\n2. Generate a Report\n3. Budget\n4.Logout\n\nChoose an option: ")
        if choice=='1':
            kind = input("\n1. Add Transaction\n2. Get Transaction History\n")
            if kind=='1':
                trans_type = input("\nEnter Transaction Type:")
                trans_amount = input("\nEnter Transaction Amount:")
                trans_catagory = input("\nEnter Transaction Catagory:")
                trans_date = input("\nEnter Transaction Date:")
                add_transaction(username,trans_type,trans_amount,trans_catagory,trans_date)
                
            elif kind=='2':
                get_transactions(username)       
                
        elif choice=='2':
            print("\n\nYour Budget Report\n\n")
            generate_report(username)
        elif choice=='3':
            print("\n\nSet Budget Below\n\n")
            bud_cat = input("\nEnter Budget Catagory:")
            bud_limit = input("\nEnter Budget Limit:")
            set_budget(username,bud_cat,bud_limit)
        else:
            return
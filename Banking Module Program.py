# Banking Module Program

# Function to create a bank account
def create_account():
    print("\n--- CREATE NEW BANK ACCOUNT ---")
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    initial_deposit = float(input("Enter initial deposit amount: $"))
    account_type = input("Enter account type (Savings/Checking): ")
    
    # Create account dictionary
    account = {
        "account_number": account_number,
        "account_holder": account_holder,
        "balance": initial_deposit,
        "account_type": account_type
    }
    
    print(f"\n✅ Account created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Account Holder: {account_holder}")
    print(f"Initial Balance: ${initial_deposit:.2f}")
    print(f"Account Type: {account_type}")
    
    return account

# Function to handle deposits
def deposit(account):
    print("\n--- DEPOSIT MONEY ---")
    print(f"Current Balance: ${account['balance']:.2f}")
    
    amount = float(input("Enter amount to deposit: $"))
    
    if amount > 0:
        account['balance'] += amount
        print(f"✅ ${amount:.2f} deposited successfully!")
        print(f"New Balance: ${account['balance']:.2f}")
    else:
        print("❌ Invalid deposit amount. Amount must be positive.")
    
    return account

# Function to handle withdrawals
def withdraw(account):
    print("\n--- WITHDRAW MONEY ---")
    print(f"Current Balance: ${account['balance']:.2f}")
    
    amount = float(input("Enter amount to withdraw: $"))
    
    if amount > 0:
        if amount <= account['balance']:
            account['balance'] -= amount
            print(f"✅ ${amount:.2f} withdrawn successfully!")
            print(f"New Balance: ${account['balance']:.2f}")
        else:
            print("❌ Insufficient funds!")
            print(f"Available balance: ${account['balance']:.2f}")
    else:
        print("❌ Invalid withdrawal amount. Amount must be positive.")
    
    return account

# Function to calculate interest on loans
def calculate_loan_interest():
    print("\n--- LOAN INTEREST CALCULATOR ---")
    
    principal = float(input("Enter loan principal amount: $"))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter loan period (years): "))
    
    # Simple interest calculation
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    print("\n--- LOAN INTEREST SUMMARY ---")
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Annual Interest Rate: {rate}%")
    print(f"Loan Period: {time} years")
    print(f"Total Interest: ${interest:.2f}")
    print(f"Total Amount to Repay: ${total_amount:.2f}")
    print(f"Monthly Payment: ${total_amount / (time * 12):.2f}")
    
    return interest, total_amount

# Function to display account details
def display_account(account):
    print("\n--- ACCOUNT DETAILS ---")
    print(f"Account Number: {account['account_number']}")
    print(f"Account Holder: {account['account_holder']}")
    print(f"Current Balance: ${account['balance']:.2f}")
    print(f"Account Type: {account['account_type']}")

# Main program function
def main():
    print("=" * 50)
    print("     WELCOME TO BANKING MODULE")
    print("=" * 50)
    
    # Create an account first
    account = create_account()
    
    while True:
        print("\n" + "=" * 40)
        print("         BANKING MENU")
        print("=" * 40)
        print("1. View Account Details")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Calculate Loan Interest")
        print("5. Create New Account")
        print("6. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            display_account(account)
        
        elif choice == '2':
            account = deposit(account)
        
        elif choice == '3':
            account = withdraw(account)
        
        elif choice == '4':
            calculate_loan_interest()
        
        elif choice == '5':
            account = create_account()
        
        elif choice == '6':
            print("\n✅ Thank you for using our banking module!")
            print("   Have a great day!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

# Run the main program
if __name__ == "__main__":
    main()
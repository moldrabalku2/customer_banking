# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # note for self from Savings account balance, interest_rate, months
    balance = float(input('Enter your starting balance for the savings account: '))
    interest = float(input('Enter your starting interest rate: '))
    maturity = float(input('Enter  enter the amount of months for this interest rate you would like: '))
    # Call the create_savings_account function and pass the variables from the user.
    savings_balance, interest_earned = create_savings_account(balance, interest, maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account: Updated Balance = {savings_balance}, Interest Earned = {interest_earned}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    balance = float(input('Enter your starting balance for the CD account: '))
    interest = float(input('Enter your starting interest rate: '))
    maturity = float(input('Enter  enter the amount of months for this interest rate you would like: '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(balance, interest, maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account: Updated Balance = {updated_cd_balance}, Interest Earned = {cd_interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()
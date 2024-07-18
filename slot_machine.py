import random
balance_file = 'balance.txt'

# Function to load the balance from the file
def load_balance():
    try:
        with open(balance_file, 'r') as file:
            balance = int(file.read().strip())
            return balance
    except FileNotFoundError:
        return 0  # Return 0 if file does not exist
    except ValueError:
        print("Error: Could not read balance from file.")
        return 0

# Function to save the balance to the file
def save_balance(balance):
    with open(balance_file, 'w') as file:
        file.write(str(balance))

balance= load_balance()

def choose_mode():

    print("What would you like to do? ")
    print("Options:")
    print("       Deposit[D]")
    print("       Withdrawl[W]")
    print("       Check Balance[B]")
    print("       Play Slots[P]")
    print("       Quit Game[Q]")

    mode = (input("Enter mode ")).lower()
    if(mode == 'd'):
        deposit()
    elif(mode == 'w'):
        withdraw()
    elif(mode == 'b'):
        check_balance()
    elif(mode == 'p'):
        play_game()
    elif(mode == 'q'):
        quit()
    else: 
        print("Enter a valid mode ")
        mode = (input("Enter mode ")).lower()

def deposit():
    global balance
    print("Minimum Deposit Amount is $100")
    print("Deposit Method:")
    print("       Bank Transfer[B]")
    print("       Crypto[C]")
    print("       UPI[U]")
    
    deposit_method = (input("Choose your deposit method: ")).lower()

    if deposit_method in ['b', 'c', 'u']:
        deposit_amt = int(input("Enter the amount you want to deposit: "))
    else:
        print("Please choose a valid deposit method ")
        choose_mode()
    
    if(deposit_amt < 100):
        print("DEPOSIT AMOUNT CAN'T BE LESS THAN $100")
        print("Please enter a valid amount")
        choose_mode()
    else:
        balance = balance + deposit_amt
        print("Your deposit was succesfull!")
        print("Your current balance is ",balance)
        save_balance(balance)
        choose_mode()
   
def withdraw():
    global balance
    print("Minimum Withdraw Amount is $110")
    print("Withdraw Method:")
    print("       Bank Transfer[B]")
    print("       Crypto[C]")
    print("       UPI[U]")
    
    withdraw_method = (input("Choose your withdraw method: ")).lower()

    if withdraw_method in ['b', 'c', 'u']:
        withdraw_amt = int(input("Enter the amount you want to withdraw: "))
    else:
        print("Please choose a valid withdraw method ")
        choose_mode()
    
    if(withdraw_amt < 110):
        print("WITHDRAW AMOUNT CAN'T BE LESS THAN $110")
        print("Please enter a valid amount")
        choose_mode()
    elif(withdraw_amt > balance):
        print("INSUFFICIENT BALANCE !!!")
        print("Your current balance is ",balance)
        choose_mode()
    else:
        balance = balance - withdraw_amt
        print("Your withdraw was succesfull!")
        print("Your current balance is ",balance)
        save_balance(balance)
        choose_mode()

def check_balance():
    load_balance()
    print(balance)
    choose_mode()

def spin_reels():
    symbols = ['A', 'B', 'C', 'D', 'E']
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

def calculate_payout(rows, result, bet_amount_per_row):
    winning_combinations = {
        ('A', 'A', 'A'): 500,
        ('B', 'B', 'B'): 8,
        ('C', 'C', 'C'): 5,
        ('D', 'D', 'D'): 3,
        ('E', 'E', 'E'): 2
    }
    payout = 0
    for row in range(rows):
        row_result = tuple(result[row])
        payout += bet_amount_per_row*winning_combinations.get(row_result, 0)
    return payout

def play_game():
    global balance
    bet_amount_per_row = int(input("How much do you want to bet on each row? "))
    max_rows = 3
    
    if balance < bet_amount_per_row:
        print("Insufficient balance to play.")
        play_game()
        return

    rows_to_bet = int(input(f"How many rows do you want to bet on (1-{max_rows})? "))
    if rows_to_bet < 1 or rows_to_bet > max_rows:
        print("Invalid number of rows.")
        play_game()
        return

    total_bet = bet_amount_per_row * rows_to_bet
    if balance < total_bet:
        print("Insufficient balance to place the bet.")
        play_game()
        return
    else: print(f"You placed a bet for {total_bet} over {rows_to_bet} rows ")

    balance -= total_bet
    result = spin_reels()
    payout = calculate_payout(rows_to_bet, result,bet_amount_per_row)
    balance += payout

    print("Spin Result: ")
    for row in result:
        print(row)
    
    if payout > 0:
        print(f"Congratulations! You won ${payout}.")
    else:
        print("Sorry, you didn't win this time.")
    print("Your current balance is $", balance)
    
    wish = input("Press ENTER to play again(q to quit)")
    if(wish == 'q'):
        quit()
    else: 
        play_game()

print("*******************  THE SLOT MACHINE  **************************")
choose_mode()

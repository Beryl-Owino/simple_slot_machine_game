# for this project we will assume we are working 3 by 3 slot machine.

import random

MAX_LINES = 3   # defining of constants
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_count = {   # List defination
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2

}


#**** checking if the user won
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
           winnings += values[symbol] *  bet
           winning_lines.append(line + 1)

    return winnings,winning_lines



#**** checking what was the out come of the slot machine
def get_slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):   # it will loop and store symbol times the number of count.
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]  # : making  copy of the because we will be deleting after making the choices
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


# **** transposing the our we got from get_slot_machine function
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len (column) - 1:   # the id statement was added to avoiding printing the | char after symbol
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()


#**** asking the user deposit amount****
def deposit():
    while True:
        amount = input("What amount would you deposit to start: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("To game enter amount greater than 0")
        else:
            print("Please enter a number")
    return amount


#****checking the users betting line****
def get_number_of_line():
     while True:
        lines  = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of line")
        else:
            print("Please enter a number")
     return lines


# ****checking with the user the amount they are willing to bet per line****
def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between $ {MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount



def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings}")
    if winning_lines:
        print(f"You won on lines: {winning_lines}")
    else:
        print("No winning lines.")
    return winnings - total_bet



#****the main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()

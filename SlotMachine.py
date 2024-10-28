import random


def spin_row():
    symbols = ['🍒','🔔','🍇','💵','⭐']

    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet*4
        elif row [0] == '🔔':
            return bet*6
        elif row [0] == '🍇':
            return bet*8
        elif row [0] == '💵':
            return bet*10
        elif row [0] == '⭐':
            return bet*15
    return 0


def main():
    balance = 100
    print("****************************************")
    print("Welcome to the Python Slot Machine")
    print("Symbols: 🍒🔔🍇💵⭐")
    print("****************************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet>balance:
            print("Insufficient funds.")
            continue

        if bet <=0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout> 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost.")

        balance += payout

        play_again = input("Would you like to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break
    if balance == 0:
        restart = input("Would you like to try again? (Y/N)").upper()
    if restart == 'Y':
        main()
    else:
        print(f"Game Over! Your final balance is ${balance}") 
if __name__ == '__main__':
    main()
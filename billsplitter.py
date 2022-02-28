
import random


def main():
    friends = {}
    winner = ""
    print("Enter the number of friends joining (including you):")
    n = int(input())
    if n <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(n):
            names = input()
            friends[names] = 0
        print("Enter the total bill value:")
        bill = int(input())
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        game = input()
        if game == "Yes":
            winner = random.choice([keys for keys in friends])
            print()
            print(f"{winner} is the lucky one!")
            billdiv = bill / (n - 1)
        else:
            print()
            print("No one is going to be lucky")
            billdiv = bill / n
        if bill % n:
            billdiv = round(billdiv, 2)
        else:
            billdiv = round(billdiv)
        for name in friends:
            if winner == name:
                continue
            friends[name] = billdiv
        print()
        print(friends)
        
        
if __name__ == "__main__":
    main()

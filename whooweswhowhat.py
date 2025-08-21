def get_friends_expenses():
    friends = []
    while True:
        name = input("Enter friend's name (or press Enter to finish): ").strip()
        if not name:
            break
        try:
            spent = float(input(f"How much did {name} spend (in INR)? "))
            friends.append({'name': name, 'spent': spent})
        except ValueError:
            print("Please enter a valid amount.")
    return friends

def calculate_settlements(friends):
    n = len(friends)
    if n == 0:
        print("No friends entered.")
        return
    total = sum(f['spent'] for f in friends)
    equal_share = total / n
    balances = [{'name': f['name'], 'balance': round(f['spent'] - equal_share, 2)} for f in friends]

    # Separate creditors and debtors
    creditors = [b for b in balances if b['balance'] > 0]
    debtors = [b for b in balances if b['balance'] < 0]

    settlements = []
    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor = debtors[i]
        creditor = creditors[j]
        amount = min(-debtor['balance'], creditor['balance'])
        settlements.append(f"{debtor['name']} owes {creditor['name']} ₹{amount:.2f}")
        debtor['balance'] += amount
        creditor['balance'] -= amount
        if abs(debtor['balance']) < 1e-2:
            i += 1
        if abs(creditor['balance']) < 1e-2:
            j += 1
    return settlements

def main():
    friends = get_friends_expenses()
    settlements = calculate_settlements(friends)
    if settlements:
        print("\nSettlement instructions:")
        for s in settlements:
            print(s)
    else:
        print("No settlements needed.")

if __name__ == "__main__":
    main()

def main():
    # 1. Girdi Alınması ve Doğrulama (While döngüleri ile)
    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance < 0:
                print("Starting balance cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            monthly_deposit = float(input("Enter monthly deposit: "))
            if monthly_deposit <= 0:
                print("Monthly deposit must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            rate = float(input("Enter monthly interest rate (%): "))
            if rate < 0:
                print("Interest rate cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            goal = float(input("Enter savings goal: "))
            if goal <= 0:
                print("Savings goal must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 4. Özel Durum: Başlangıç bakiyesi zaten hedefi karşılıyor mu?
    if starting_balance >= goal:
        print(f"\nThe starting balance already meets or exceeds the goal!")
        print(f"Goal reached in 0 months.")
        print(f"Final Balance: {starting_balance:.2f}")
        print(f"Total Interest Earned: 0.00")
        return

    balance = starting_balance
    total_interest = 0.0
    month = 0

    print(f"\n{'Month':<8} | {'Interest Earned':<16} | {'New Balance':<12}")
    print("-" * 42)

    # 2. Aylık Simülasyon Döngüsü (En fazla 60 ay)
    while month < 60:
        month += 1
        
        # Her ay önce faiz hesaplanır ve eklenir, ardından depozito eklenir
        interest_earned = balance * rate / 100
        balance += interest_earned + monthly_deposit
        total_interest += interest_earned

        print(f"{month:<8} | {interest_earned:<16.2f} | {balance:<12.2f}")

        # Bakiye hedefe ulaştıysa veya geçtiyse erken çıkış yap
        if balance >= goal:
            break

    # 3. Sonuç Ekranı
    print("-" * 42)
    if balance >= goal:
        print(f"Goal reached in {month} months.")
    else:
        print("Goal not reached within 60 months.")
        
    print(f"Final Balance: {balance:.2f}")
    print(f"Total Interest Earned: {total_interest:.2f}")

if __name__ == "__main__":
    main()

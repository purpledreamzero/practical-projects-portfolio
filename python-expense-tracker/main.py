def main():
    print("=== Python 個人記帳系統 ===")

    income = float(input("請輸入本月收入:"))
    expense = float(input("請輸入本月支出:"))
    balance = income - expense

    print(f"本月收入:{income} 元")
    print(f"本月支出:{expense} 元")
    print(f"本月結餘:{balance} 元")

if __name__ == "__main__":
    main()

def get_income():
    while True:            
        try:                
            float(input("請輸入本月收入:"))
        except ValueError:        # 輸入錯誤時顯示提示
            return
print("程式執行結束")








class Card:
    def __init__(self, cardID = None, accounts = None, pin = None):
        self.cardID = cardID
        self.accounts = accounts
        self.pin = pin

class Account:
    def __init__(self, account_ID = None, balance = None):
        self.account_ID = account_ID
        self.balance = int(balance)

    def show_balance(self):
        print (self.balance)

    def deposit(self, money):
        self.balance += int(money)
        print ("입금 금액 :" + money)
        print("잔액 : " + str(self.balance))

    def withdraw(self, money):
        if self.balance >= int(money):
            self.balance -= int(money)
            print("출금 금액 :" + money)
            print("잔액 : " + str(self.balance))
        else :
            print("잔액이 부족합니다.")


def insert_card():
    print ('Insert_Card')
    #카드 정보를 토대로 카드DB에서 카드 정보를 받아온다.
    myCard = Card("1234567-89", ["111-222-333", "222-333-444"], "1234")

    pin_process(myCard)


def check_pin_number(myCard, pin_number):
    # Bank API를 사용 예정.
    if myCard.pin == pin_number:
        return True
    else:
        return False


def pin_process(myCard):
    print("PIN Number : ")
    PIN_Number = input()
    if check_pin_number(myCard, PIN_Number):
        print ("PIN Number is Correct")
        select_account(myCard)
    else:
        print ("PIN Number is not Correct")
        exit()


def select_account(myCard): #계좌 선택
    for account in myCard.accounts:
        print("계좌 :" + account)
    print("계좌를 선택하시오 : ")
    account_selected = input()
    #계좌 번호를 토대로 계좌 정보를 가져온다. 아래는 10만원 잔액 계좌 정보를 가져왔을 때 예시
    myAccount = Account(account_selected, 100000)
    select_system(myAccount)


def select_system(myAccount):
    print("Balance / Deposit / Withdraw")
    Select_System = input()
    if Select_System == "Balance":
        myAccount.show_balance()
    elif Select_System == "Deposit":
        print("입금할 돈을 입력하세요.")
        money = input()
        myAccount.deposit(money)
        exit()
    elif Select_System == "Withdraw":
        print("출금할 돈을 입력하세요.")
        money = input()
        myAccount.withdraw(money)
        exit()


insert_card()

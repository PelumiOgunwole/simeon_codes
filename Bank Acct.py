"Modelling of a simple bank account. When atm is used to withdraw more than thrice, it deducts ATM Charges of #65"
import  random
class Bank:
    count=10
    no_of_withdrawal=0
    account_no=None
    phone_no=None
    account_bal=0.0
    BVN_no=0
    sms_charges=0.0

    def acct_details(self):
        print("Welcome to GT Bank")
        self.phone_no=input("Insert Phone No You Want to use for registering this account: ")
        print("Insert Phone No You Like To Register This Account With",self.phone_no)
        acc=str(217)
        self.account_no = random.randint(111111,9999999)
        final_acct_no=acc+str(self.account_no)
        print("Your Account No For GT Bank is: ",final_acct_no)
        bv=str(223)
        self.BVN_no=random.randint(111111,9999999)
        final_BVN=bv+str(self.BVN_no)
        print("Your Bvn No is: ",final_BVN)

    def credits(self):

        deposit=int(input("Are you making a deposit?" +"if Yes press 1, if no press 0"))
        if deposit ==1:
            payment=int(input("How much do you want to deposit?: "))
            self.account_bal+=payment
            print("Your current account balance is: " +"#",self.account_bal)
        else:input("Try something else")
    def debits(self):
        withdrawal = int(input("Do you wanna withdraw?" + "if Yes press 1, if no press 0"))

        if withdrawal==1:
            debit = int(input("How much do you want to withdraw?: "))
            if debit<self.account_bal:
                self.account_bal -= debit
                print("Your new balance is: " + "#", self.account_bal)

            elif debit>self.account_bal: print("Impossible withdrawal")



    def bank_atm_charges(self):
        print(self.no_of_withdrawal)
        atm_use=int(input("Do you wanna use ATM" + "if Yes press 1, if no press 0"))
        if atm_use==1:
            atm_cost=int(input("How much do you wanna withdraw from ATM: "))
            if atm_cost > self.account_bal:
                print("Impossible Transaction")
            elif atm_cost<self.account_bal:
                self.no_of_withdrawal += 1
                self.account_bal-=atm_cost
                print("Your current account balance is: ",self.account_bal)
            if self.no_of_withdrawal >=3:

                atm_withdrawal=65
                self.account_bal -= atm_withdrawal*(self.no_of_withdrawal-3)
                print("Your current account balance is: ",self.account_bal)
    def account_balance(self):
        self.acct_details()
        self.credits()
        self.debits()
        self.bank_atm_charges()
        self.bank_atm_charges()
        self.bank_atm_charges()
        self.bank_atm_charges()
        self.bank_atm_charges()


if __name__ == '__main__':
    gtb=Bank()
    gtb.account_balance()

class ATM:
    def __init__(self):
        self.bank={20:0,50:0,100:0,200:0,500:0}

    def deposit(self, banknotesCount: List[int]) -> None:
        i=0
        for currency in self.bank:
            self.bank[currency]+=banknotesCount[i]
            i+=1
        
    def withdraw(self, amount: int) -> List[int]:
        d=dict(sorted(self.bank.items(),key= lambda x:x[0], reverse=1))
        used={20:0,50:0,100:0,200:0,500:0}

        for i in d.keys():
            
            while amount>=i and d[i]>0:
                total=amount//i
                if d[i]>=total:
                    amount-=i*total
                    d[i]=d[i]-total
                    used[i]+=total

                else:
                    used[i]+=d[i]
                    amount-=i*d[i]
                    d[i]=0

                if amount<=0:
                    for i in used:
                        self.bank[i]-=used[i]
                    return used.values()
                
        return [-1]
        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)

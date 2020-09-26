import math
class Category:
    ledger = list()
    category = ''
    
    def completeStr(self, str1, str2='', str3 = ' '):
        if(str2 == ''):
            left = round(15 - len(str1)/2)
            right = 30 - left - len(str1)
            s = str1
            for i in range(left):
                s = '*' + s
            for i in range(right):
                s = s + '*'
            return s
        else:
            center = 30 - len(str1)- len(str2)
            s = ''
            for i in range(center):
                s = s + ' '
            return str1 + s + str2

    def __str__(self) -> str:
        strCategory = self.completeStr(self.category)
        s = ''
        count = 1
        for obj in self.ledger:
            am = ''
            if obj['amount'] >= 0:
                am = str(obj['amount'] +0.0001)
            else:
                print(round(obj['amount']-0.0001, 2), 'negativo')
                #if type(obj['amount']) is float
                am = str(obj['amount'] -0.0001)
            print(am, 'ppppp')
            pos = am.find('.')
            if len(obj['description'] + am[:pos+3]) < 30:
                s = s + self.completeStr(obj['description'], am[:pos+3]) + '\n'
            else:
                s = s + self.completeStr(obj['description'][:29-len(am[:pos+3])], am[:pos+3]) + '\n'
            if count >= 23:
                break
            count = count + 1
        balance = self.get_balance()
        balance = str(balance + 0.0001)
        strTotal = 'Total: '+ balance[:len(balance)-2]
        return strCategory + '\n' + s + strTotal

    def __init__(self, z):
        self.category = z
        print(self.category, 'constructed')

    def deposit(self, amount, description=''):
        obj = dict()
        obj['amount'] = amount
        obj['description'] = description
        arr = [obj]
        self.ledger = self.ledger + arr
        print('deposit', self.ledger)

    def withdraw(self, amount, description=''):
        obj = dict()
        obj['amount'] = -amount
        obj['description'] = description
        if self.get_balance() - amount > 0: 
            arr = [obj]
            self.ledger = self.ledger + arr
            print('withdraw')
            return True
        print('withdraw', self.ledger)
        return False

    def get_balance(self):
        balance = 0
        print(self.category)
        for item in self.ledger:
            balance = balance + item['amount']
            #print(balance, item)
        return balance
    
    def transfer(self, amount, budget):
        print('transfering....')
        if self.get_balance() - amount > 0:
            self.withdraw(amount, 'Transfer to '+ budget.category)
            print('transfered to '+ budget.category)
            budget.deposit(amount, 'Transfer from '+ self.category)
            return True
        print('succesfully')
        return False
    
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        elif self.get_balance() < amount:
            return False

def create_spend_chart(categories):
    title = 'Percentage spent by category'
    per = dict()
    total = 0
    for clss in categories:
        print(clss.ledger)
        objects = clss.ledger
        for obj in objects:
            print(obj)
            if(obj['amount'] < 0):
                #print(per[len(per)], clss.category)
                try:
                    per[clss.category] = per[clss.category] + abs(obj['amount'])
                except:
                    per[clss.category] =  abs(obj['amount'])
                total = total + abs(obj['amount'])
    print(per)
    char = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ',' 40| ',' 30| ', ' 20| ', ' 10| ', '  0| ']
    maxLenKey = 0
    listOfArrayKeys = list()
    for key, value in per.items():
        if len(key) > maxLenKey:
            maxLenKey = len(key)
        num = 11
        #create histogram array
        for i in range(len(char)):
            if math.floor((value/total)*10) >= num-i-1:
                char[i] = char[i] + 'o  '
            else: 
                char[i] = char[i] + '   '

    #generate list the names of categories
    for word in list(per.keys()):
        for i in range(maxLenKey):
            try:
                if i < len(word):
                    listOfArrayKeys[i] = listOfArrayKeys[i] + word[i] + '  '
                else:
                     listOfArrayKeys[i] = listOfArrayKeys[i] + '   '
            except:
                if i < len(word):
                    listOfArrayKeys.append('     ' + word[i]+'  ')
                else:
                    listOfArrayKeys.append('     ' + '   ')
    char.insert(0, title)
    char.append('    ')
    #append de axi
    for i in range(len(char[len(char)-2])-4):
        char[len(char)-1] = char[len(char)-1] + '-'
    char = char + listOfArrayKeys
    s = ''
    for i in range(len(char)):
        if i < len(char)-1:
            s = s + char[i] + '\n'
        else:
            s = s + char[i]
        
    #print(per, total, per[0]['Food']/total, perList)
    return s
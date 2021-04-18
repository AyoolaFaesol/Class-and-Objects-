class Budget:
    descrp = 'THIS IS A GROUP UNDER THE BUDGET CLASS WHICH CONTAINS CATEGORIES LIKE FOOD, CLOTHING AND ENTERTAINMENT AND ALSO THE TOTAL AMOUNT OF ALL THREE CATEGORIES IS PRESENT IN THE GROUP'
    
    def __init__(self, food, clothing, entertainment, total_amount):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.total_amount =  total_amount
    
    def deposit(self):
        self.deposit = int(input('how much would you like to deposit to this group? \n'))
        print('you have deposited %d' %self.deposit)
        return 'your new total amount is now {}'.format(self.total_amount + self.deposit)

        
    def withdrawal(self):
        print('HERE IS THE WITHDRAWAL SECTION')
        print('NOTE: Your withdrawal cannot exceed the available balance in this group')
        self.withdrawal = int(input('how much would you like to withdraw from this group? \n'))
        if self.withdrawal <= self.total_amount:
            return 'withdrawal succesful'
        else:
            exit('insufficient amount, try again')
          
    
    def bal(self):
        print('HERE IS THE CURRENT AVAILABLE BALANCE')
        self.bal = self.total_amount + self.deposit - self.withdrawal
        return self.bal
    
    def transfer(self):
        print('you can also transfer funds from one group to another under this section')
        print('NOTE: Amount to be transfered must not exceed the available amount in this group')
        self.transfer = int(input('how much would you like to transfer? \n'))
        if self.transfer < self.bal:
            return 'you have transfered %d to the other group' %self.transfer
        else:
            exit('transfer error as the amount exceeds the available balance')
    

        
grp_1 = Budget('rice', 'prada', 'musics', 20000)

grp_2 = Budget('beans', "gucci", 'movies', 30000)

print('THERE ARE TWO GROUPS IN "CLASS BUDGET"')
print('\n')

print(grp_1.descrp)
print('FOR GROUP ONE')
print(grp_1.deposit())

print('\n')

print(grp_2.descrp)
print('FOR GROUP TWO')
print(grp_2.deposit())

print('\n')

print('FOR GROUP ONE')
print(grp_1.withdrawal())

print('\n')

print('FOR GROUP TWO')
print(grp_2.withdrawal())

print('FOR GROUP ONE')
print(grp_1.bal())

print('\n')

print('FOR GROUP TWO')
print(grp_2.bal())

print('\n')

print('FOR GROUP ONE')
print(grp_1.transfer())

print('\n')

print('FOR GROUP TWO')
print(grp_2.transfer())

grp_2.new_amount = grp_1.transfer + grp_2.bal
grp_1.new_amount = grp_2.transfer + grp_1.bal
print('\n')

print('FOR GROUP ONE')
print('{} is the overall total amount available in grp_1 after a transfer was done from grp_2'.format(grp_1.new_amount))

print('\n')

print('FOR GROUP TWO')
print('{} is the overall total amount available in grp_2 after a transfer was done from grp_1'.format(grp_2.new_amount))
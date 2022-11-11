from account import Account, Checking

x = Checking(54321,654.33)
print(x)

x.withdraw(1000)

x.balance


def set(self, tit):
    self.__tit = tit

def get(self):
    return self.__tit

def __str__:
    return f'{self.get_titular()}' #nao acvessa atributo direta,emte

# __ acessa direto o atributo
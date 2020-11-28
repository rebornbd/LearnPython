class Super:
    var1    = None
    _var2   = None
    __var3  = None

    def __init__(self, var1=None, var2=None, var3=None):
        self.var1   = var1
        self._var2  = var2
        self.__var3 = var3
    
    def disPublicMem(self):
        print(self.var1)

    def _disProtectedMem(self):
        print(self._var2)

    def __disPrivateMem(self):
        print(self.__var3)
        self.__var3
    
    def accessPrivateMemFun(self):
        self.__disPrivateMem()

class Sub(Super):
    def __init__(self, var1=None, var2=None, var3=None):
        Super.__init__(self, var1, var2, var3)
    
    def accessProtectedMemFun(self):
        self._disProtectedMem()


superObj = Super('pub', 'pro', 'pri')
# print(f"{superObj.var1} {superObj._var2} {superObj._Super__var3}")
print(f"{superObj.var1} {superObj._var2} {superObj.accessPrivateMemFun()}")

subObj = Sub('pub', 'pro', 'pri')
print(f"{subObj.var1} {subObj._var2} {subObj._Super__var3}")

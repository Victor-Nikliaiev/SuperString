class SuperString:
    """
    Class to provide the type of a mutable string with some 
    additional params
    """
    def __init__(self, s):
        self.__s = list(s)
    
    def __iter__(self):
        self.__i = 0
        return self
    
    def __next__(self):
        if self.__i > len(self.__s) - 1:
            raise StopIteration
        else:
            a = self.__s[self.__i]
            self.__i = self.__i + 1
            return a
    
    def __len__(self):
        return len(self.__s)

    def __str__(self):
        return "".join(self.__s)

    def __iscorrectindex(self, i):
        if type(i) == int or type(i) == slice:
            if type(i) == int and i > self.__len__() - 1:
                raise IndexError            
        else:
            raise TypeError

    def __iscorrectindextoset(self, i):
        if type(i) == int:
            if i > self.__len__() - 1:
                return False  
            else: 
                return True         
        else:
            raise TypeError

    def __getitem__(self, i):
        self.__iscorrectindex(i)
        return self.__s[i]
    
    def __setitem__(self, i, v):
        if type(v) == int:
            v = str(abs(v))                                            
        if not self.__iscorrectindextoset(i):
            self.__s += list(v)
            return
        if len(v) > 1: 
            self.__s = self.__s[0:i] + [i for i in v] + self.__s[i:]
            return
        self.__s[i] = v
         

    def __delitem__(self, i):
        self.__iscorrectindex(i)
        del self.__s[i]

    def __contains__(self, v):
        return v in self.__s
    
    def __addition(self, s, m):       
        if type(s) == int or \
            type(s) == float or \
            type(s) == SuperString:
            s = str(s)            
        if type(s) == str:
            if m == 'l':
                return "".join(self.__s) + s                
            if m == 'r':
                return s + "".join(self.__s)                 
        raise TypeError("Types of data must be only digit or string")
               
    def __add__(self, s):        
        return self.__addition(s, 'l')

    def __radd__(self, s):             
        return self.__addition(s, 'r')

s1 = SuperString("Practiceperfect")
s1[8] = " make " 
print(s1)
print(s1 + 3)
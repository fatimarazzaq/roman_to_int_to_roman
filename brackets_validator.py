class Solution:
    valid_lst=[]
    parenthesis_pair={
    '(':')',
    '{':'}',
    '[':']',
}


    validity=[]
    def is_valid_parenthesis(self,mystr):
        for i in mystr:
            if i in self.parenthesis_pair.keys():
                self.valid_lst.append(i)
            elif i in self.parenthesis_pair.values():
                if self.parenthesis_pair[self.valid_lst[-1]]==i:
                    self.valid_lst.pop()
                    self.validity.append(True)
                else:
                    self.validity.append(False)


        if len(self.valid_lst)==0 and False not in self.validity:
            return True
        else:
            return False



s=Solution()
print(s.is_valid_parenthesis('[5+4(3*4)]'))
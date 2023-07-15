class special_sub_sequences:
    def AG (self,string):
        result=0
        count=0
        for i in string:
            if i=="A":
               count+=1
            if i=="G":
               result+=count
        return result
string=special_sub_sequences()
print(string.AG(input()))
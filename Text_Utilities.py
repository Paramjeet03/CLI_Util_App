class Text_Util:
    def Word_count(self,Text):
        s=[]
        for i in Text.strip().split(" "):
            if i !="":
                s.append(i)
        print("The list of word :- ",s,"\n","Total words :- ",len(s))
    
    def case_converter(self,Text,Case_S):
        if Case_S.strip()=="upper":
            print("Text In upper case :- ",Text.upper())
        else:
            print("Text In upper case :- ",Text.lower())

    def reverse_text(self, text):
        print( text[::-1] )
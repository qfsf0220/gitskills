class teststring:
    def __init__(self,pass_phrasestatic,plain_string,pass_phrasepublic):
        self.__plain_string = plain_string
        self.__pass_phrase =pass_phrasestatic
        self.pass_phrase =pass_phrasepublic

    @property
    def decrypt(self):
        if self.pass_phrase == self.__pass_phrase:
            return  self.__pass_phrase
        else:
            return "wrong"

    @decrypt.setter
    def decrypt(self,value):
        self.__pass_phrase=value

    def get_pass(self):
        return self.__pass_phrase

t = teststring("aaa","bbb","aaa")

t.decrypt="aaa1"
# print(t.__pass_phrase)

# print(t._teststring__pass_phrase)
# print("*"*80)
print(t.decrypt)

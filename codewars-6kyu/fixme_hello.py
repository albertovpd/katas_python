# FIXME: Hello

class Dinglemouse(object):
    def __init__(self):
        self.dictionary = {}
    def setAge(self, age):
        self.dictionary['age'] = f'I am {age}.'
        return self
    def setSex(self, sex):
        self.dictionary['sex'] = f"I am {'male' if sex=='M' else 'female'}."
        return self
    def setName(self, name):
        self.dictionary['name'] = f'My name is {name}.'
        return self
    def hello(self):
        return ' '.join(['Hello.'] + list(self.dictionary.values()))
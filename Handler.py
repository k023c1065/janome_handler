from janome.tokenizer import Tokenizer

class handler():
    def __init__(self):
        self.tokenizer = Tokenizer()
        
    def get_token(self,sentence):
        return self.tokenizer.tokenize(sentence)
    
    def analyze(self,sentence):
        tokens = self.get_token(sentence)
        result = {}
        for token in tokens:
            token=str(token)
            word,desc= token.split("\t")
            desc = desc.split(",")
            result[word]=desc
        return result
    
    def split_sentence(self,sentence):
        result = self.analyze(sentence=sentence)
        return list(result.keys())


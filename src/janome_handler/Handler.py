from janome.tokenizer import Tokenizer

class handler(Tokenizer):
    def __init__(self,*args):
        super().__init__(*args)
        
    def get_token(self,sentence):
        return self.tokenize(sentence)
    
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
    

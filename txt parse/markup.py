import sys,re
from handlers import HTMLRenderer
from util import blocks
from rules import rule_list

class Parser:
    '''parent'''
    def __init__(self,handler):
        self.handler=handler
        self.rules=[]
        self.filters=[]

    def addRule(self,rule:
        self.rules.append(rule)

    def addFilter(self,pattern,name):
        def filter(block,handler):
            return re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    
    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block=filter(block,self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last=rule.action(block,self.handler)
                if last:
                    break
        self.handler.end('document')
    
class BasicTextParser(Parser):
    def __init__(self,handler):
        super().__init__(handler)
        for rule in rule_list:
            self.addRule(rule)
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

def main():
    handler=HTMLRenderer()
    parser=BasicTextParser(handler)
    parser.parse(sys.stdin)

if __name__='__main__':
    main()
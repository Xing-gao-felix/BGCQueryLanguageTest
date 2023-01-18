from lark import Lark
from lark import Transformer
from lark import tree

class BGCQLToJSON(Transformer):
    def wherekeyword(self,items):
        return "WHERE"

    def querykeyword(self,items):
        return "QUERY"

    def booleanandconjunction(self,items):
        return "AND"

    def booleanorconjunction(self,items):
        return "OR"

    def data(self,items):
        return "BGC"

    def condition_feild(self,items):
        return items[0]

    def taxonomy_condition(self,items):
        return items[0]

    def superkingdom(self,items):
        return "superkingdom"


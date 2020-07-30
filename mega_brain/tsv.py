import csv

def get():
    expressions = []
    with open("tsv.txt") as src:
        for expr in csv.reader(src, dialect="excel-tab"):
            obj = {}
            obj['dif'] = expr[0]
            obj['type'] = expr[1]
            obj['expr'] = expr[2]
            obj['res'] = expr[3]
            expressions.append(obj)

    return sorted(expressions, key=lambda expr : expr['dif'])

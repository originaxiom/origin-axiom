import ast, builtins
src=open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'the_norm_of_the_boundary_class.py')).read()
tree=ast.parse(src)
defined=set(dir(builtins))
class V(ast.NodeVisitor):
    def __init__(s): s.stores=set(); s.loads=[]
    def visit_Name(s,n):
        if isinstance(n.ctx,(ast.Store,ast.Del)): s.stores.add(n.id)
        else: s.loads.append((n.id,n.lineno))
    def visit_FunctionDef(s,n):
        s.stores.add(n.name)
        for a in n.args.args+n.args.kwonlyargs: s.stores.add(a.arg)
        if n.args.vararg: s.stores.add(n.args.vararg.arg)
        s.generic_visit(n)
    def visit_Lambda(s,n):
        for a in n.args.args: s.stores.add(a.arg)
        s.generic_visit(n)
    def visit_Import(s,n):
        for a in n.names: s.stores.add((a.asname or a.name).split('.')[0])
    def visit_ImportFrom(s,n):
        for a in n.names: s.stores.add(a.asname or a.name)
    def visit_ExceptHandler(s,n):
        if n.name: s.stores.add(n.name)
        s.generic_visit(n)
v=V(); v.visit(tree)
und=[(n,l) for n,l in v.loads if n not in v.stores and n not in defined]
print("possibly undefined:", und)

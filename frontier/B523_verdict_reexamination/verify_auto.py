# Verify phi in Aut(F4) INDEPENDENTLY (not on chat3's authority):
# F_n is Hopfian => a surjective endomorphism is an automorphism.
# So it suffices to show a,b,A,B are each in im(phi) = <phi(a),phi(b),phi(A),phi(B)>.
# We exhibit explicit words and free-reduce to confirm.  (Uppercase = separate generators;
# inverses written with '~': a~ = a^{-1}, etc.)

def inv(w):
    out=[]
    for c in reversed(w):
        out.append(c[:-1] if c.endswith('~') else c+'~')
    return out
def reduce(w):
    st=[]
    for c in w:
        if st and ((st[-1].endswith('~') and st[-1][:-1]==c) or (c.endswith('~') and c[:-1]==st[-1])):
            st.pop()
        else:
            st.append(c)
    return st
def word(s):
    # parse 'aAB' or with inverses given as list already
    return list(s)
# images (letters a,b,A,B ; here A,B are their OWN generators)
al='a b A B'.split()
img={'a':['a','b','A','A','B'], 'b':['a','A','B'], 'A':['a','b','A','B'], 'B':['a','A']}
alpha,beta,gamma,delta = img['a'],img['b'],img['A'],img['B']

def build(seq):
    # seq is a list of (which_image, invert?) -> concatenate reduced
    w=[]
    for name,iv in seq:
        piece = {'al':alpha,'be':beta,'ga':gamma,'de':delta}[name]
        w += inv(piece) if iv else piece
    return reduce(w)

# candidate expressions (derived by hand):
a_expr = build([('be',0),('al',1),('ga',0),('be',1),('de',0)])   # beta alpha^-1 gamma beta^-1 delta
print("a  = beta a^-1 gamma beta^-1 delta ->", ''.join(a_expr), " == 'a' :", a_expr==['a'])
B_expr = build([('de',1),('be',0)])                               # delta^-1 beta
print("B  = delta^-1 beta                 ->", ''.join(B_expr), " == 'B' :", B_expr==['B'])
# A = a^-1 delta  (a as the word above)
A_expr = reduce(inv(a_expr)+delta)
print("A  = a^-1 delta                    ->", ''.join(A_expr), " == 'A' :", A_expr==['A'])
# b = a^-1 (gamma beta^-1) a
gb = reduce(gamma+inv(beta))
b_expr = reduce(inv(a_expr)+gb+a_expr)
print("b  = a^-1 (gamma beta^-1) a        ->", ''.join(b_expr), " == 'b' :", b_expr==['b'])

allgood = a_expr==['a'] and B_expr==['B'] and A_expr==['A'] and b_expr==['b']
print("\nall four generators in im(phi) => phi SURJECTIVE => (F4 Hopfian) phi in Aut(F4):", allgood)

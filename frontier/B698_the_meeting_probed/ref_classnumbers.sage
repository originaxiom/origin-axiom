from sage.all import QuadraticField, NumberField, polygen, QQ
print("=== class numbers (verify the meeting-invariant claim) ===")
for d in [-3, 5, -15]:
    K=QuadraticField(d)
    Cl=K.class_group()
    print(f"  Q(sqrt{d:>3}): disc={K.discriminant():>4}  h={K.class_number()}  Cl={Cl.invariants()}")
# genus theory: 2-rank of Cl(Q(sqrt d)) = t-1, t = #prime discriminant factors
print()
print("=== genus-theory 2-rank check (t-1, t=#prime-disc factors) ===")
def prime_disc_factors(d):
    from sage.all import fundamental_discriminant, factor
    D=fundamental_discriminant(d)
    # number of prime discriminants dividing D
    # prime discriminants: -4, 8, -8, (-1)^((p-1)/2) p for odd p
    from sage.all import prime_divisors
    t=0
    for p in prime_divisors(D):
        if p==2: t+=1
        else: t+=1
    return D,t
for d in [-3,5,-15]:
    D,t=prime_disc_factors(d)
    print(f"  Q(sqrt{d:>3}): fund.disc={D:>4}, #prime-disc factors t={t}, genus 2-rank=t-1={t-1}  -> |Cl[2]|=2^{t-1}")
print()
print("The biquadratic Q(sqrt-3,sqrt5): compositum, disc 225=15^2, h=1;")
print("its subfield Q(sqrt-15) is the ONLY one with h=2 -> the meeting's 2-torsion.")

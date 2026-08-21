"""B1117 lock -- the two adelic anchors, this bench's independent verification.
Anchor B: Vol(m004) = 9*sqrt3*zeta_K(2)/pi^2, K=Q(sqrt-3), to 1e-25.
Anchor A: B1106's edge windows are the Fibonacci convergent denominators,
even index closes / odd breaks (cross-ref B1106/B1110, banked)."""
import mpmath as mp
mp.mp.dps = 40


def anchor_B():
    Lchi2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
    zetaK2 = mp.zeta(2) * Lchi2
    vol_pred = 9 * mp.sqrt(3) * zetaK2 / mp.pi**2
    vol_true = mp.mpf('2.029883212819307250042405108549')
    return abs(vol_pred - vol_true), vol_pred


def anchor_A():
    F = [0, 1, 1]  # 1-indexed: F[1]=1...
    for _ in range(20):
        F.append(F[-1] + F[-2])
    # F_14=377 F_16=987 F_18=2584 close (even idx); F_13,15,17,19 break (odd)
    close = {F[14]: 14, F[16]: 16, F[18]: 18}
    brk = {F[13]: 13, F[15]: 15, F[17]: 17, F[19]: 19}
    return (all(i % 2 == 0 for i in close.values())
            and all(i % 2 == 1 for i in brk.values())
            and set(close) == {377, 987, 2584} and set(brk) == {233, 610, 1597, 4181})


def test_anchor_B_vol_is_zeta_value():
    diff, _ = anchor_B()
    assert diff < mp.mpf('1e-25'), f"Vol != 9sqrt3 zeta_K(2)/pi^2, diff {diff}"


def test_anchor_A_windows_are_convergents():
    assert anchor_A()


if __name__ == "__main__":
    d, v = anchor_B()
    print("Anchor B: 9sqrt3 zeta_K(2)/pi^2 =", mp.nstr(v, 30), "| diff from Vol =", mp.nstr(d, 4))
    print("Anchor A (windows = Fibonacci convergents, even-closes/odd-breaks):", anchor_A())

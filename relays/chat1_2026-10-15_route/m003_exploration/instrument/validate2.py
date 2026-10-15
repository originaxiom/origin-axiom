# EXPLORATION at excluded orders only: (a) d = e exactly at N = 5 (identical spectra, every cell); (b) a non-closing line
# must fail closure (negative control): up on L R^24's... use L R^25 with N = 5 but the line (1, 0), not fixed.
exec(open("twisted_explore.py").read().split('if __name__ == "__main__":')[0])
w = "L" + "R"*25
spec = {}
for sector, ch in (("down", (1, 2)), ("lepton", (-3, 6))):
    r = raw(w, 512, (0, 1), ch, 5)
    cs = cells(r)
    spec[sector] = {n: cs[n]["s"] / cs[n]["s"][0] for n in cs if cs[n] is not None}
dmax = max(float(np.max(np.abs(spec["down"][n] - spec["lepton"][n]) / np.maximum(spec["down"][n], 1e-300))) for n in spec["down"])
print("(a) N = 5, L R^25, line (0,1)/5: down vs lepton spectra, worst relative difference over all cells:", f"{dmax:.2e}")
r = raw(w, 384, (1, 0), (1, -4), 5)
print("(b) negative control, N = 5, L R^25, line (1,0)/5 (not fixed): closure", r["closure"])

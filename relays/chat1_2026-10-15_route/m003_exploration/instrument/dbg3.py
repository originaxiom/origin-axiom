exec(open("twisted_explore.py").read().split('if __name__ == "__main__":')[0])
M = matrix("L" + "R"*25); a, b, c, d = (int(x) for x in M.flatten()); tr = a + d
x0 = (a - d)/(2*c); rho = math.sqrt(tr*tr - 4)/(2*abs(c)); Pl = 2*math.acosh(tr/2)
s = -Pl/2 + Pl*np.arange(512)/512; Tun = x0 + rho*(np.tanh(s) + 1j/np.cosh(s))
ud = quat3(Tun, (3/5, 0), (-1/5, 0)); ul = quat3(Tun, (3/5, 0), (-9/5, 0))
ratio = ul/ud
bad = np.where(np.abs(ratio - 1) > 1e-6)
print("points with ratio != 1:", len(set(bad[0])), "of", len(Tun))
for p in sorted(set(bad[0]))[:6]:
    print("   tau", np.round(Tun[p], 3), "ratio", np.round(ratio[p], 4), "|u_down|", np.abs(ud[p]))

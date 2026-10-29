\\ narrow class numbers and SL2Z-class counts H(t) = sum over f^2 | t^2-4 with (t^2-4)/f^2 a discriminant of h+((t^2-4)/f^2)
hplus(D) = { my(h = qfbclassno(D), u = quadunit(D)); if (norm(u) == -1, h, 2*h) };
H(t) = { my(D = t^2 - 4, s = 0); fordiv(core(D,1)[2], f, my(d = D / f^2); if (d % 4 == 0 || d % 4 == 1, if (d > 1 && !issquare(d), s += hplus(d)))); s };
for (t = 3, 12, print("t=", t, " D=", t^2-4, " H(t)=", H(t), " hplus(D)=", if(issquare(t^2-4),"sq",hplus(t^2-4))));
print("quadunit(5)=", quadunit(5), " norm=", norm(quadunit(5)), " h(5)=", qfbclassno(5));

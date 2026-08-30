cd "$(dirname "$0")/certificates"
CERTS="cp1_strata cusp_beat jordan_beat a2_glue64 a5_parity_lemma b2_yukawa a4_pin c5_qp1 c1_weyl c2_habiro c2b_ohtsuki_bridge"
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "$c.py" > "../our_${c}.out" 2>&1
  rc=$?
  if [ -f "../outputs/${c}_out.txt" ]; then
    if diff <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../our_${c}.out" | tail -30) \
            <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../outputs/${c}_out.txt" | tail -30) >/dev/null 2>&1; then
      echo "  VERDICT: rc=$rc  REPRODUCES (verdict region identical)"
    else
      echo "  VERDICT: rc=$rc  DIFF"
    fi
  else
    echo "  VERDICT: rc=$rc  (no committed output)"
  fi
done
echo "===== REPRODUCE_DONE ====="

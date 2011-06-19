results = {}
for a in range(1, 999):
    for b in range(a + 1, 999):
        for c in range(b + 1, 999 - a - b):
            if a**2 + b**2 == c**2:
                p = a + b + c
                if p not in results:
                    results[p] = 0
                results[p] += 1
print max(results, key=results.get)

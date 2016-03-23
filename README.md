# Reservoir

A reservoir sampling implementation.

```bash
$ cat letters.txt | ./reservoir.py 10 -v
> Adding at index 0: 'A\n'
> Adding at index 1: 'B\n'
> Adding at index 2: 'C\n'
> Adding at index 3: 'D\n'
> Adding at index 4: 'E\n'
> Adding at index 5: 'F\n'
> Swap at index 0: 'A\n' -> 'G\n' (proba was 6/7)
> Swap at index 2: 'C\n' -> 'H\n' (proba was 6/8)
> Swap at index 3: 'D\n' -> 'L\n' (proba was 6/12)
> Swap at index 4: 'E\n' -> 'O\n' (proba was 6/15)
> Swap at index 4: 'O\n' -> 'R\n' (proba was 6/18)
G
B
H
L
R
F
```

# Reservoir

A reservoir sampling implementation.

```bash
$ cat letters.txt | ./reservoir.py -v 6
> Adding at index 0: 'A\n'
> Adding at index 1: 'B\n'
> Adding at index 2: 'C\n'
> Adding at index 3: 'D\n'
> Adding at index 4: 'E\n'
> Adding at index 5: 'F\n'
> [p=6/7] Swap at index 5: 'F\n' -> 'G\n'
> [p=6/8] Swap at index 1: 'B\n' -> 'H\n'
> [p=6/9] Swap at index 4: 'E\n' -> 'I\n'
> [p=6/11] Swap at index 3: 'D\n' -> 'K\n'
> [p=6/13] Swap at index 1: 'H\n' -> 'M\n'
> [p=6/15] Swap at index 4: 'I\n' -> 'O\n'
> [p=6/16] Swap at index 0: 'A\n' -> 'P\n'
> [p=6/19] Swap at index 0: 'P\n' -> 'S\n'
S
M
C
K
O
G
```

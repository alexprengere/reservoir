# Reservoir

A reservoir sampling implementation based on [this blog](http://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/), using high-fidelity approximation to the reservoir sampling-gap distribution.

```bash
$ cat letters.txt | ./reservoir.py -v 6
> Adding at index 0: 'A\n'
> Adding at index 1: 'B\n'
> Adding at index 2: 'C\n'
> Adding at index 3: 'D\n'
> Adding at index 4: 'E\n'
> Adding at index 5: 'F\n'
> [p=6/7] Swap at index 3: 'G\n' replaces 'D\n'
> [p=6/8] Swap at index 2: 'H\n' replaces 'C\n'
> [p=6/10] Swap at index 0: 'J\n' replaces 'A\n'
> [p=6/17] Swap at index 4: 'Q\n' replaces 'E\n'
> After gap 1, swap at index 0: 'Y\n' replaces 'J\n'
Y
B
H
G
Q
F
```

You can hit ctrl+C during the command execution, the signal will be caught and the sample will be printed on stdout.

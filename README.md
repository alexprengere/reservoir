# Reservoir

A reservoir sampling implementation based on [this blog](http://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/), using high-fidelity approximation to the reservoir sampling-gap distribution.

```bash
$ cat HUGE_FILE_BILLIONS_OF_LINES.txt | ./reservoir.py 1000
# wait, when bored, hit ctrl+C
line154
line786
# and 998 other lines selected with an equal probability
```

You can get more details on what is going on under the hood:

```bash
$ cat letters.txt | ./reservoir.py --verbose 6
> Adding element nb 0: 'A\n'
> Adding element nb 1: 'B\n'
> Adding element nb 2: 'C\n'
> Adding element nb 3: 'D\n'
> Adding element nb 4: 'E\n'
> Adding element nb 5: 'F\n'
> [p=6/7] Swap element nb 3: 'G\n' replaces 'D\n'
> [p=6/9] Swap element nb 5: 'I\n' replaces 'F\n'
> [p=6/10] Swap element nb 0: 'J\n' replaces 'A\n'
> [p=6/11] Swap element nb 2: 'K\n' replaces 'C\n'
> [p=6/16] Swap element nb 0: 'P\n' replaces 'J\n'
> [p=6/23] Swap element nb 4: 'W\n' replaces 'E\n'
> After skipping 1 line, swap element nb 5: 'Y\n' replaces 'I\n'
P
B
K
G
W
Y
```

You can hit ctrl+C during the command execution, the signal will be caught and the sample will be printed on stdout.

If you want to make tests on bigger data sets, you can build arbitrarily large files using this (600Mo needed!):
```bash
for i in `seq 1 100000`; do echo $i ; done > 100_000.txt
for i in `seq 1 1000`; do cat 100_000.txt ; done > 100_000_000.txt
```

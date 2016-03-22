# Reservoir

A reservoir sampling implementation.

```bash
$ cat letters.txt | ./reservoir.py 6
WARNING:root:Adding 'A\n' to unfilled reservoir
WARNING:root:Adding 'B\n' to unfilled reservoir
WARNING:root:Adding 'C\n' to unfilled reservoir
WARNING:root:Adding 'D\n' to unfilled reservoir
WARNING:root:Adding 'E\n' to unfilled reservoir
WARNING:root:Adding 'F\n' to unfilled reservoir
WARNING:root:[Probability 6/7] Replacing item at index 4 with 'G\n'
WARNING:root:[Probability 6/8] Replacing item at index 0 with 'H\n'
WARNING:root:[Probability 6/9] Replacing item at index 2 with 'I\n'
WARNING:root:[Probability 6/12] Replacing item at index 2 with 'L\n'
WARNING:root:[Probability 6/13] Replacing item at index 3 with 'M\n'
WARNING:root:[Probability 6/14] Replacing item at index 1 with 'N\n'
WARNING:root:[Probability 6/15] Replacing item at index 4 with 'O\n'
WARNING:root:[Probability 6/18] Replacing item at index 1 with 'R\n'
WARNING:root:[Probability 6/20] Replacing item at index 4 with 'T\n'
WARNING:root:[Probability 6/21] Replacing item at index 5 with 'U\n'
WARNING:root:[Probability 6/23] Replacing item at index 1 with 'W\n'
H
W
L
M
T
U
```

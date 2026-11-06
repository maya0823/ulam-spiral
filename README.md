# ulam-spiral

Write the positive integers in a square spiral that starts with 1 in the center and winds outward. Mark the prime numbers. The resulting pattern is called an Ulam spiral. Primes tend to form noticeable diagonal lines and other structures, which is surprising because primes are usually thought of as randomly distributed.

This tool builds the spiral for a given side length and marks the primes so you can see the pattern on the terminal.

## Usage

```
python ulam.py 15
```

That prints a 15x15 grid. Primes get a * after the number. At the end it reports how many primes appeared.

```
python ulam.py 21 --plain
```

Prints the numbers only, no markers.

Needs Python 3.7+. No extra packages.

## Notes

The prime check is a simple 6k+/-1 trial division. Fine for the sizes you would print on a terminal. Larger grids get wide and hard to read, so stick to something under ~40.

Even sizes are automatically bumped up by one so the center stays centered.

MIT License

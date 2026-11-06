# ulam-spiral

Generate the Ulam spiral for a given side length and mark the primes.

The spiral starts with 1 in the center and winds outward. Odd sizes work best so the center stays centered. Even sizes get bumped up by one.

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

MIT License

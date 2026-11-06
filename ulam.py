#!/usr/bin/env python3
"""Ulam spiral generator. Marks primes in a square spiral starting from 1 at the center."""

import argparse
import sys


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_ulam_spiral(size: int) -> list[list[int]]:
    """Build size x size grid. size should be odd. Center is 1, spiral outward."""
    if size % 2 == 0:
        size += 1  # force odd so there is a clear center
    grid = [[0] * size for _ in range(size)]
    x = y = size // 2
    grid[y][x] = 1

    # directions: right, up, left, down
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    dir_idx = 0
    step = 1
    num = 2

    while num <= size * size:
        for _ in range(2):  # each step length used twice
            for _ in range(step):
                x += dx[dir_idx]
                y += dy[dir_idx]
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                num += 1
                if num > size * size:
                    break
            dir_idx = (dir_idx + 1) % 4
            if num > size * size:
                break
        step += 1

    return grid


def print_spiral(grid: list[list[int]], mark_primes: bool = True) -> None:
    size = len(grid)
    max_num = size * size
    width = len(str(max_num)) + (1 if mark_primes else 0)

    prime_count = 0
    for row in grid:
        for val in row:
            if val == 0:
                print(" " * width, end=" ")
                continue
            marker = ""
            if mark_primes and is_prime(val):
                marker = "*"
                prime_count += 1
            print(f"{val}{marker}".rjust(width), end=" ")
        print()
    if mark_primes:
        print(f"\nPrimes marked with *. Total primes: {prime_count}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate an Ulam spiral and mark primes."
    )
    parser.add_argument(
        "size",
        type=int,
        help="Side length of the square (odd preferred; even is rounded up)",
    )
    parser.add_argument(
        "--plain",
        action="store_true",
        help="Print numbers only, no prime markers",
    )
    args = parser.parse_args()

    if args.size < 1:
        print("Size must be at least 1", file=sys.stderr)
        sys.exit(1)

    grid = generate_ulam_spiral(args.size)
    print_spiral(grid, mark_primes=not args.plain)


if __name__ == "__main__":
    main()

# Week 2 — Python Module Assignment (Professor: Anudit Pokhrel)

This repository contains seven small Python programs completed for the Week 2 assignment. Each script focuses on basic control flow, string manipulation, and dictionary usage to solve small, self-contained problems.

**Project Overview**
- **Purpose**: Practice control structures (loops, conditionals), basic parsing, and simple algorithms using Python.
- **Scope**: Seven standalone scripts that prompt for input and print results.
- **Platform**: macOS or any system with a modern Python interpreter.

**Folder Structure**
- `assignment_week_2_q1.py` — Process numbers from input, skip multiples of 5 and stop when number > 50.
- `assignment_week_2_q2.py` — Reverse every word at an odd index (0-based indexing: words 1, 3, ...).
- `assignment_week_2_q3.py` — Identify duplicate words and print a dictionary of duplicates with counts.
- `assignment_week_2_q4.py` — Simple inventory check for books with validation of requested copies.
- `assignment_week_2_q5.py` — Case-insensitive frequency count of words from input.
- `assignment_week_2_q6.py` — Return the largest (longest) word from a sentence.
- `assignment_week_2_q7.py` — Title-case a sentence (first letter upper, rest lower for each word).

**Prerequisites**
- Python `3.8+` recommended (any modern 3.x works).
- Terminal access to run scripts (`python3` on macOS).


**Script Details and Examples**

**Q1 — Numbers Filter and Stop (`assignment_week_2_q1.py`)**
- **Behavior**: Reads space-separated tokens, keeps integers (including negative), iterates through them and:
  - stops processing when a number > 50 is encountered (`break`),
  - skips printing numbers divisible by 5 (`continue`),
  - prints other numbers.
- **Notes**: Non-integer tokens are ignored. Negative integers are accepted.
- **Example**:

```
Enter numbers separated by space: 3 10 23 55 7
Output:
3
23
```

**Q2 — Reverse Words at Odd Index (`assignment_week_2_q2.py`)**
- **Behavior**: Splits the sentence into words and reverses words at odd indices (1, 3, ...), leaving even-indexed words unchanged.
- **Implementation detail**: Uses `while` loops to iterate and reverse characters manually.
- **Example**:

```
Enter a sentence: one two three four
Output: one owt three ruof
```

**Q3 — Duplicate Word Counter (`assignment_week_2_q3.py`)**
- **Behavior**: Counts occurrences of each space-separated item and prints a dictionary containing only words that appear more than once and their counts.
- **Example**:

```
Enter words separated by space: apple banana apple orange banana
Output: {'apple': 2, 'banana': 2}
```

**Q4 — Simple Book Inventory (`assignment_week_2_q4.py`)**
- **Behavior**: Predefined inventory for three books (`Book1`, `Book2`, `Book3`). Prompts for a book name and an integer number of copies to buy (validates integer input). Prints:
  - `Available` if inventory >= requested,
  - `Partially Available` if inventory > 0 but < requested,
  - `Unavailable` if none or book not listed.
- **Example**:

```
Enter the name of the book you want: Book1
Enter number of copies to buy: 3
Output: Available
```

**Q5 — Case-insensitive Word Frequency (`assignment_week_2_q5.py`)**
- **Behavior**: Counts occurrences of each word ignoring case and prints a dictionary mapping lowercase words to counts.
- **Example**:

```
Enter words separated by space: Apple apple BANANA banana
Output: {'apple': 2, 'banana': 2}
```

**Q6 — Largest Word (`assignment_week_2_q6.py`)**
- **Behavior**: Returns the longest word in the sentence (first encountered in tie). If there are no words, returns an empty string.
- **Example**:

```
Enter a sentence: find the longestword here
Output: longestword
```

**Q7 — Title Case (`assignment_week_2_q7.py`)**
- **Behavior**: Converts each word so the first character is uppercase and the rest are lowercase, rejoining with single spaces. Handles empty words gracefully.
- **Example**:

```
Enter a sentence: this IS a TeSt
Output: This Is A Test
```

**Testing Tips & Improvements**
- Provide clean inputs to avoid unexpected behavior (e.g., integers where expected).
- Edge cases to try:
  - Q1: non-integer tokens, negative numbers, first number >50, numbers divisible by 5.
  - Q2: empty input, multiple spaces (split handles them), punctuation in words.
  - Q3/Q5: punctuation — current code treats punctuation as part of words.
  - Q4: unknown book names (returns `Unavailable`), non-integer quantity input (re-prompts).
  - Q6: empty sentence.
  - Q7: words with mixed case and punctuation.
- Potential improvements:
  - Add unit tests for each script (use `unittest` or `pytest`).
  - Improve input parsing (handle floats, strip punctuation where appropriate).
  - Add a small CLI wrapper to choose and run questions interactively.

**Acknowledgements**
- Completed as part of the Python Module Week 2 assignment under Professor Anudit Pokhrel.

# Week 1 — Python Module Assignment (Professor: Anudit Pokhrel)

This repository contains six small, focused Python scripts completed for the Week 1 assignment. Each script introduces a fundamental concept: type conversion and formatting, string parsing, indexing and slicing, conditional logic, frequency counting, and character classification.

## Project Overview
- Purpose: Practice core Python concepts via small, interactive scripts.
- Scope: Six standalone programs, each prompting for input and printing results.
- Platform: macOS or any system with a modern Python interpreter.

## Folder Structure
- `assignment_week_1_q1.py` — Convert a decimal number to int and string; format output.
- `assignment_week_1_q2.py` — Extract uppercase initials from a provided full name.
- `assignment_week_1_q3.py` — Slice a given word from a specified starting index.
- `assignment_week_1_q4.py` — Assess password strength using simple rules.
- `assignment_week_1_q5.py` — Count frequency of alphabetic characters in a string.
- `assignment_week_1_q6.py` — Count vowels and consonants in a string.

## Prerequisites
- Python `3.8+` recommended (any modern 3.x works)
- Terminal access to run scripts (`python3` on macOS)

## How to Run
1. Open Terminal and navigate to the project folder:
   ```bash
   cd "/Users/prashantkoirala/Desktop/Python Module Assignemnt"
   ```
2. Run a script with:
   ```bash
   python3 assignment_week_1_qX.py
   ```
   Replace `X` with `1`–`6` depending on the question.

## Script Details and Examples

### Q1 — Number Conversion and Formatting (`assignment_week_1_q1.py`)
- Prompts for a decimal number, converts it to `int` and `str`, and prints the original float with two decimal places.
- Concepts: type casting (`int`, `str`), string formatting (`format`/`{:.2f}`).
- Example:
  ```text
  Please, enter a decimal number: 12.345
  Original float: 12.35
  Converted to integer: 12
  Converted to string: "12.345"
  ```

### Q2 — Initials from Full Name (`assignment_week_1_q2.py`)
- Trims whitespace, splits the full name by spaces, and prints uppercase initials from the first and last parts.
- Concepts: `strip`, `split`, indexing, string methods.
- Notes: For a single-name input, both initials derive from the same word (`A.A`).
- Example:
  ```text
  Please, enter your full name: Ada Lovelace
  Your initials are: A.L
  ```

### Q3 — Substring from Index (`assignment_week_1_q3.py`)
- Prompts for a word and a starting index, then prints the substring from that index to the end.
- Concepts: input parsing, `int` conversion, slicing (`word[index:]`).
- Edge behavior: Negative indices are allowed (Pythonic slicing). Out-of-range indices yield an empty string without error.
- Example:
  ```text
  Please, enter a word: python
  Enter starting index:
  2
  Substring from index 2 : "thon"
  ```

### Q4 — Password Strength (`assignment_week_1_q4.py`)
- Evaluates password strength using simple heuristics:
  - Weak: length `< 6` or only letters (`isalpha`).
  - Moderate: length `>= 6` and alphanumeric (`isalnum`).
  - Strong: length `>= 8` and contains at least one of `@#$%&`.
  - Else: Moderate.
- Concepts: conditionals (`if/elif/else`), length checks, membership tests.
- Notes: The strong rule is limited to the special set `@#$%&`. Other symbols are treated as non-strong unless included in that set.
- Example:
  ```text
  Please, enter your password: Passw0rd@
  Password strength: Strong
  ```

### Q5 — Alphabet Frequency (`assignment_week_1_q5.py`)
- Lowercases the text and counts occurrences of alphabetic characters (`a–z`). Non-letters are ignored.
- Concepts: dictionaries, iteration, `isalpha`, case normalization.
- Output order follows first occurrence insertion order of characters.
- Example:
  ```text
  Please, enter a string: Hello, World!
  h → 1
  e → 1
  l → 3
  o → 2
  w → 1
  r → 1
  d → 1
  ```

### Q6 — Vowel vs Consonant Count (`assignment_week_1_q6.py`)
- Lowercases input and counts vowels (`aeiou`) vs consonants; non-alphabetic characters are ignored.
- Concepts: classification, membership tests, conditional increments.
- Example:
  ```text
  Please, enter a string:
  Hello, World!
  Vowels: 3
  Consonants: 7
  ```

## Testing Tips
- Provide valid inputs to avoid `ValueError` (e.g., enter an integer for index in Q3).
- Try edge cases:
  - Q2: Single-word name, multiple middle names.
  - Q3: Negative and very large indices.
  - Q4: Short passwords, all letters, all digits, and with symbols outside `@#$%&`.
  - Q5: Mixed punctuation and spaces.
  - Q6: Strings with no letters.


## Acknowledgements
- Completed as part of the Python Module Week 1 assignment under Professor Anudit Pokhrel.

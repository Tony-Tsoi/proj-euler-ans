# Problem 17

## Problem Description
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

## Solve:
#### Number 1 - 9:
By counting: 36

#### Number 10 - 19:
As they are in form of "eleven" to "ninteen", instead of "ten-one" and so on => a separate catagory.

By counting: 70

#### Number 20 - 99:
For the ones = 8 * 36 = 288

For the tens, 10 * 46 = 460

Sum: 748

#### Number 100 - 999
Hundreds (1-9) = 100 * 36 = 3600

Repeating term "hundred" (len = 7) = 9 * 7 = 63

Repeating term "hundred and" (len = 10) = 891 * 10 = 8910

Repeating tens and ones (1-99) = 9 * (36 + 70 + 748) = 7686

Sum: 20259

#### Number 1000
By counting: 11

#### Answer
= 36 + 70 + 748 + 20259 + 11 = 21124

# Related Links / Useful resources

* 

--------

# 2020/01: Report Repair
* Part 1: Find the two numbers from a list that sum to 2020.
* Part 2: Find the three numbers from a list that sum to 2020.

Very easy. Just doing the naive way works fine. Input size is n=200.

# 2020/02: Password Philosophy

Input given is shaped like
```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

* Part 1: Count valid passwords. Validity check uses counting repetitions of a given character.
* Part 2: Count valid passwords. Validity check uses indexing and xor.

Fairly straightforword. Starts with regex / parsing. 

# 2020/03: Toboggan Trajectory

Given a map of trees and squares, like this:

```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

you start from the upper left corner and descend to the bottom row, using a given slope. (The columns repeat indefinitely as you go to the right) 


* Part 1: Using the given slope (3 right, 1 down), count how many trees you encounter until you pass through the map (below the last row).
* Part 2: Do the previous part for 5 different given slopes, and multiply the results together.

Overall wasn't too bad. Only need to do some modular adding to get the repetition to happen. 

An easy refactor was done to make part 2 work from part 1. 

# 2020/04: Passport Processing

Input looks like this:
```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```

Newlines separate passport entries. Whitespace characters (space, newline) separate key:value pairs. 

* Part 1: Count how many valid passports are in the dataset. Validation requires 7 out of 8 keys existing, with `cid` being optional.
* Part 2: Count how many valid passports are in the dataset. Validation requires checking the value associated to each key, except for `cid` which is still optional.

The first part I did quick and dirty. The second part required more time to implement, but wasn't more difficult.


# 2020/05: Binary Boarding

Boarding passes are of the form `HHHHHHHVVV` where `H` is either the character `F` for front, or `B` for back, and where `V` is either the character `L` for left or `R` for right. 

The halving is read from left to right. Binary is a very important clue to this exercise.

A seat's ID is given by 8 times it's row number plus its column number. 

You are given a list of boarding passes. 

* Part 1: What is the highest seat ID on a boarding pass?
* Part 2: Your seat is the only missing boarding pass on the list, where the seats 1 above and 1 below are on the list (there are seats at the very front or the very back of the plane which don't actually exist, so they don't show up on the list).

Pretty easy. String replace `F` with `0` and `B` with `1`, and also `R` with `1` and `L` with `0`. The boarding pass has become a binary number. Then convert it to an integer. The rest is straightforward.

For part 2, to identify the missing numbers in the list, I just took the set difference. By inspection, the largest value on my list was 816. Taking range(816) and set subtracting gives all missing numbers. 
Again by inspection, the odd number out is quickly discoverable.

# 2020/06: Custom Customs

There are groups of people that "answer" yes to various questions (characters a-z). Each line is a different person. Blank new lines separate groups of people. The data looks like this:

```
cudipzhqbmnavfrylg
qycingdprmuvhlbzfa
cdigzluybqfvmrahpn

phxsu
pxsuh
sxuhp
suhpx
```

* Part 1: For each group, count the number of questions to which *anyone* answered yes. The answer is the sum of these counts. 
* Part 2: For each group, count the number of questions to which *everyone* answered yes. The answer is the sum of these counts. 

I used set union and intersection for these.

# 2020/07: Handy Haversacks

This involves string parsing, and tree construction and counting of children nodes (if I set up the tree in that way).

Given rules of bag containment

* Part 1: Count how many bag colors eventually contain at least one shiny gold bag
* Part 2: Count how many bags are inside a shiny gold bag.

For part 1, I used the rules (in reverse order) to populate a dictionary pointing child -> containers. That way counting the possible containers can be done by repeatedly calling this dictionary. 

For part 2, I used the rules (in order) to populate a dictionary "children" and created a "count_children" function that uses recursion.

# 2020/08: Handheld Halting

You're given a program like this:
```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

* Part 1: Run the program until it loops (runs a line it already ran). What is the value in the accumulator immediately before the program loops?
* Part 2: There is exactly one instruction that is corrupted (jmp -> nop OR nop -> jmp). Repairing the code will make it terminate correctly. What is the value of the accumulator after the program terminates?

Both parts were relatively straightforward. 
To extend from part 1 to part 2, I wrapped the running code into a function `run_program`. To be able to answer part 2, I had to return a success value as well as the accumulator value.

# 2020/09: Encoding Error
You're given a list of numbers. 
* Part 1: Find the first number in the list that is not the sum of two of the 25 numbers before it (example uses window of length 5)
* Part 2: Find a contiguous set of at least two numbers that sums to the number you found in part 1. 

Length of the list was 1000. I could just brute-force. Didn't have to do anything that clever.


# 2020/10: Adapter Array
Gives a list of adapters (integers). 

* Part 1: Compute the number of 1-jolt differences multiplied by the number of 3-jolt differences
* Part 2: Find total number of arrangements of adapters that can be used.

First sort the list. 
For part 1, compute a list of differences. Then apply a counter to the list.

For part 2, we need to be smart. The number of arrangements can be determined by using the number of consecutive 1's in the list of differences. The analysis that concludes this can be found in `2020/day10analysis.txt`.

* 2 consecutive 1's corresponds multiplication by 2
* 3 consecutive 1's corresponds to multiplication by 4
* 4 consecutive 1's corresponds to multiplication by 7


# 2020/11: Seating System

Given a grid of seats, like so:
```
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
```
evolve it like a 2D cellular automata following given rules for seats become empty / occupied, until the seating has stabilized.
Return the number of occupied seats.

* Part 1: Rules consider adjacent seats
* Part 2: Rules consider the first visible seats in each of the eight directions.

I broke the code into many different functions. Modifying my code for part 2 wasn't so bad because of this. 

I encoded the grid of seats as a dictionary mapping coords to a character that marks occupied '#' OR empty 'L'. 
Using a "2D array" probably would have been fine also.


# 2020/12: Rain Risk

You're given instructions for navigating a ship. 

* Part 1: Actions move the ship and rotate it. Compute Manhattan distance after executing all instructions.
* Part 2: Actions move waypoint, rotate it relative to the ship, and move ship in direction of waypoint by an integer multiple. Compute Manhattan distance after executing all instructions.

Pretty easy.

# 2020/13: Shuttle Search (PARTWAY)

Given a starting time and a series of buses (comma separated) like so:
```
939
7,13,x,x,59,x,31,19
```
Buses depart at multiples of their ID number.

* Part 1: Find the ID of the earliest bus you can take, and multiply by how long you'll need to wait for it.
* Part 2: 

Part 1 was straightforward. 

Part 2 is mathematical? Solve system of modular congruences? Unless there's an easier way?

# 2020/14: Docking Data

Given input like
```
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
```

* Part 1. Mask is applied to value before storing into memory.  '1' and '0' override the value's bit. The 'X' uses the value's bit.
* Part 2. Mask is applied to the address. The 'X' represents all values, '0' does not modify that address bit, '1' overrides the address bit with '1'. So a masked-address of '0XX1' will correspond to 4 addresses that the value will be stored to.

Part 1 was pretty straightforward. Just need to know how to convert to binary, left-pad the string, and to covert back to base 10.

Part 2, had to consider the recursion to get all addresses matching a masked-address.


# 2020/15: Rambunctious Recitation

Follow a counting game, where the next number in the sequence is given by the distance between the previous number and its previous occurrence. 

So a sequence starting with `0,3,6` goes like

```
index: 1 2 3 4 5 6 7 8 9 10 ...
vals : 0 3 6 0 3 3 1 0 4  0 ...
```

* Part 1. Find the 2020th number in the sequence.
* Part 2. Find the 30,000,000th number in the sequence.

Implemented Part 1 the naive way (storing all values) because N=2020.

Redesigned for Part 2, where N=30,000,000. Created a dictionary `last_index` that maps value -> last index of occurence. 
Still, will likely store ~30,000,00 vals as repetitions may not be so common. 

Was able to get the answer, though slowly, and running may still yield Out of Memory if not enough available. Not sure how to further optimize. 

# 2020/16: Ticket Translation

Given a ticket like:
```
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
```

* Part 1: Values in the nearby tickets are invalid if they are not valid for any field. Sum up all invalid values in the nearby tickets.
* Part 2: Ignore all invalid tickets. 
As a further example (all tickets valid):
  ```
  class: 0-1 or 4-19
  row: 0-5 or 8-19
  seat: 0-13 or 16-19

  your ticket:
  11,12,13

  nearby tickets:
  3,9,18
  15,1,5
  5,14,9
  ```
  From the nearby tickets, determine which column corresponds to which field. Multipy the six fields on *your* ticket that start with the word `departure`.


I used range objects to make use of the `in` comparison (see helper function `make_range(input)`). 

Reading in the data was a bit ugly. I had to use a `part` integer variable to separate the different parts of the data, and to detect which part by using specific line headings.

For part 1, I put all ranges into a `all_ranges` list (ignoring ticket fields) and used a `ticket_error(lst)` method to help total up the invald values.

Part 2 was trickier. An oversight of mine: `ticket_error == 0` does not mean the ticket is valid. In my data, there was a ticket with a field having value `0` but such value wasn't allowed by my constraints. 
I used `ticket_valid(lst)` to clean the list of nearby tickets. 

I used a `possible_fields(nums)` function to determine for each column, what possible ticket fields that column could be.
I stored this data in an `associations` dict `int -> list(str)` that maps column numbers to ticket fields.

This `associations` dict is then fully simplified using two simplifier methods, so that the `column -> ticket_field` association is known. (Turns out only one of them is actually needed, but I didn't know because I didn't catch the `ticket_error==0` mistake until after implementing both and noticing issues with the outputted simplifications.)
The rest is straightforward.

# 2020/17: Conway Cubes

Gives an input config in the form of:
```
.#.
..#
###
```

* Part 1: Input is for 3d cellular automata. Gives update rules. Run for six steps and count number of active cells.
* Part 2: Input is for 4d cellular automata. Everything else is the same.

I used a dictionary `grid` mapping `tuple -> bool`. I made utility methods `adjacents(coord)`, `count_active_adjacent(grid, coord)`, `potential_coords(grid)` that helped to deconstruct the method for executing a single step `step(grid)`. 

The `potential_coords` function was perhaps a clever optimization. The idea was that to create the next grid-state, I didn't need to use all possible coordinates (applying `adjacents` to the entire `grid`). Instead, the only coordinates that are important (and hence need to be computed) are those that are already on ("active"), and those that might turn on (adjacent to active coords). This also helps by throwing away unneeded entries in subsequent `grid`s. 

Luckily or not, the way I combined these methods, going from part 1 to part 2 only involved introducing 3 lines for the data read-in, and 4 lines to overload the `adjacents(coord)` utility method to handle both 3-tuples and 4-tuples.

# 2020/18: Operation Order

Given a list of math expressions involving addition, multiplication and parentheses like:
```
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
```
except the rules of precedence are different from usual.

* Part 1: Addition and multiplication are equal precedence, computed from left to right. Compute sum of all calculations.
* Part 2: Addition takes precedence over multiplication. Compute sum of all calculations.

The first issue to deal with is tokenizing the expression-string, because `string.split(' ')` won't work for any expression with parens. I created a `tokenize` function that uses `list(string)` followed by `filter` to remove the `' '` characters.

For part 1, I noticed that if the expression doesn't have any parentheses, the answer can be computed directly, and this serves as the "easy" case for recursion. (This gets pulled out to the function `simple_calc1` when I refactor for part 2.)
I use a `split_to_ops` helper function to turn the tail of the expression into a "list" of pairs `[op, num]` that are easily processed.
This is the first half of the main function `calc(expr_lst)`. 
The rest of `calc` is if the expression has parens. It captures the subexpression contained in parens and recursively calls `calc` to get the sub-result, then does a sublist-replacement to the expression-list. Recursion occurs again, with another call to `calc` on this simplified expression-list. 

For part 2, I noticed the recursion logic for handling parenthesized subexpressions in `calc` still applies, but the logic for computing the "simple calculations" without parens needs to be swapped out to handle the different precedence rule. So I refactored `calc(expr_lst, simple_calc)` to take an argument `simple_calc` which is a first-class function used to evaluate expressions without parentheses, with `simple_calc1` being the logic from part 1. The refactoring is straightforward.
I then just have to create the function `simple_calc2`. Addition takes precedence over multiplication, so all subexpressions with `'+'` are handled (modifying the expression-list) until all that's left are multiplications, which are then easily handled (I used `functools.reduce` and `operator.mul`, after filtering).

# 2020/19: Monster Messages (STUCK)
Input is of the form:
```
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
```

This is basically asking to create a lexer that matches against a given grammar. 
TODO: read about how to create lexer from a language grammar? Finite state machine?

* Part 1: How many messages match rule `0`?

# 2020/20: Jurassic Jigsaw (TODO)

An image has been split into a collection of tiles that have been rotated and flipped to random orientations. Tiles that should be adjacent will have matching borders. Reconstruct how the tiles should be arranged.

# 2020/21: Allergen Assessment

Given list of encoded ingredients (with allergens possibly listed in plain).

```
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
```

Walkthrough of this example:
* Can conclude `mxmxvkd=dairy` from first 2 lines.
* Then, lines 1 and 4 conclude `sqjhc=fish`.
* Then line 3 and knowledge of encoding concludes `fvjkl=soy`.
* We were able to determine all the allergens. Remaining words are safe (`kfcds`, `nhms`, `trh`, `sbzzf` twice) so answer is `5`.


* Part 1: Determine which ingredients cannot possibly contain any of the allergens in the your list. How many times do those ingredients appear?
* Part 2: Arrange the ingredients alphabetically by their allergen. Answer is this as a comma-separated list.

All the work was in part 1. I reshaped the data so that I could, for each allergen, intersect the sets of potential ingredients to make a `potentially_contains` dict mapping `allergen -> list(ingredients)`. 
I then simplified this dict. Entries where the ingredients list only has one ingredient are known associations. They get added to the dict `contains_allergen: ingredient -> allergen`, and then all references to that allergen are removed from `potentially_contains`. Repeat until stabilized. Then all unsafe ingredients can be obtained from the two dictionaries, and all safe ingredients can be counted.

Part 2 was a simple dictionary-structure manipulation. All the needed information was already stored in `contains_allergen`. Used a function call `sorted(dict, key=dict.get)` to sort a dictionary's keys by the dictionary's values.

# 2020/22: Crab Combat

* Part 1: Simulate a card game of war, with given input decks. 
* Part 2: Simulate a game of "recursive combat", where rounds require (if possible to recurse) playing a subgame of 'recursive combat' to determine the winner of a round and otherwise, follow normal 'war' rules.

Coding part 1 was straightforward. Key things were that 
1) I uses `collections.deque` to model a deck.
2) I used a one-liner to compute the score of the winning hand:
   ```python 
   sum([i*j for i,j in zip(deck, reversed(range(1,len(deck) + 1)))])
   ```

Part 2 was roughly straightforward in the sense that you just have to carefully read the specification of the problem and how the recursion should behave, and code it up.

In particular, 
* The outermost game is a game of recursive combat.
* Subgames of recursive combat are used to determine winners of a round.
  * The winner is the person with all the cards at the end (same as war).
* The check for a reoccuring round occurs per (sub)game, so the memory variable needs to be inside the `recursive_combat` function.
* I noticed that the return behavior of `recursive_combat` should bifurcate. The result for subgames should return the winner (1 or 2) of the subgame, as it determines the winner of the round in the parent-game. But the result for the main game should return the winner's deck, or the winner's score for use in printing the answer. Because of this, I introduced the field `depth` to `recursive_combat` to bifurcate the type of return value.


# 2020/23
# 2020/24
# 2020/25

------

# 2019/01: The Tyranny of the Rocket Equation
A rocket has multiple modules with various masses. Launching a given module requires fuel. 
Compute the total fuel required for all modules.

* Part 1: The amount of fuel required is given by the formula: $fuel(mass) = \lfloor mass / 3 \rfloor - 2$.
* Part 2: Fuel has mass, meaning that fuel is needed to lift it, making the computation recursive.


# 2019/02: 1202 Program Alarm
Begin developing Intcode computer.
Has opcodes `1` add,  `2` multiply, and `99` terminate. 

Example program:
```
1,9,10,3,
2,3,11,0,
99,
30,40,50
```

First line says add values in position 9 and position 10 and store result in position 3. The computer's memory and code are theoretically intermingled (Self-modifying code. Memory can be executed as code. No boundary between the two).

* Part 1: Implement Intcode computer with opcodes `1`,  `2`, and `99`. 
Read in a program, load values `12`  and `2` into positions 1 and 2, and execute.
Answer is the value at position 0 after program has executed.

  String splitting. Indexing is somewhat tricky. I don't think it was too bad.

* Part 2: Find the two inputs that make the program yield a given output.
  
  Inputs are values between `0` and `99`. This is just a doubly-nested loop. Pretty easy to implement. Program should be reloaded for every execution.


# 2019/03: Crossed Wires

Sample input:

```
R8,U5,L5,D3
U7,R6,D4,L4
```

Each line represents a wire. Visually, it looks like this:
```
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

The `X` marks where the two wires cross. The `o` is the "central port" where the wires start.

* Part 1: Determine the distance from the central port to the closest intersection, using Manhattan distance.

  For each wire, I determined all coordinates that comprise the wire. I then took the set intersection to get all intersection points. Apply manhattan distance to all the intersection points and take the minimum distance.

* Part 2: Determine the closest intersection point of the two wires in terms of length travelled on the wires (both)

  The amount travelled on a wire to reach a given coordinate can be given by the coordinate's index in the list of coordinates of the wire. 
  I used this fact to produce a `timed_dist` function. Applying this function to the set of all intersection points and taking the minimum gives the answer. 

# 2019/04: Secure Container

* Part 1: Count the number of passwords in a certain range meet a given criteria
* Part 2: Criteria is modified to be a bit more specific/involved

# 2019/05: Sunny with a Chance of Asteroids 

Extend functionality of Intcode computer. 

* Opcode `3` takes input and stores it at a specified position. So `3,50` takes an input value and stores it at address `50`. 
* Opcode `4` outputs the value of its only parameter. So `4,50` would output the value at address `50`. 

Parameter modes:
```
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
```

The instruction `1002,4,3,4,33` is a multiply (opcode `02`) with the first parameter in position mode, the second parameter in immediate mode, the third in position mode. So we take the value stored at position 4, multiply by 3, and store back to position 4. 

* Opcode `5` jump-if-true: if first parameter is nonzero, set the instruction pointer to the value of the second parameter
* Opcode `6` jump-if-false: if first parameter is zero, set instruction pointer to value of the second parameter.
* Opcode `7` less than: If first parameter is less than the second parameter, store 1 in the position given by the third parameter. Otherwise store 0. 
* Opcode `8` equals: If first parameter equals second parameter, store 1 in position given by the third parameter. Otherwise store 0. 

* Part 1: Add intput and output functionality and position/immediate value modes to the Intcode runner. 
* Part 2: Add jump and comparison operations to Intcode runner

# 2019/06: Universal Orbit Map

* Part 1: Read in a tree and count the "total depth" of the tree
* Part 2: Find distance between two nodes in a tree


# 2019/07: Amplification Circuit (STUCK)

Need to refactor code so that can daisy-chain Intcode computer instances.
Need to modify input and output so that can chain together.

* Part 1: Iterate through (and chain together) initialization states for the Intcode runner to produce a maximum output. 

# 2019/08: Space Image Format

* Part 1: Read in a "layered image". Compute a checksum
* Part 2: Aggregate the layers to produce a final image. 

# 2019/09: Sensor Boost (PAUSED)
* Part 1: Add relative mode to Intcode runner

# 2019/10: Monitoring Station
# 2019/11: Space Police
# 2019/12: The N-Body Problem
# 2019/13: Care Package
# 2019/14: Space Stoichiometry
# 2019/15: Oxygen System
# 2019/16: Flawed Frequency Transmission
# 2019/17: Set and Forget
# 2019/18: Many-Worlds Interpretation
# 2019/19: Tractor Beam
# 2019/20: Donut Maze
# 2019/21: Springdroid Adventure
# 2019/22: Slam Shuffle
# 2019/23: Category Six
# 2019/24: Planet of Discord
# 2019/25: Cryostasis

--------

# 2018/01: Chronal Calibration

You're given a list of freqency changes like `+1, -2, +3, +1` except newline-separated instead of comma-separated. The starting frequency is 0.

* Part 1: Find the resulting frequency after applying all the changes. 
* Part 2: The list of frequency changes loops indefinitely. Find the first frequency that gets reached twice.

Part 1 is easy. Just add all the numbers up. 
Part 2 isn't so bad. Just keep a set of all frequencies reached, and each time, check the new frequency is already in the set.


# 2018/02: Inventory Management System

Given a list of box IDs (strings of the same length that look similar, except for some different characters).

* Part 1: Find the number of IDs that contain exactly 2 of any letter, and the number of IDs that contain exactly 3 of any letter. The answer is the product of these two numbers.
* Part 2: Find the pair of box IDs in the list that differ by only one character. The answer is the characters that are the same between the two.

For part 1, I used Counters. Part 2, I just brute force looped over all pairs. Needed to create a hamming_distance function.

# 2018/03: No Matter How You Slice It

You're given data that looks like this:
```
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
```

They are claims on parts of fabric (all are rectangles). 
In particular the claim `#NUM @ a,b: wxh` would correspond to a claim with ID `NUM` starting `a` from the left, `b` from the top, with width `w` and height `h`. 

* Part 1: There are claims that overlap. Count how many positions are contained in more than one claim.
* Part 2: There is exactly one claim that does not overlap with any other. Find its ID.

For part 1, 
I populated a dictionary (called "coverage") that, given a coordinate, would return the number of rectangles (claims) that contained the coordinate. After populating such a dictionary, answering part 1 is easy.

For part 2, the rectangle we're looking for would have a max coverage of 1.

# 2018/04: Repose Record

You're given records that look like
```
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
```
These records are not in order.

* Part 1: Find the guard with the most minutes asleep. What minute does that guard spend asleep the most? Answer is the ID of the guard multipled by the minute.
* Part 2: Which guard is the most frequently asleep n the same minute?

I started by sorting the entire file. I think I used vim to do that, or maybe shell commads.

I populated a dictionary `sleep_data` that maps each guard number to a list of minutes when they were asleep.

From there, answering these two parts involves traversing this data structure (and using counters).

# 2018/05: Alchemical Reduction

A polymer is a collection of characters, like `dabAcCaCBAcCcaDA`.
When the same letters are next to each other but of different case, they "react" and cancel, giving a shorter polymer. 

* Part 1: After fully reacting your given polynomial, how long is it? 
* Part 2: You are now allowed to remove all instances of one character (both upper and lower case) before fully reacting. What is the length of the shortest polymer you can produce when doing this?

This was a pretty easy string manipulation exercise.

# 2018/06: Chronal Coordinates (STUCK) 

How can you detect whether an area is infinite or not....

# 2018/07: The Sum of Its Parts

Resolving a dependancy graph..

# 2018/08: Memory Maneuver

Tree traversal / construction ..

# 2018/09: Marble Mania
# 2018/10: The Stars Align
# 2018/11: Chronal Charge
# 2018/12: Subterranean Sustainability
# 2018/13: Mine Cart Madness
# 2018/14: Chocolate Charts
# 2018/15: Beverage Bandits
# 2018/16: Chronal Classification
# 2018/17: Reservoir Research
# 2018/18: Settlers of The North Pole
# 2018/19: Go With The Flow
# 2018/20: A Regular Map
# 2018/21: Chronal Conversion
# 2018/22: Mode Maze
# 2018/23: Experimental Emergency Teleportation
# 2018/24: Immune System Simulator 20XX
# 2018/25: Four-Dimensional Adventure

----------------------

# 2017/01: Inverse Captcha
Given a long string of digits. Consider the string to be circular.
* Part 1: Calculate a checksum, that compares a character with the next.
* Part 2: Calcualte a checksum that compares a character with one halfway around the circular list.

Wraparound can be handled cleverly by using the right expression for indexing.

# 2017/02: Corruption Checksum
Given a spreadsheet of numbers

* Part 1: Calculate a checksum (for each row, max value - min value. Sum all these differences)
* Part 2: In each row, there are only two numbers where one evenly divides the other. Find these numbers, divide them, and sum up over all rows. 

Brute forced part 2. 

# 2017/03: Spiral Memory

Memory is stored in an infinite spiral grid:

```
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
```

* Part 1: Calculate Manhattan distance from your input number to `1`.
* Part 2: Allocate values into spiral grid by summing previous values that are adjacent. The grid starts off like this:
  ```
  147  142  133  122   59
  304    5    4    2   57
  330   10    1    1   54
  351   11   23   25   26
  362  747  806--->   ...
  ```
  Find the first value written that is larger than your input number.

I made the grid as a dictionary mapping coordinates (a string "x-val,y-val") to the value in the grid. 

Populating the grid requires traversal logic.


# 2017/04: High-Entropy Passphrases

* Part 1: Count how many passphrases don't have duplicate words
* Part 2: A passphrase is invalid if any of the words' letters can be rearranged to form any other word in the passphrase. Count the valid passphrases.

To check for duplicates, compare the length of the list of words with the size of the set.

For part 2, have to sort the letters of the word. Not too bad.

# 2017/05
# 2017/06
# 2017/07
# 2017/08
# 2017/09
# 2017/10: Knot Hash (STUCK)
  Something doesn't work in what I implemented. 
  I had to create a Circular List data structure which I think works..
  But somehow, I'm not getting the right result.

# 2017/11
# 2017/12
# 2017/13
# 2017/14
# 2017/15
# 2017/16
# 2017/17
# 2017/18
# 2017/19
# 2017/20
# 2017/21
# 2017/22
# 2017/23
# 2017/24
# 2017/25

-----

# 2016/01
# 2016/02
# 2016/03
# 2016/04
# 2016/05
# 2016/06
# 2016/07
# 2016/08
# 2016/09
# 2016/10
# 2016/11
# 2016/12
# 2016/13
# 2016/14
# 2016/15
# 2016/16
# 2016/17
# 2016/18
# 2016/19
# 2016/20
# 2016/21
# 2016/22
# 2016/23
# 2016/24
# 2016/25

-----

# 2015/01: Not Quite Lisp
Given a string consisting of characters `(` and `)`, such as `))(((((`. Treat `(` as incrementing by 1 and `)` as decrementing by 1. Start at position `0`.

* Part 1: Find the position you end up at after all changes.
* Part 2: Find how many steps it takes before you land on position `-1`.

Trivial.

# 2015/02: I Was Told There Would Be No Math

Given list of box dimensions like: 
```
20x3x11
15x27x5
6x29x7
30x15x9
19x29x21
10x4x15
1x26x4
1x5x18
10x15x23
10x14x20
3x5x18
```

* Part 1: Calculate amount of wrapping paper needed, using formula involving surface area and minimum side area.
* Part 2: Calculate amount of ribbon needed, using formula involving volume and minimum side perimeter.

Trivial.

# 2015/03: Perfectly Spherical Houses in a Vacuum

On a 2d rectangular grid. 
Given input like `>v^>^^^<>><v^<^^^<>v<<v<^v>>>^>>v^><<>vvv><^>>v><v><>v>>^>v><<><<>^<>^^^vv><v^>v^^>>^>^<^v<v<^^<^vvvv>v<v>^>v^>^><^<vvvv><^><><<v<>v<v^><^<v^>^v^^<<<<^><^^<^><>>^v<<^<<^vv>v>>v<^<^vv>><v<vv>v<v<v>^v<>^>v<>^v<<<v>>^^v>>><vvv>v^>^v^v>^^^v<vvvv>><^>vvv^<vv^^vv><<<>v<>v>^<vvv^<^<v<v<^vv^^>>vv^<^^v^><^^^^^v<^<v<^>>>vv^v^>^<v>^<><v^<^v>>><^v^<<v<<v<>v>^v<v^v>>^^v<<v<v<<>>>vv>>^v>>^<<<<^><<<><^^>>v<>^vvvv>v^^^>^^^>^<vvvv><^^v<v<>v<^v^v<<v^^^v^<v<^v>v^^<>^>^<^v>vv<v^vv<^<<>v><<^><><^^v<<><^^><>^v>^<><<^<^^<<>vv<>^^<<^>><<<>>vvv>^>v^^v^><<^>v>^>^<^<<>v<^>vv^v^v<>vv<<v>vv<vv><^>v^<>^vv^v^<v<^>>>>v^v><^<><<>vv^<vvv^>>vvv^>v>>><^^vv<vvvv>v`

which corresponds to instructions for traversing the grid.

* Part 1: Count how many positions get visited.
* Part 2: The instructions are alternated between two players. Count how many positions get visited.

Used sets of coordinates.

# 2015/04: The Ideal Stocking Stuffer

Given a "secret key" that is a short string.

* Part 1: Starting at 1, find the smallest number that needs to be appended to the secret key so that the resulting string, when MD5 hashed, will start with 5 zeros
* Part 2: Same, but for 6 zeros.

Trivial.

# 2015/05: Doesn't He Have Intern-Elves For This? (STUCK)

Given a list of strings of random alphabetic characters.

* Part 1: Strings are "nice" if they satisfy the three properties:
  * it contains >3 vowels
  * it has a letter appearing twice in a row
  * it does not have a given set of substrings

  The goal is to count the number of nice strings in the dataset.
* Part 2: The goal is the same, but "nice" strings are now those that satisfy both the properties:
  * contains a pair of two letters appearing twice without overlap
  * contains at least one letter that repeats with exactly one letter between them

Part 1 was easy. For part 2, I used regex.

# 2015/06: Probably a Fire Hazard

Given a list of instructions like:
```
turn off 70,873 through 798,923
toggle 258,985 through 663,998
turn on 601,259 through 831,486
turn off 914,94 through 941,102
turn off 558,161 through 994,647
turn on 119,662 through 760,838
toggle 378,775 through 526,852
turn off 384,670 through 674,972
turn off 249,41 through 270,936
turn on 614,742 through 769,780
```
where the "through" means it applies to the rectangular range determined by those two coordiantes.

* Part 1: Lights are binary. Count how many lights are lit. 
* Part 2: Lights are integer valued "brightness". Toggle increases by 2, turn on increaes by 1, turn off decreases by 1 (but does not go below zero). Calculate total brightness of all lights.

Used regex to extract useful values from instructions. Used defaultdicts for grids.

Created a function `rect_of_points` to create the list of coordinate points from the two endpoints given. Part 1 uses a counter. Part 2 uses `sum()`.

# 2015/07: Some Assembly Required
A circuit is expressed by input of the form:
```
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
```
* Part 1: Determine the value of wire `a`
* Part 2: Reset the circuit with wire `b` taking the answer from part 1. Determine the new value for wire `a`.

Used strings of 16 characters (`0` and `1`) to handle the required operations. Created utility methods (`bin_and`, `bin_or`, `bin_lshift`, `bin_rshift`, `bin_not`, `convert_to_binstr`) to manipulate these strings accordingly.
Looped over unused rules (assignments) until everything was determined.

For part 2, I put the loading code in a `load()` function and the executing code in an `execute()` function. That made the resetting and reloading for part 2 possible programmatically. 

# 2015/08: Matchsticks
Given data like:
```
"\\c\"jyufbry\"ryo\"xpo\x26ecninfeckh\\s"
"hdnpngtuc\"dzbvvosn\x31fwtpzbrt"
"hesbpd\xd4"
"dsdbstuzrdfmrnyntufs\"dmv"
"d\xeeibcwhcvkt"
"fvzwrsfjdqdmy\"\"v"
"ns\"dqafz\\lkyoflnazv\"mn\x37\"o\"yj\"e"
```

There are two lengths: the code representation and the in-memory length.
For example

|Input|Code representation|In-memory|
|---|:----:|:-----:|
|""|2|0|
|"\x27"|6|1|
|"a\\a"|6|3|

* Part 1: Count total difference between code representation length and the in-memory length.
* Part 2: Count total difference between reencoded length and the original length.

Both parts straightforward. For part 1, I carefully iterated to handle the escaped character sequences. For part 2, I counted *just* the number of added characters. 

# 2015/09: All in a Single Night
Given data about distances between cities:
```
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
```
A route consists of travelling to every location exactly once. 
Possible routes for this sample data are:
```
Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
```

* Part 1: Determine the distance of the shortest route.
* Part 2: Determine the distance of the longest route.

Quite easy. 
Created a dictionary of distances, with keys being pairs of cities. Doubled the keys by putting cities in both orders, to make lookup easier. 
Used `itertools.permutations` to make all possible trips.
Created a `trip_dist` function to process the tuple `permututations` returns.
Then the answers are just gotten by one-liners:
```python
min(trip_dist(perm) for perm in permutations(cities))
max(trip_dist(perm) for perm in permutations(cities))
```

# 2015/10: Elves Look, Elves Say
Given an input string consisting of characters `1`, `2`, `3`.
Iterate the look-and-say sequence on this string.

* Part 1: Compute the 40th iteration on the given input.
* Part 2: Compute the 50th iteration on the given input.

Straightforward. Implemented `look_and_say` by iterating over string carefully.
Calculating the 40 iterations takes about 2 seconds. 
Calculating an additional 10 iterations takes about 40 seconds.

# 2015/11: Corporate Policy
Given a starting password.
A valid password satisfies three conditions:
1) Increasing straight of 3 letters
2) Does not contain the characters `i`, `o`, `l`
3) Contains two non-overlapping pairs of letters

* Part 1: Find the next valid password from the starting password.
* Part 2: Find the next valid password after that.

Easy. Created boolean functions corresponding to each condition, one for returning whether the password is valid, and one for incrementing.

To do incrementing, I covert the string to a list of integer `ord` values using a one-liner `ords = list(map(ord, list(pw)))` and then increment with carry-over. Then covert back with `''.join(map(chr, ords))`

# 2015/12: JSAbacusFramework.io

Given a JSON document, which has arrays, objects, numbers, and strings. There will be *no* strings containing numbers.

* Part 1: Sum all the numbers in the document.
* Part 2: Find the sum, ignoring any objects (which are `{...}`, not `[...]`) that have a value of `"red"`.

Easy. Decoded the JSON using `json.loads` to make traversing easy/possible.
To sum everything, I created a `sum_all` method that recursively handles the structures depending on their type (`dict`, `list`, `int`, `str`).

To adjust for part 2, I introduced a field `part` to the `sum_all` function signature, using it to affect the recursion.

# 2015/13
# 2015/14
# 2015/15
# 2015/16
# 2015/17
# 2015/18
# 2015/19
# 2015/20
# 2015/21
# 2015/22
# 2015/23
# 2015/24
# 2015/25

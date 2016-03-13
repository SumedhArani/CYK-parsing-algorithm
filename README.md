# CYK-parsing-algorithm
->The program prompts the user to enter a file name. 
->The file will contain a grammar (assuming that the given grammar will be in Chomsky Normal Form).
->Then the program prompts the user to enter a string. It then outputs whether or not this string so entered belongs to the language of the grammar specified in the input file.

An example input file:
<ST> A <STB> <STC>  //all the non terminals
a b  //terminals
<ST> //start state

<ST> -> A<STB>
<ST> -> <STB><STC>
A -> <STB>A | a
<STB> -> <STC><STC> | b
<STC> -> A<STB> | a

Assumptions about the grammar file:
- Assuming that all non-terminals are in uppercase and all terminals are in lowercase.
- There can be multiple |'s (as shown above), or even none (such as for instance, S -> BA) for a given production. 
-There can be same non terminal appearing more than once in the LHS.

The CYK parsing algorithm has a running time complexity of O(n<sup>3</sup>)

It makes use of techiniques of dynamic programming or table filling method. the underlying concept here is that you make use of results already found in previous case to arrive at the result

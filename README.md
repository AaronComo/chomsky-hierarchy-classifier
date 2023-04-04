# Chomsky Hierarchy Classifier

## Description

Classify given grammar by Chomsky Hierarchy.



## Input format

~~~
grammar: G[N]
VN: N,D
rule1: N::=ND|D
rule2: D::=0|1|2|3
rule3: end
~~~

**Note:** Don't use space when typing.



## Output format

~~~
G[S]:   ({'B', 'E', 'S'}, {'a', 'e', 'b'}, P, S)
P:      S ::= aSBE|aBE 
        eE ::= ee
        aB ::= ab

Given grammar is a Chomsky-1 grammar.
~~~

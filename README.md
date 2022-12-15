# Jezeri, a slique language.
Jezeri is a simple Pascal-inspired programming language. It compiles directly to Python, and automatically runs `chmod` on the output file.
# Example
```
program Test
start main()
  print "Hello, World!"
finish
```
_`program` defines the name of the output file. Even if this file is named askjdas.jz Jezeri will output Test._
```
program MadLibs
start main()
  {: Multi-
  line-
  comment :}
  declare name=input()
  print "Wassup,{name}?"
finish
```
_All comments are multi-line comments._

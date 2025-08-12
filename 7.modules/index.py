import mymodule as md
md.greeting("Leandro")

from mymodule import greeting
greeting("Leleko")

from mymodule import greeting as gt
gt("Lelezura")

from mymodule import do_something as d_smt
d_smt()
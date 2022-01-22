# Module - a flie containing python code . may contain functions , classes , etc.
# used with modular programming , which is to seprate a program into parts .

import messages as m

m.hello()
m.bye()

from messages import hello,bye
hello()
bye()

from messages import *
hello()
bye()

help("modules")
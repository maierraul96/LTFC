from lexical_analyser.core.coreAnalyser import *
from lexical_analyser.printer import Printer
from lexical_analyser.afMeniu import Menu
from lexical_analyser.core.finiteAutomate import *
import unittest

# analyser = AnalyserCore("raza.lbc")
#
# analyser.run()
# analyser.show()
#
#
# Printer().show(analyser.CODTS, "FIP")
# print('\n')
# Printer().show(analyser.NAMES, "TS")


# unittest.main()

af = AF()
af.load_states_from_file("AF.json")
menu = Menu(af)
af.set_input("102.0")
menu.run()




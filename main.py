from lexical_analyser.core.coreAnalyser import *
from lexical_analyser.printer import Printer
from lexical_analyser.core.FiniteAutomate import *

# analyser = AnalyserCore("raza.lbc")
#
# analyser.run()
# analyser.show()
#
#
# Printer().show(analyser.CODTS, "FIP")
# print('\n')
# Printer().show(analyser.NAMES, "TS")

af = AF()
af.load_states_from_file("AF.json")
af.set_input("102.4.0")
print(af.digest())

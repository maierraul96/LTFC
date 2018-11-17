from lexical_analyser.core import *
from lexical_analyser.printer import Printer

analyser = AnalyserCore("raza.lbc")
analyser.run()
analyser.show()


Printer().show(analyser.CODTS, "FIP")
print('\n')
Printer().show(analyser.NAMES, "TS")

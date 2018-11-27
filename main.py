from finite_automate.ui.afMeniu import Menu
from lexical_analyser.IO.printer import Printer
from lexical_analyser.core.coreAnalyser import AnalyserCore

analyser = AnalyserCore("resources/source_codes/raza.lbc")

analyser.run()
analyser.show()


Printer().show(analyser.CODTS, "FIP")
print('\n')
Printer().show(analyser.NAMES, "TS")


# af = AF()
# af.load_states_from_file("zecimal.json")
# menu = Menu(af)
# af.set_input("102.0")
# menu.run()




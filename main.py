from finite_automate.ui.afMeniu import Menu
from finite_automate.core.finiteAutomate import *

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




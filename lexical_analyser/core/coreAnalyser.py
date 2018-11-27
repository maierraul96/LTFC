from finite_automate.core.finiteAutomate import AF
from lexical_analyser.IO.parser import Parser


class AnalyserCore:
    TERMS = {
        "NOTITA": 0,
        "ADHOC": 1,
        "~NOTITE~": 2,
        "~GATA_CU_NOTITELE~": 3,
        "NOTITA_NUMAR_INTREG": 4,
        "NOTITA_NUMAR_ZECIMAL": 5,
        "NOTITA_NUMAR_TEXT": 6,
        "INSIRUIRE": 7,
        "~MISIUNI_PENTRU_SOT~": 8,
        "~SOTIA_E_MANDRA~": 9,
        "devine": 10,
        "destainuie": 11,
        "(": 12,
        ")": 13,
        "+": 14,
        "-": 15,
        "*": 16,
        "/": 17,
        "noteaza": 18,
        "de_la": 19,
        "pe": 20,
        "CUNOSCATOR": 21,
        "no_daca": 22,
        "atunci": 23,
        "daca_nu": 24,
        "atata_timp_cat": 25,
        "onoreaza": 26,
        "atat": 27,
        "bine?": 28,
        "TEANC_DE": 29,
        "este": 30,
        "si": 31,
        "sau": 32,
        "ii_mai_mare_decat": 33,
        "ii_mai_mic_decat": 34,
        "GATA_CU_ONORAREA": 35,
        "nu_este": 36
    }

    CATEGORY = {"#": "NOTITA",
                "i": "ADHOC",
                "z": "ADHOC",
                "t": "ADHOC",
                "c": "CUNOSCATOR",
                "ids": "NOTITA",
                "zecimal": "ADHOC"
                }

    NAMES = {0: 100}
    CODTS = list()

    afs = dict()

    def __init__(self, path):
        self.parser = Parser(path)
        self.afs['ids'] = AF("resources\\af_definitions\ids.json")
        self.afs['zecimal'] = AF("resources\\af_definitions\zecimal.json")

    def run(self):
        elements = self.parser.get_elements()
        print(elements)
        for element in elements:

            if element in self.TERMS.keys():
                self.CODTS.append({self.TERMS[element]: -1})

            elif [af for af in self.afs.keys() if self.afs[af].verify(element)[0]]:
                if element not in self.NAMES.keys():
                    self.NAMES[element] = max(self.NAMES.values())+1

                category = [af for af in self.afs.keys() if self.afs[af].verify(element)[0]][0]
                self.CODTS.append({self.TERMS[self.CATEGORY[str(category)]]: self.NAMES[element]})

            elif element[0] in ["i", "t", "c"]:

                if element not in self.NAMES.keys():
                    self.NAMES[element] = max(self.NAMES.values())+1

                self.CODTS.append({self.TERMS[self.CATEGORY[element[0]]]: self.NAMES[element]})

            else:
                raise SyntaxError("Syntax error for " + element)

    def show(self):
        print(self.CODTS)

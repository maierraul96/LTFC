from lexical_analyser.IO.printer import *


class Menu:
    def __init__(self, af):
        self.af = af
        self.printer = Printer()

    def run(self):
        while True:
            print("(1) multimea starilor")
            print("(2) alfabetul")
            print("(3) tranzitiile")
            print("(4) multimea starilor finale")
            print("(5) verifica secventa")
            print()
            r = int(input("Optiune: "))
            options = [self.show_states,
                       self.show_alphabet,
                       self.show_trans,
                       self.show_final_states,
                       self.verify
                       ]
            options[r-1]()

    def show_states(self):
        self.printer.print_list("STATES", self.af.get_states_names())

    def show_trans(self):
        self.printer.print_list("TRANSITIONS", self.af.get_transitions())

    def show_alphabet(self):
        self.printer.print_list("ALPHABET", self.af.get_alphabet())

    def show_final_states(self):
        self.printer.print_list("TERMINAL STATES", self.af.get_final_states())

    def verify(self):
        seq = input("Secventa: ")
        self.af.set_input(seq)
        rez, msg = self.af.digest()

        print("SUCCESSFUL" if rez else "FAILURE")
        print(msg)
        print()
        print()

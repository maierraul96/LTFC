from copy import copy


class Printer:
    def show(self, table, title):

        if type(table) is dict:
            aux = copy(table)
            table = list()
            for key in aux.keys():
                table.append({key: aux[key]})

        max_len_value = max([len(str(list(values.values())[0])) for values in table])
        max_len_key = max([len(str(list(keys.keys())[0])) for keys in table])

        print(title)
        print('-' * (max_len_key + max_len_value + 8))
        form = '|' + '{:^' + str(max_len_key+2) + '}|' + '{:^' + str(max_len_value+2) + '}|'
        for row in table:
            print(form.format(list(row.keys())[0], list(row.values())[0]))
        print('-' * (max_len_key + max_len_value + 8))

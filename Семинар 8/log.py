import model as m


def log_it():
    with open('log.csv', 'a', encoding='UTF-8') as logfile:
        logfile.write(f'{m.surname}; {m.name}; {m.phone}; {m.comment} \n')
        
def import_file():
    with open('import.csv', 'r', encoding='UTF-8') as logfile:
        string = logfile.read()
        string = "".join([i for i in string if i != ";"])
        m.init(string)
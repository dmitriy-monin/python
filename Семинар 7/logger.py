from datetime import datetime as dt

def log_add(a, b, z, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time};{a}{z}{b}={result}\n')
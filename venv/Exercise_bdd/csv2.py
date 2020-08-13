import csv

with open('/home/clement/PycharmProjects/pythonProject1/venv/Exercise_bdd/exercice python/reg2016.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('/home/clement/PycharmProjects/pythonProject1/venv/Exercise_bdd/exercice python/reg2016.txt', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow('')
        writer.writerows(lines)
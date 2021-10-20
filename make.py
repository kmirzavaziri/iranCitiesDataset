import argparse
import csv

CSV_FILE = "iranAdministrativeDivision.csv"
SQL_FILE = "iranAdministrativeDivision.sql"

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('table', type=str)

args = parser.parse_args()
table = args.table


def readCsv():
    with open(CSV_FILE, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for raw in csvreader:
            row = {}
            for i in range(len(header)):
                row[header[i]] = raw[i]
            yield row


with open(SQL_FILE, 'w') as f:
    f.write("SET NAMES 'utf8mb4' COLLATE 'utf8mb4_persian_ci';\n")
    f.write(f"TRUNCATE TABLE {table};\n")
    for row in readCsv():
        if not row['parent']:
            row['parent'] = 'null'
        f.write(f"INSERT INTO {table}(`id`, `title`, `type`, `parent`) " +
                f"VALUES({row['id']}, '{row['title']}', '{row['type']}', {row['parent']});\n")

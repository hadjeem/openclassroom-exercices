import csv
# Écrivez votre code ici !

def extract():
    data = []
    with open("input.csv") as file:
        reader = csv.DictReader(file, delimiter=",")
        for line in reader:
            data.append(line)
    return data

def transform(data):
    data_to_load = []
    for line in data:
        transformed_data = {}
        transformed_data["nom"] = line["nom"]
        transformed_data["salaire"] = int(line["heures_travaillees"]) * 15
        data_to_load.append(transformed_data)
    return data_to_load    

def load(data):
    with open("output.csv", "w", newline="") as file:
        fieldnames = ["nom", "salaire"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerow(line)

def main():
    data = extract()
    data_to_load = transform(data)
    load(data_to_load)



# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
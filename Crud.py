import csv

# Função para criar um novo registro
def create_record(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Função para ler todos os registros
def read_records():
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Função para atualizar um registro pelo índice
def update_record(index, new_data):
    records = []
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)

    if 0 <= index < len(records):
        records[index] = new_data
        with open('data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)

# Função para excluir um registro pelo índice
def delete_record(index):
    records = []
    with open('data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)

    if 0 <= index < len(records):
        del records[index]
        with open('data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)

# Menu para interagir com o usuário
while True:
    print("\nMenu:")
    print("1. Adicionar Registro")
    print("2. Ler Registros")
    print("3. Atualizar Registro")
    print("4. Excluir Registro")
    print("5. Sair")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        data = input("Digite os dados do registro (separados por vírgula): ")
        create_record(data.split(','))
    elif choice == '2':
        print("Registros:")
        read_records()
    elif choice == '3':
        index = int(input("Digite o índice do registro que deseja atualizar: "))
        new_data = input("Digite os novos dados do registro (separados por vírgula): ")
        update_record(index, new_data.split(','))
    elif choice == '4':
        index = int(input("Digite o índice do registro que deseja excluir: "))
        delete_record(index)
    elif choice == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")

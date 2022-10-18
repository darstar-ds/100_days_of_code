from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electrix", "Water", "Fire"])
table.align["Pokemon name"] = "l"
table.align["Type"] = "r"
print(table)
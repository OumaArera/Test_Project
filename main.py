from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Student Name",["James Ochuodho", "Brian Katembo", "John Ouma", "Antony Opiyo"])
table.add_column("Class", ["Form 4G", "Form 4B", "Form 4Y", "Form 4R"])
print(table)
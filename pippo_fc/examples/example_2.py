from pippo_fc import pippo_fc

while True:
	surname = str(input("\ninsert your surname: "))
	name = str(input("insert your name: "))
	sex = str(input("insert your sex (M - F): "))
	birthdate = str(input("insert your birthdate (DD/MM/YYYY): "))
	birthplace = str(input("insert your birthplace: "))

	result = pippo_fc.encode(surname=surname, name=name, sex=sex, birthdate=birthdate, birthplace=birthplace)
	print("\n" + result)
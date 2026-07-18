from pathlib import Path

num = int(input())
def get_to_do_list():

	while True:

		to_do_list = []

		for i in range(0,num):
			to_do = input("Enter what you need to do : ")
			to_do_list.append(to_do)
		for list in to_do_list:
			print(list)
		answer = input("Is it right? [y/n] : ")

		if answer == "y":
			return to_do_list
		else:
			continue


final_to_do_list = get_to_do_list()
print("Your To-Do_List : " , final_to_do_list)

format_todo = "\n".join(final_to_do_list)

file_path = Path("./.todo.txt")
file_path.write_text(format_todo, encoding="utf-8")

first_string = "Hello"
second_string = "my"
third_string = "name "
fourth_string = "is"
fifth_string = "keval"

full_string = [first_string, second_string, third_string, fourth_string, fifth_string]

new_file = open("C:/Users/admin/Desktop/TextDocument1.txt", 'w')
new_file.write(full_string)
new_file.close()

#write() only accepts string whereas
#writelines() accpets list also.
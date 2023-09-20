my_file = open("file_projects/data.txt","r")

file_content = my_file.read()

my_file.close()

print(file_content, '\n')

user_name = input('Enter your name: ')

my_file_writing = open("file_projects/data.txt","w")
my_file_writing.write(user_name)

my_file_writing.close()
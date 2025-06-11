#test.py
# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file

from functions.run_python import run_python_file

# result0 = get_files_info("calculator", ".")
# print(result0)


# result1 = get_files_info("calculator", "pkg")
# print(result1)

# result2 = get_files_info("calculator", "/bin")
# print(result2)

# result3 = get_files_info("calculator", "../")
# print(result3)

# result4 = get_file_content("calculator", "main.py")
# print(result4)
# result5 = get_file_content("calculator","pkg/calculator.py")
# print(result5)
# result6 = get_file_content("calculator", "/bin/cat")
# print(result6)
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
result7=run_python_file("calculator", "main.py")
print(result7)
result8= run_python_file("calculator", "tests.py")
print(result8)
result9= run_python_file("calculator", "../main.py")
print(result9)
result10= run_python_file("calculator", "nonexistent.py")
print(result10)

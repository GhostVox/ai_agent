#test.py
from functions.get_files_info import get_files_info

result0 = get_files_info("calculator", ".")
print(result0)


result1 = get_files_info("calculator", "pkg")
print(result1)

result2 = get_files_info("calculator", "/bin")
print(result2)

result3 = get_files_info("calculator", "../")
print(result3)

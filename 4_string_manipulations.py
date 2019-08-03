str1 = "Pradeep works in Sony"

print(f"str is \"{str1}\"... yes.")

print(f"upper: {str1.upper()}")
print(f"lower: {str1.lower()}")
print(f"title: {str1.title()}")
print(str1)

str1 = str1.upper()
print(str1)

print("Sony" in str1)  # false. as SONY is available but not Sony
print("sony" in str1.lower())  # true

str1 = "oracle"
print(f"len of str1: {len(str1)}")
print(f"first 3 chars[1:3]: {str1[1:3]}")  # slicing
print(f"chars[:3] {str1[:3]}")  # ora
print(f"chars[2:] {str1[2:]}")
print(f"reverse: {str1[::-1]}")

str1 = "Pradeep works at Sony"
print(str1.split(" "))

# startswith
# endswith
# regex

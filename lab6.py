import hashlib

def calculate_hash(file_path, hash_function):
    with open(file_path, "lab3") as file:
        file_data = file.read()
        hash_object = hash_function(file_data)
        return hash_object.hexdigest()
    
#file paths
file1 = ""
file2 = ""

# calculate md5 and sha-1 for both files 
md5_file1 = calculate_hash(file1, hashlib.md5)
md5_file2 = calculate_hash(file2, hashlib.md5)

sha1_file1 = calculate_hash(file1, hashlib.sha1)
sha1_file2 = calculate_hash(file2, hashlib.sha1)

# print the results
print(f"md5 of {file1}: {md5_file1}")
print(f"md5 of {file2}: {md5_file2}")
print(f"sha-1 of {file1}: {sha1_file1}")
print(f"sha-1 of {file2}: {sha1_file2}")

# check of collisons 
if md5_file1 == md5_file2:
    print("MD5 collison detected!")
else:
    print("No md5 collion.")


if sha1_file1 == sha1_file2:
    print("SHA-1 collison detected!")
else:
    print("No SHA-1 collion.")

class PasswordTest:
    """a password and the rules it must follow"""

    def __init__(self, password, req_char, min_count, max_count):
        """iinitialize the password/rule combo"""
        self.password = password
        self.req_char = req_char
        self.min_count = min_count
        self.max_count = max_count
    
    def is_valid(self):
        """test if the user's password follows its prescribed rules"""
        req_char_count = 0
        for char in self.password:
            if char == self.req_char:
                req_char_count += 1
        
        if req_char_count >= self.min_count and req_char_count <= self.max_count:
            return True
        else:
            return False
    
    def pw_char_list(self):
        """converts the password into a list of individual characters"""
        char_list = []
        for char in self.password:
            char_list.append(char)
        return char_list

passwords = []

with open('input.txt') as input_file:
    for line in input_file:
        stripped = line.rstrip()
        passwords.append(stripped.split(' '))
        

for password in passwords:
    min_max = password.pop(0).split('-')
    password.insert(0, min_max[0])
    password.insert(1, min_max[1])

for password in passwords:
    test_char = password.pop(2)
    password.insert(2, test_char.rstrip(':'))

# create a PasswordTest instance for each item in passwords:
password_tests = []
valid_passwords = []

for password in passwords:
    new_password_test_instance = PasswordTest(password[3], password[2], int(password[0]), int(password[1]))
    password_tests.append(new_password_test_instance)
    test = new_password_test_instance.is_valid()
    
    if test:
        valid_passwords.append(new_password_test_instance)

#print(f"we tested {len(password_tests)} passwords, and {len(valid_passwords)} were valid")

password_tests_2 = []
valid_passwords_2 = []

for pw_test in password_tests:
    
    #this variable holds the password as a list of characters
    pw_chars = pw_test.pw_char_list()
    
    test_char_1 = pw_chars[pw_test.min_count - 1]
    test_char_2 = pw_chars[pw_test.max_count - 1]

    char_count = 0
    if test_char_1 == pw_test.req_char:
        char_count += 1
    if test_char_2 == pw_test.req_char:
        char_count += 1
    
    if char_count == 1:
        valid_passwords_2.append(pw_test)
    
    password_tests_2.append(pw_test)


print(f"Based on the requirements in part 2, we again tested all {len(password_tests_2)} " \
    f"passwords and {len(valid_passwords_2)} were valid.")
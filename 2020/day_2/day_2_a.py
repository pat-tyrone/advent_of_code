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

print(f"we tested {len(password_tests)} passwords, and {len(valid_passwords)} were valid")



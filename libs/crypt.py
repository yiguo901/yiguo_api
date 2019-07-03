import hashlib


def make_password(passwd_str):
    return hashlib.md5(("9@^"+passwd_str+'$&').encode()).hexdigest()


def check_password(passwd_str, encrypted_str):
    print(passwd_str,encrypted_str,"密码门密码")
    return make_password(passwd_str) == encrypted_str

if __name__ == '__main__':
    mima = make_password("f458beff31e5079faad2b1a64071aad4")
    print(mima)
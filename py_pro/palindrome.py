# This is an program for demonstrate what's mypy function do

def is_palindrome(string: str) -> bool:
    string = string.replace(' ','').lower()
    return string == string[::-1]

def run():
    print(is_palindrome('ana'))
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()
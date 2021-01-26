import os

def main():
    username = os.environ.get('ACTION_USERNAME')
    password = os.environ.get('ACTION_AUTHKEY')
    print(username + password)

if __name__ == '__main__':
    main()


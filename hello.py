import os
from pathlib import Path

def main():
    Test_DIR = Path(__file__).parent
    Test2_DIR = Test_DIR / "dir"
    # print(type(Test2_DIR))
    Test2_DIR.mkdir(exist_ok=True)

    with open('test.txt', 'w') as file:
        file.write('hello uv\n')

    test2_file = Test2_DIR / "test2.txt"
    # print(type(test2_file))
    with test2_file.open(mode='w') as file:
        file.write('uv is good tool!\n')
        

    print("Hello from test-python!")


if __name__ == "__main__":
    main()

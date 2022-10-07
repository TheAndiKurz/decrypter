import sys
from functions import decrypt_file


def process_args(args: list[str]) -> dict[str, str]:
    options = {
        "filepath": args[0]
    }

    for i, arg in enumerate(args[1:]):
        if arg == "-p" or arg == "--password":
            if "password" not in options:
                if i + 2 >= len(args):
                    print("-p | --password usage: --password <password>",
                          file=sys.stderr)
                else:
                    options["password"] = args[i+2]

    return options


def get_password():
    return input("With what password do you want to encrypt the file? ")


def main(argv: list[str]):
    if len(argv) < 2:
        print(f"usage: python {argv[0]} <filepath> [options]", file=sys.stderr)
        return

    options = process_args(argv[1:])

    filepath = options["filepath"]

    password = options.get("password")

    if password == None:
        password = get_password()

    print(f"encrypting {filepath} with password {password}")

    decrypt_file(filepath, password)


if __name__ == "__main__":
    argv = sys.argv
    main(argv)

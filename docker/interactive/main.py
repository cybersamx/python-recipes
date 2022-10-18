from faker import Faker


def main():
    Faker.seed()
    faker = Faker()

    try:
        msg = input("Hello %s! Is this your name? (ctrl-d to exit) " % faker.name())
        print(msg)
        while True:
            msg = input('Say something? (ctrl-d to exit) ')
            print(msg)
    except (EOFError, KeyboardInterrupt):
        print('exiting...')


if __name__ == '__main__':
    main()

import click

@click.command()
#basic options
@click.option('--name', '-n',  default = 'John', help = 'Firstname is Description')

def main(name):
    print('My name is {}'.format(name))

if __name__ == "__main__":
    main()
import click


@click.group
def mycommands():
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")

def hello(name):
    click.echo(f"Hello {name}!")

PRIORITIES = {
    "o": "OPTIONAL",
    "l": "LOW",
    "m": "MEDIUM",
    "h": "HIGH"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the todo's name", help="The todo item's name")
@click.option("-d", "--desc", prompt="Describe the todo", help="The todo item's description")
def add_todo(name, desc, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]\n")

@click.command()
@click.argument("idx", type=int, required=1)
@click.argument("todofile", type=click.Path(exists=True), required=0)
def delete_todo(idx, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open(filename, "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(todofile, priority):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"{idx}:{todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"{idx}:{todo}")


mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__ == "__main__":
    mycommands()
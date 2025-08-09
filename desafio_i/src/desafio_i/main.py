import sys
from .handlers.handle_del import handle_remove
from .handlers.handle_add import handle_append
from .handlers.handle_list import handle_listing


help_message = """
Usage:
    
    $ <python> src/desafio_i/main.py [add,del] <json path>

Args:

    add     add a person to the list
    del     removes a person from the list
    list    prints the list of registred users
"""


## Starting point.
def main():
    if len(sys.argv) < 3:
        print(help_message)

        # Returns safely if there is no args or json path.
        return

    json_path = sys.argv[2]

    match sys.argv[1]:
        case "del":
            handle_remove(json_path)
        case "add":
            handle_append(json_path)
        case "list":
            handle_listing(json_path)
        case _:
            print(help_message)


# Starting execution 
if __name__ == "__main__":
    main()

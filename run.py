container = {
    'dim': None,
    'in' : []
}
list_of_content_box = []

def print_box():

    """
    Print the box
    """
    width = 4
    height = 2
    thickness = 2

def get_input(text):

    """
    Get input
    """

    return tuple(map(int, input(text).split(',')))

def container_prompt():

    """
    Get dimensions for a container box
    """

    input = get_input("What are dimensions of the container box?\r\n")
    h, w, z = input
    for l in range(h):
        if l == 0:
            print(".." * w)
        print("." + "  " * (w-1)+ ".")
        if l == len(range(h)) - 1:
            print(".." * w)

    container['dim'] = input
    return input

def content_prompt():

    """
    Get dimensions for a content box
    """

    input = get_input("What are dimensions of the content box?\r\n")
    return validate_size(input)


def menu_prompt():

    """
    Get choice from displayed menu
    """

    return input("""Choices :
    0 - Add container box dimensions
    1 - Add box in the container box
    2 - Display container with boxes inside
    3 - Quit the program\r\n""")

def validate_size(content_dim):

    """
    Validate box size in a box container
    Returns True if ok else False
    """

    for index, elem in enumerate(content_dim):
        if container is not None and int(container['dim'][index]) < elem:
            return False
    return content_dim


def calc_available_space(content, container):

    """
    Calc available space
    """

    cubic_meter = container['dim'][0] * container['dim'][1] * container['dim'][2]
    sum = 0

    for c in container['in']:
        sum += c['dim'][0] * c['dim'][1] * c['dim'][2]

    new_surface =  content['dim'][0] * content['dim'][1] * content['dim'][2]
    sum += new_surface
    available_space = cubic_meter - sum

    return available_space

def add_box_into_container(content_dim, container):

    """
    Add box into container
    """

    res = calc_available_space(content_dim, container)
    if res >= 0:
        container['in'].append(content_dim)
    else:
        raise Exception("Out of the box")

def main():

    """
    Contain the main program
    """
    choice = None

    while choice != '3' or choice is None:

        choice = menu_prompt()

        if choice == '0':
            print("<<< Add container box dimensions >>>")
            # Save container sizes
            container_dim = container_prompt()
        elif choice == '1':
            # Save content block sizes
            box = content_prompt()
            add_box_into_container(box, container)
        elif choice == '2':
            # Display container
            print_box()
            print(container)
        else:
            print("Bye bye")


if __name__ == "__main__":
    main()
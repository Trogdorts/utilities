def kvprint(data, indent=0, print_types=False):
    # Helper function to add indentation
    def add_indentation(indent):
        return "    " * indent

    # If data is a dictionary
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{add_indentation(indent)}{key}:")
                kvprint(value, indent + 1, print_types)
            else:
                value_str = f"{value}"
                if print_types:
                    value_str += f" ({type(value).__name__})"
                print(f"{add_indentation(indent)}{key}: {value_str}")
    # If data is a list
    elif isinstance(data, list):
        for index, value in enumerate(data):
            if isinstance(value, (dict, list)):
                print(f"{add_indentation(indent)}[{index}]:")
                kvprint(value, indent + 1, print_types)
            else:
                value_str = f"{value}"
                if print_types:
                    value_str += f" ({type(value).__name__})"
                print(f"{add_indentation(indent)}[{index}]: {value_str}")
    else:
        data_str = f"{data}"
        if print_types:
            data_str += f" ({type(data).__name__})"
        print(f"{add_indentation(indent)}{data_str}")

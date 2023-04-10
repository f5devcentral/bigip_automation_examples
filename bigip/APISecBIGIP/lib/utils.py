import json


def replace_conf_file(filepath, data_old, data_replaced):
    """Replace content of a file."""
    f = open(filepath, 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(data_old, data_replaced)
    f = open(filepath, 'w')
    f.write(newdata)
    f.close()


def update_json_file(filepath, file_key, new_value):
    """Update contents of a json file by key."""
    f = open(filepath, 'r')

    # returns JSON object as a dictionary
    data = json.load(f)

    # updating value
    data[file_key] = new_value

    # Closing files
    f.close()

    with open(filepath, "w") as outfile:
        json.dump(data, outfile)

def get_node_by_class(tree, class_name, parent_key=None):
    if isinstance(tree, dict):
        if 'class' in tree and tree['class'] == class_name:
            return parent_key
        for key, value in tree.items():
            rValue = get_node_by_class(value, class_name, key)
            if rValue:
                return rValue
    elif isinstance(tree, list):
        for item in tree:
            rValue = get_node_by_class(item, class_name, parent_key)
            if rValue:
                return rValue
    return None

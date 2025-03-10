def search(name, base, prop=None):
    """Name - what we're finding,
    prop - in what property we're finding,
    Base - where are we finding (like products list),"""
    global results, indices_of_results
    if prop is None:
        results = [fd for fd in base if fd.name == name]
        indices_of_results = [i for i, fd in enumerate(base) if fd.name == name]
    elif prop == 'surname':
        results = [fd for fd in base if fd.surname == name]
        indices_of_results = [i for i, fd in enumerate(base) if fd.surname == name]

    return results, indices_of_results

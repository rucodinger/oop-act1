def search(name, base):
    """Name - what we're finding,
    prop - in what property we're finding,
    Base - where are we finding (like products list),"""
    results = [fd for fd in base if fd.name == name]
    indices_of_results = [i for i, fd in enumerate(base) if fd.name == name]
    return results, indices_of_results
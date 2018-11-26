import pdb
def distinct(iterable):
    """Return unique items by eliminating duplicates.
    Args:
        iterable: The source of the items.
    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
#    import pdb; pdb.set_trace()
    for item in distinct(items):
        print(item)

run_distinct()

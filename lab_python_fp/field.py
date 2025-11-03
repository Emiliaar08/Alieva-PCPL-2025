def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] != None:
                yield item[key]
    else:
        for item in items:
            new = {key: item[key] for key in args if key in item and item[key] != None}
            if new:
                yield new
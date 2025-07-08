def api(traffic, *args, **kwargs):
    print(traffic)

    for item in args:
        print(item)

    print(type(args))

    for key, value in kwargs.items():
        print(f"key is: {key} of value {value}")
    print(type(kwargs))

api(5, "title", "description", isAvailable=True, quantity=30)
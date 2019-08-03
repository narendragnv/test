def italic(message):
    return f"<i>{message}</i>"

def bold(message):
    return f"<b>{message}</b>"

m = italic(bold("world"))
print(m)

###################################################

def italic_dec(func):
    def wrapper(message):
        return f"<i>{func(message)}</i>"

    return wrapper

@italic_dec
def normal(message):
    return f"<n>{message}</n>"

m2 = normal("world")
print(m2)

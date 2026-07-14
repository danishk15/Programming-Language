import basic

while True:
    text = input('Quilhawk >')
    result,error = basic.run('<stdin>',  text)

    if error:print(error.as_string())
    elif result is not None:print(result)
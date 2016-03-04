spoken = lambda greeting: greeting + '.'
shouted = lambda greeting: greeting.upper() + '!'
whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)


if __name__=='__main__':
    print(greet(spoken, "Hello"))
    print(greet(shouted, "Hello"))
    print(greet(whispered, "Hello"))

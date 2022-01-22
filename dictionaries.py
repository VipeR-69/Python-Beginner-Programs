# dictionary = a changeable , unorderd collection of unique key:value pairs .
#              fast becz they use hashing , allow us to access a value quickly .

capitals = {'India':'New Delhi',
            'USA':'WashingtonDC',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()

print(capitals['Russia'])
print(capitals.get('France'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)
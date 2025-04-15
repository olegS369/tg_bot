import random
r_h2 = 0

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def r_h(a, b):
    global r_h2
    r_h2 = random.randint(a, b)
    return r_h2

def decomposition(material):
    srok_razl = {
        "пластик": '500 лет',
        'стекло': '1000000 лет',
        'дерево': '3 - 10 лет',
        'батарейки': '2млн лет+',
        'алюминевые банки': '200 лет'
    }
    #for i in range(len(srok_razl)):
    for key in srok_razl.keys():
        if key == material:
            return srok_razl[key]
        else:
            return 'к сажелению здесь такого материала нет:('
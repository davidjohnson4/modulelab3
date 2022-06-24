def main():
    my_info = {
        'name': 'David Johnson',
        'student_id': '10209057',
        'toppings' : [
            'pepperoni',
            'peppers',
            'bacon',
        ],
        'movies': [
            {'title': 'Endgame',
            'genre': 'Action'},
            {'title': 'Transformers',
            'genre': 'Sci-Fi'
            }
        ]
    }
    new_toppings = ('olives', 'chesse')
    add_toppings(my_info, new_toppings)
    top = my_info['toppings']
    top.sort()
    
    full_name = 'Hi Joe, my name is ' + my_info['name'] + ' and my student ID is ' + my_info['student_id']
    
    print(full_name)
    print('My ideal pizza has ',top)
    print_genre(my_info)
    print_title(my_info)


def print_genre(my_info):
    sentence3 = 'I like to watch ' 
    for g in my_info['movies']:
        
        sentence3 += g['genre'] + ', '
        
    
    print(sentence3[:-2])

def print_title(my_info):
    sentence4 = 'Some of my favourite movies are '
    for m in my_info['movies']:
        sentence4 += m['title'] + ', '
    print(sentence4[:-2])


def add_toppings(my_info, new_toppings):
    for t in new_toppings:
        my_info['toppings'].append(t)
   

main()
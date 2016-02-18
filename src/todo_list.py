
from __future__ import print_function 
import datetime
import time

class TodoItem:
    def __init__(self, item, description=''):
        self.__item = item
        self.__date_added = datetime.datetime.now()
        self.__description = '{}'.format(description)

    def __str__(self):
        return '{}: {} {}'.format(self.__date_added, self.__item, '- '+self.__description if self.__description else '')

class TodoList(object):
    def __init__(self, *args):
        self.__items = [TodoItem('{}'.format(i)) for i in args]
    
    def size(self):
        return len(self.__items)
        
    def __str__(self):
        return '\n'.join(['{}'.format(i) for i in self.__items])
    
    def __getattr__(self,attr):
        print('here')
        return 'foo'

    def add_todo_item(self, item, desc = ''):
        self.__items.append(TodoItem(item, desc))

def get_input_from_user():
    stop = False

    while not stop:
        todo_item = input("Enter a todo list item: ")
        desc = ''

        for d in (':', '-'):
            if d in todo_item:
                todo_details = [ i.strip() for i in todo_item.split(d)]
                todo_item, desc = todo_details[0], d.join(todo_details[1:])
                break
        
        obj.add_todo_item(todo_item, desc)
        print(obj)

        cont = input("Do you still want to continue? ")

        if cont.lower() == 'n':
            stop = True

if __name__ == "__main__":
    workout = 'workout'
    lunch = 'Eat lunch'
    obj = TodoList('Study programming', 'check emails', lunch)

    '''
    
    print(obj)
    print(obj.size())
    
    obj.foo = 'bar'
    print(obj.foo)
    '''

    get_input_from_user()

    obj.add_todo_item(workout)
    obj.add_todo_item('Study Hangeul')

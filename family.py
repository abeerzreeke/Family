
class Family():
    
    def __init__(self, members, last_name):
        self.members = [
            {'name':'Michael',
            'age':35,
            'gender':'Male',
            'is_child':False},
            {'name':'Sarah',
            'age':32,
            'gender':'Female',
            'is_child':False} 
            ]
        self.last_name = last_name
    
    def born(self, **new_born):
        self.new_born = new_born
        self.members.append(new_born)
        return 'congratulation you add a new born'
    
    def is_18(self, name_born):
        self.name_born = name_born
        borns = self.members
        one_born = 0
        total_borns = len(borns)

        while one_born < total_borns:
            if borns[one_born]['name'] == name_born:
                if (borns[one_born]['age'] > 18):
                    return True
                return False
            one_born +=1
     
if __name__ == '__main__':

    my_family = Family('Meme', 'zreeke')
    print(my_family.born(name = 'Meme',age = 2, gender = 'Female', is_child = False))
    print(my_family.is_18('Meme'))


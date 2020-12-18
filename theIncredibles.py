from family import Family

class TheIncredibles(Family):

    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self):
        borns = self.members
        one_born = 0
        total_borns = len(borns)
        print(total_borns)
        while one_born < total_borns:
            if (borns[one_born]['age'] > 18):
                if 'power' in borns[one_born]:
                    print('the power of {} is {} ' .format(borns[one_born]['name'],borns[one_born]['power']))
                    one_born +=1
                else:
                    print('{} You have no power here !!' .format(borns[one_born]['name']))
                    one_born +=1 
            else:
                print('check how !!')
                one_born +=1

    def incredible_presentation(self):
        borns = self.members
        one_born = 0
        total_borns = len(borns)
        print(total_borns)
        while one_born < total_borns:          
            if 'power' in borns[one_born]:
                print('the power of {} is {} ' .format(borns[one_born]['name'],borns[one_born]['power']))
                one_born +=1
            else:
                one_born +=1

                



        
if __name__ == '__main__':
    
    my_family = TheIncredibles('Mrmr', 'zreeke')
    my_family.born(name = 'Mrmr',age = 22, gender = 'Female', is_child = False, power = 'full',incredible_name = 'lala' )
    my_family.born(name = 'lulu',age = 32, gender = 'Female', is_child = False, power = 'medeum',incredible_name = 'jad' )
    my_family.incredible_presentation()
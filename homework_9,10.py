#9

str1 = 'alerksey_yudin_olegovisch'
lst = str1.split('_')
print(str1, '->', (lst[0].title() + lst[1].title() + lst[2].title()))

#10

str2 = 'Artur Pirojkov*1944-08-28*2010-11-20'
lst1 = str2.split('*')
name = lst1[0]
lst2 = lst1[1]
lst3 = lst2.split('-')
lst4 = lst1[2]
lst5 = lst4.split('-')
year_of_life = ((int(lst5[0])) - (int(lst3[0])))
print(name, year_of_life)

"""print ("Ну здарвствуй, лысина")
print (2+2)
print (4*2)
print (5//2)
print(2/3)
print (5%2)"""
"""int=1# целые числа
type_float=1.23 # числа  с точкой
type_str= "сттроки пишутся в ковыччках"
type_bool_one= True  # булевы значения истина (правда)
type_bool_two = False #булевы значения ложь
type_none = None#  пустышка например для проверки или выполнение функци при перемонной пустоты
"""
"""x=5
y=123
print(x*2)
print(x*3)
print(x*4)
print(x*5)
print(x*7)
print(x*8)
print(x*9)
print(x*6)
print(x*y)*/
"""
"""a=1233
print (a * 2, type(a))
a=str(a)
print (a)
a=float(a)
print (a,type(a)) """
"""c = int(input ("введите число - мы емножим его на 2: ")) # инпут по умолчанию строчный
c=int(c)# таким образом меняю тип данных которые вуодит пользщователь на численные и их уже можно перемножать делить и тд
print (c*2)
"""
"""
print("Заполните красткую информациб о себе")
name=input("введите имя")
print(name)
age=input("Укажите свой возраст")
age=str(age)
f=input("расскажите о вашем хоби")
print ('уважаемый пользователь мы выяснили как вас зовут и сколько вам лет а так же ваше хоби' )
ask=input('Расскажите чем мы можем вам помочь? возможно  рассказать что мы выяснили? если это так то введите da')
print (name,age,ask,f)"""

"""19 Мая Комбинации IF. Else. Elif.
if отвеает на 2 вопроса правда и не правда
if a<b  - ситнаксиси, условие в конце свтаим двоеточие тогда питон ждет ответа обязательно писать с новой строчки но не сс самого начала например таб или проблем
OR c командой Ор "ИЛИ" достаточно сработать 1 из условий 
AND срабатывает токльо если сработали все условия, не как ОР, код пойдет только в случае выполнения всех задач
Скобки работают как в математике
if (a<b or  b<11) and a == 5 для срабатывания должно быть и одно из  значений вскобках и обязательное после скобок
== двойное равно это СРАВНИвание, не уточнение, вопрос!!!!!
else - ЕСЛИ ИНАЧЕ Эта Команда железно должна быть всегда после команды ИФ Элзе будет работаьтьтолько еслин е сработал иф
Elif(Elseif) (ИНАЧЕ ЕСЛИ) он  нужен только при вариации дествий  если не сраббатывает проверка на иф то идет проверка на элиф а , элзе сработает всегда и на крайняк выдаст что то вроде "ОШИБКА ДАННЫХ"
IF u ELSE КОТОРые относятся друг к  другу должны писаться в ОДНУ ЛИНИ ОЧЕНЬ ВАЖНО!!!!!!!
И в ифе и в жльзе можно создавать новые переменные например вызвать сообщение поддержки
"""
"""
a=5
b=10
if (a<b or  b<11) and a == 5: # сработает только если тру тоесть правда и кол выполнится если не правда код не сработает
    print("if comleted")
else:
    print ("else выполняется")"""
"""
login=input("Ведите логин")
password=input("Ввеите пароль")
if login=="admin"and  password=="admin":
     print("Вход выполнен")
else:
    print("Не верный логин или пароль: 1этап")
"""
# 5вопрос есслди польщзователь набирает 3 очка спросить хочет ли он отвечать на доп вопрос если отвечает да или ес то задаем иначе завершаем игру и выдаем очки
"""
q1=input("Зимой и летом одним цветом")
score=0
if q1== "елка"or q1=="ёлка":
    print("Congratulation")
    score= score + 1
else:
    print("Lose")
    score= score - 1
q2=input("2+2=4?")
if q2=="4" or q2=="да":
    print("Congratulation")
    score= score + 1
else:
    print("Lose")
    score= score - 1
q3=input("что  наступает после лета")
if q3=="осень":
    print("Congratulation")
    score= score + 1
else:
    print("Lose")
    score= score - 1
q4=input("Дедушка мороз  старый?")
if q4=="да"or q4=="старый":
        print("Congratulation")
        score= score + 1
else:
    print("Lose")
    score= score - 1
q5=input("Илюша  станет програмистом??")
if q5=="да"or q5=="Конечно":
    print("Congratulation")
    score= score + 1
else:
    print("Lose")
    score= score - 1

if score>3:
    x=input("Вы набрали больше 3 очков хотите ответить на дополнительные вопросы?")
    if x=="да":
     print("Сегодня хорошее настроение?")
    else:
     print("Всего  вам хорошего")
else:
    print ("Игра закончена"+"вЫ НАБРАЛИ")
    print(score)
y=input
if y == "да":
    print("Да хватит брат дополнительных вопросов")
else:
    print("Да хватит брат дополнительных вопросов")

"""
"""Тема Урока ЦЫКЛ"""
"""Цикл начинается с команлы фор"""
# Сработает пока  ай больше 133 и меньше 138 есди после 2 символо добавить цифру через щапитую то они выйжут с шагом этой цифры тоесть не каждый первйы а каждый второй третий да любой

"""30 Мая Циклы поглубже"""
"""number=1
ЦИКЛЫ В ЦИКЛЕ ЭТО КАК СКУНДА МИНУТА ЧАС ДЕНЬ ГОД И ТД"""
"""import time
for h in range (0,24): # i=2
    for m in range(0,60):
        for s in range(0,60):# j=2 cначала круг снизу потом +1 к кругу сверху 
            print (f"Ч:{h}м:{m}c:{s}")
            time.sleep(1)
"""
"""h=0
m=0
s=0
while h<24:
    m=0
    while m<60:
        s=0
        while s<60:
            print (f"Ч:{h}м:{m}c:{s}")
            s+=1
        m+=1        
    h+=1"""

# Использование циклов вкнутри циклов с возвратом значений , + условия

print ("Регистраиця персонажа")
reg=0
while reg<1:
    reg_gender =0
    while reg_gender <1:
        gender=(input("Выберите пол персонажа'\n1-мужской \n2 - женский \n: "))
        if gender =="1":
            gender = "Мужской"
            reg_gender +=1
        elif gender =="2":
            gender="Женский"
            reg_gender +=1
        else:
            print ("Выберите либо 1 либо 2")
        if reg_gender==1:  
            reg_race=0
            while reg_race<1:
                race=input("0< - назад  Выберите расу персонажам \n1 - Человек \n2 - Эльф\n: ")
                if race=="1":
                    race= "Человек"
                    reg_race+=1
                elif race== "2":
                    race= "Эльф"
                    reg_race+=1
                elif race =="0":
                    reg_gender = 0
                    break 
                else:
                    print ("Выберите либо 1 либо 2")

    reg+=1            
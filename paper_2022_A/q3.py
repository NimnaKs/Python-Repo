a = 1
#global

def func1():
    print('Inside func1() : ', a)


def func2():
    a = 2
    #local variable
    print('Inside func2() : ', a)

def func3():
    global a
    a = 3
    print('Inside func3() : ', a)

func1()
func2()
func3()


# Inside func1() : 1
# Inside func2() : 2
# Inside func3() : 3
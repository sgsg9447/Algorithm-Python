#파이썬 함수식 및 람다 

#함수 정의식 및 람다()

#함수 정의 방법
#def 함수명 (parameter):
#   code

#함수 호출
#함수명(parameter)

#함수 선언 위치 중요

#예제1

def hello(world):
    print("Hello", world)

hello("python")
hello(777)

def hello_return(world):
    val = "Hello" + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

#예재3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)


#예재4 (다중리턴)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt, type(lt))

#예제5
# *args, *kwargs
#매개변수가 몇개를 받을 지 모를때 함수의 작동을 달리할때 여러가지 기능을 하는!
# *하나일때는 튜플로 받고, ** 두개일때는 딕셔너리로 받음!

def args_func(*args):
    # for t in args:
    #     print(t)

    for i,v in enumerate(args):
        print(i,v)

args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')


# kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1="kim", name2="park")

#전체혼합
def example_mul(arg1,arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10,20, 'park', 'kim', age1=24, age2 = 35)

#중첩함수(클로저)
def nasted_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num+10000)

nasted_func(10000)


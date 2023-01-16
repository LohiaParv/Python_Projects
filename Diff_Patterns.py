def pattern1():  # todo - right side pattern
    """
    How this works:
                           *
                          **
                         ***
                        ****
                       *****

    outerloop   Space   Print *
    0           4       1
    1           3       2
    2           2       3
    3           1       4
    4           0       5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Space: a - i;   range 4-0 - 4,3,2,1,0
    Print *: i + 1; range 1-5 - 1,2,3,4,5

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        print()


def pattern2():  # todo - right side pattern with numbers
    """
    How this works:
                           1
                          12
                         123
                        1234
                       12345

    outerloop   Space   Print *
    0           4       1
    1           3       2
    2           2       3
    3           1       4
    4           0       5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Space: a - i;   range 4-0 - 4,3,2,1,0
    Print *: i + 1; range 1-5 - 1,2,3,4,5
    *number - when printing instead of *, print k+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print(k+1, end="")
        print()


def pattern3():  # todo - right side pattern with number doubles
    """
    How this works:
                           1
                          22
                         333
                        4444
                       55555

    outerloop   Space   Print *
    0           4       1
    1           3       2
    2           2       3
    3           1       4
    4           0       5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Space: a - i;   range 4-0 - 4,3,2,1,0
    Print *: i + 1; range 1-5 - 1,2,3,4,5
    *number - when printing instead of *, print i+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print(i+1, end="")
        print()


def pattern4():  # todo - left side pattern
    """
    How this works:
                    *
                    **
                    ***
                    ****
                    *****

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print("*", end="")
        print()


def pattern5():  # todo - left side pattern with numbers
    """
    How this works:
                    1
                    12
                    123
                    1234
                    12345

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5
    *number - when printing instead of *, print j+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print(j+1, end="")
        print()


def pattern6():  # todo - left side pattern with number doubles
    """
    How this works:
                    1
                    22
                    333
                    4444
                    55555

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:    - i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5
    *number - when printing instead of *, print j+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print(i+1, end="")
        print()


def pattern7():  # todo - right arrow pattern
    """
    How this works:
                *
                **
                ***
                ****
                *****
                ****
                ***
                **
                *

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Print *: a - i - 1; range 4-0 - 4,3,2,1,0 - below part

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print("*", end="")
        print()
    for i in range(a):
        for k in range(a-i-1):
            print("*", end="")
        print()


def pattern8():  # todo - right arrow pattern with number
    """
    How this works:
                1
                12
                123
                1234
                12345
                1234
                123
                12
                1

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Print *: a - i - 1; range 4-0 - 4,3,2,1,0 - below part
    *number1 - when printing instead of *, print j+1 for same loop
    *number2 - when printing instead of *, print k+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print(j+1, end="")
        print()
    for i in range(a):
        for k in range(a-i-1):
            print(k+1, end="")
        print()


def pattern9():  # todo - right arrow pattern with number doubles
    """
    How this works:
                1
                22
                333
                4444
                55555
                4444
                333
                22
                1

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Print *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Print *: a - i - 1; range 4-0 - 4,3,2,1,0 - below part
    *number1 - when printing instead of *, print i+1 for same loop
    *number2 - when printing instead of *, print a-i-1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i+1):
            print(i+1, end="")
        print()
    for i in range(a):
        for k in range(a-i-1):
            print(a-i-1, end="")
        print()


def pattern10():  # todo - left arrow pattern with number doubles
    """
    How this works:
                 *
                **
               ***
              ****
             *****
              ****
               ***
                **
                 *

    outerloop   Print *
    0            1
    1            2
    2            3
    3            4
    4            5

    a = 5
    Loop1:      i;   range 0-5 - 0,1,2,3,4
    Space1:   a - 1; range 4-0 - 4,3,2,1,0
    Print1 *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Loop2:      i;   range 0-5 - 0,1,2,3,4
    Space2:   i + 2; range 2-5 - 2,3,4,5
    Print2 *: a- i - 1; range 4-0 - 4,3,2,1,0 - upper part

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        print()
    for i in range(a):
        for j in range(i+2):
            print(" ", end="")
        for k in range(a-i-1):
            print("*", end="")
        print()


def pattern11():  # todo - left arrow pattern with number
    """
    How this works:
                 1
                12
               123
              1234
             12345
              1234
               123
                12
                 1


    a = 5
    Loop1:      i;   range 0-5 - 0,1,2,3,4
    Space1:   a - 1; range 4-0 - 4,3,2,1,0
    Print1 *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Loop2:      i;   range 0-5 - 0,1,2,3,4
    Space2:   i + 2; range 2-5 - 2,3,4,5
    Print2 *: a- i - 1; range 4-0 - 4,3,2,1,0 - upper part
    *number1 - when printing instead of *, print k+1 for same loop
    *number2 - when printing instead of *, print k+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print(k+1, end="")
        print()
    for i in range(a):
        for j in range(i+2):
            print(" ", end="")
        for k in range(a-i-1):
            print(k+1, end="")
        print()


def pattern12():  # todo - left arrow pattern with number doubles
    """
    How this works:
                 1
                22
               333
              4444
             55555
              4444
               333
                22
                 1

    a = 5
    Loop1:      i;   range 0-5 - 0,1,2,3,4
    Space1:   a - 1; range 4-0 - 4,3,2,1,0
    Print1 *: i + 1; range 1-5 - 1,2,3,4,5 - upper part
    Loop2:      i;   range 0-5 - 0,1,2,3,4
    Space2:   i + 2; range 2-5 - 2,3,4,5
    Print2 *: a- i - 1; range 4-0 - 4,3,2,1,0 - upper part
    *number1 - when printing instead of *, print i+1 for same loop
    *number2 - when printing instead of *, print a-i+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i):
            print(" ", end="")
        for k in range(i+1):
            print(i+1, end="")
        print()
    for i in range(a):
        for j in range(i+2):
            print(" ", end="")
        for k in range(a-i-1):
            print(a-i-1, end="")
        print()


def pattern13():  # todo - left arrow pattern with number doubles
    """
    How this works:
         *
        ***
       *****
      *******
     *********


    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: a-i-1; range 4-0 - 4,3,2,1,0
    Print *: 2 * i + 1; range 1-9 - upper part

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()


def pattern14():  # todo - left arrow pattern with number doubles
    """
    How this works:
            1
           123
          12345
         1234567
        123456789

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: a-i-1; range 4-0 - 4,3,2,1,0
    Print *: 2 * i + 1; range 1-9 - upper part
    *number1 - when printing instead of *, print k+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print(k+1, end="")
        print()


def pattern15():  # todo - left arrow pattern with number doubles
    """
    How this works:
            1
           222
          33333
         4444444
        555555555

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: a-i-1; range 4-0 - 4,3,2,1,0
    Print *: 2 * i + 1; range 1-9 - upper part
    *number1 - when printing instead of *, print i+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print(i+1, end="")
        print()


def pattern16():  # todo - left arrow pattern with number doubles
    """
    How this works:
        *********
         *******
          *****
           ***
            *


    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: i; range 0-5
    Print *: 2*a - 2*i - 1; range 9-0

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print("*", end="")
        print()


def pattern17():  # todo - down arrow pattern with number
    """
    How this works:
            123456789
             1234567
              12345
               123
                1

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: i; range 0-5
    Print *: 2*a - 2*i - 1; range 9-0
    *number1 - when printing instead of *, print k+1 for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print(k+1, end="")
        print()


def pattern18():  # todo - left arrow pattern with number doubles
    """
    How this works:
            999999999
             7777777
              55555
               333
                1

    a = 5
    Loop:      i;   range 0-5 - 0,1,2,3,4
    Space: i; range 0-5
    Print *: 2*a - 2*i - 1; range 9-0
    *number1 - when printing instead of *, print a-i for same loop
    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print(a-i, end="")
        print()


def pattern19():  # todo - left arrow pattern with number doubles
    """
    How this works:
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
*****************
 ***************
  *************
   ***********
    *********
     *******
      *****
       ***
        *

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        print()
    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print("*", end="")
        print()


def pattern20():  # todo - left arrow pattern with number doubles
    """
    How this works:
            1
           123
          12345
         1234567
        123456789
        123456789
         1234567
          12345
           123
            1

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print(k+1, end="")
        print()
    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print(k+1, end="")
        print()


def pattern21():  # todo - left arrow pattern with number doubles
    """
    How this works:
            1
           222
          33333
         4444444
        555555555
        555555555
         4444444
          33333
           222
            1

    """
    a: int = int(input("Enter number here : "))

    for i in range(a):
        for j in range(a-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print(i+1, end="")
        print()
    for i in range(a):
        for j in range(i):
            print(" ", end="")
        for k in range(2*a-2*i-1):
            print(a-i, end="")
        print()


def main():
    for i in range(1,22,1):
        val = "pattern" + str(i) + "(" + ")"
        exec(val)

main()


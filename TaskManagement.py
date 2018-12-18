from collections import deque

dq = deque([])

PriorityTypes = ['High', 'Low']

loop = 1

while loop == 1:
    TaskNumber = input("Input Task Number: ")
    Priority = input("Define High or Low priority: ")
    print(TaskNumber)
    print(Priority)

    if TaskNumber is int:
        if Priority in PriorityTypes:
            if Priority == 'High':
                dq.appendleft(TaskNumber)
                print(dq)
            else:
                dq.append(TaskNumber)
                print(dq)
        else:
            print("Priorty must be set as High or Low.  Please Try again scumbag!!")
    else:
        print("Task Number MUST be a numeric value .  Please Try again scumbag!!")
        print(dq)
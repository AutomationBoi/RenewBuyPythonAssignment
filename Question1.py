"""
We assume the input will always be in the form name,age,score

"""


def sortTuples(listofTuple):
    return sorted(listofTuple)


if __name__=='__main__':
    lines = []
    print('Enter Name, age, score')
    while True:
        line = input()
        if line:
            lines.append((line))
        else:
            break

    listOfTuple=[tuple(i.split(',')) for i in lines]
    print(sortTuples(listOfTuple))


"""

Test Cases:

1 [same name, same age, different score]

2 [same name, different age, same score]

3 [different name, same age, same score]


Default input

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85


Case 1
Tom,19,80
Tom,19,90
Jony,17,91
Jony,17,93
Json,21,85

Expected: [('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80'), ('Tom', '19', '90')]
Actual: [('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80'), ('Tom', '19', '90')]



Case 2
Tom,19,80
Tom,20,80
Jony,17,91
Jony,17,93
Json,21,85

Expected: [('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80'), ('Tom', '20', '80')]
Actual: [('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80'), ('Tom', '20', '80')]

Case 3
Tom,19,80
Andy,19,80
Jony,17,91
Jony,17,93
Json,21,85

Expected: [('Andy', '19', '80'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Actual: [('Andy', '19', '80'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""
#Name: Gloria Silva
#Assignment: proj7.py
#Date: 18 November, 2025
#Description: This project reads Student ID numbers and grades from a file, calculates the averages of the grades, and outputs the results to the screen and onto a file. 


def calc_average(score1,score2,score3):
    scores = score1 + score2 + score3
    average = scores/3
    return average

def main():
    file = open("scores.txt", "r")
    line = file.readline()
    line = line.strip()
    output_file = open("grades.txt","w")
    while line != "":
        score1 = float(file.readline())
        score2 = float(file.readline())
        score3 = float(file.readline())
        student_average = calc_average(score1, score2, score3)
        student_average = round(student_average, 2)
        print(f'Student {line} average is {student_average:.2f}')
        f = student_average
        output_file.write(f'{line} {f:.2f}')
        output_file.write('\n')
        line = file.readline()
        line = line.strip()
    output_file.close()
    file.close()

main()
    
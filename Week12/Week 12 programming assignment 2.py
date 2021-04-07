n = int(input())    #taking no. of question comes in Gate exam ferom the user

ramesh_answer = input().split()

suresh_answer = input().split()

max_marks = 0

for i in range(n):

  if ramesh_answer[i] not in suresh_answer[i] and suresh_answer[i] != "." and ramesh_answer[i] !=".":

    max_marks += 1
print(max_marks, end="")
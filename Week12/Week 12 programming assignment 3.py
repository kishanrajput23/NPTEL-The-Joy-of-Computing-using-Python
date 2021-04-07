# importing math modulw
import math

#taking length of side PQ 
PQ = int(input())

#taking length of side PR
PR = int(input())

#finding length of side QR
QR = (PQ * PQ + PR * PR) ** (0.5)

#finding the angle XQR
Angle_XQR = math.asin(PQ / QR)

#rounding off the value to nearest integer
print(round(math.degrees(Angle_XQR)),end="")
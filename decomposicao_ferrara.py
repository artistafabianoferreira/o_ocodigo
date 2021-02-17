"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import math
import operator

#a = eval(input("Enter a number: "))
#a = 95414241933104212211
a = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
size = str(a)
size_var = len(size)
print ("The number has ",size_var," digits.")

prime_number = 1
q1 = int(math.sqrt(a))

size_q1 = str(q1)
size_var_q1 = len(size_q1)
verify_final_zero = size_q1[-1:]
if (int(verify_final_zero) == 0):
    q1 = q1 + 1

print ("The square root of ",a," is ",q1)

if (q1 % 2 == 0):
   q1 = q1 - 1
   print ("The odd value of q1 is ",q1)
   
r = 2
counter = 0
result = 0
subresult = 1
rest = 1

#Start of the MDeven calculation
MDeven = ""
MDeven_cont = 1

if (size_var % 2 == 0):
   MDeven_aux = int((size_var / 2) - 1)
else:
   MDeven_aux = int(((size_var / 2) + 0.5) - 1)

print ("MDeven has ",MDeven_aux," digits.")
MDeven_aux = MDeven_aux - 5
MDeven = operator.concat(MDeven,"1011")

while (MDeven_cont <= MDeven_aux):
       MDeven = operator.concat(MDeven,"9")
       MDeven_cont = MDeven_cont + 1
MDeven = operator.concat(MDeven,"8")
print ("MDeven is ",MDeven)
#End of MDeven calculation.

#Start of the MDevenX calculation
MDevenX = ""
MDevenX_cont = 1
MDevenX_aux = MDeven_aux + 2
MDevenX = operator.concat(MDevenX,"2")
while (MDevenX_cont < MDevenX_aux):
       MDevenX = operator.concat(MDevenX,"9")
       MDevenX_cont = MDevenX_cont + 1
MDevenX = operator.concat(MDevenX,"8")
print ("MDevenX is ",MDevenX)
#End of MDevenX calculation.

#Start of the MDevenY calculation
MDevenY = ""
MDevenY_cont = 1
MDevenY_aux = MDeven_aux - 1
MDevenY = operator.concat(MDevenY,"200")
while (MDevenY_cont < MDevenY_aux):
       MDevenY = operator.concat(MDevenY,"9")
       MDevenY_cont = MDevenY_cont + 1
MDevenY = operator.concat(MDevenY,"8")
print ("MDevenY is ",MDevenY)
#End of MDevenY calculation.

#Start of the MDevenZ calculation
MDevenZ = ""
MDevenZ_cont = 1
MDevenZ_aux = MDeven_aux - 2
MDevenZ = operator.concat(MDevenZ,"48")
while (MDevenZ_cont < MDevenZ_aux):
       MDevenZ = operator.concat(MDevenZ,"0")
       MDevenZ_cont = MDevenZ_cont + 1
MDevenZ = operator.concat(MDevenZ,"2")
print ("MDevenZ is ",MDevenZ)
#End of MDevenZ calculation.

#Start of the MDevenW calculation
MDevenW = ""
MDevenW_cont = 1
MDevenW_aux = MDeven_aux - 41
MDevenW = operator.concat(MDevenW,"12859184575916856568975466716076826358585")
while (MDevenW_cont < MDevenW_aux):
       MDevenW = operator.concat(MDevenW,"0")
       MDevenW_cont = MDevenW_cont + 1
MDevenW = operator.concat(MDevenW,"366")
print ("MDevenW is ",MDevenW)
#End of MDevenW calculation.

newMDeven = (int(MDeven) + int(MDevenX) + int(MDevenY) + int(MDevenZ) + int(MDevenW))
print ("Novo valor de MDPAR é ", newMDeven)
while ((rest != 0) or (result >= q1)):
   subresult = (q1 - (newMDeven + (counter * r)))
   result = a / subresult
   counter = counter + 1
   rest = a % subresult

   if (rest == 0):
         print ("The number ",subresult," is the smallest prime factor of ",a,". So ",a," is a compound number.")
         result = 1
         prime_number = 0
   

if (prime_number != 0):
    print ("The number ",a," is a prime number.")

print ("End of calculation.")

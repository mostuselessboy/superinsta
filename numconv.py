#Convert Number To Variable
#by Syed Hamza


def numconv(num):
  if 0 <= num <= 999:
     result_num=(num)
  elif 999 < num <= 9999:
     result_num=( str(num)[0:1]+ ","+ str(num)[1:])
  elif 9999 < num <= 99999:
     result_num=( str(num)[0:2]+ "."+str(num)[2:3]+"K")
  elif 99999 < num <= 999999:
     result_num=( str(num)[0:3]+ "."+str(num)[3:4]+"K")
  elif 999999 < num <= 9999999:
     result_num=( str(num)[0:1]+ "."+str(num)[1:2]+"M")
  elif 9999999 < num <= 99999999:
     result_num=( str(num)[0:2]+ "."+str(num)[2:3]+"M")
  elif 99999999 < num <= 999999999:
     result_num=( str(num)[0:3]+ "."+str(num)[3:4]+"M")
  elif 999999999 < num <= 9999999999:
     result_num=( str(num)[0:1]+ "."+str(num)[1:2]+"B")
  elif 9999999999 < num <= 99999999999:
     result_num=( str(num)[0:2]+ "."+str(num)[2:3]+"B")
  elif 99999999999 < num <= 999999999999:
     result_num=( str(num)[0:3]+ "."+str(num)[3:4]+"B")
  return result_num


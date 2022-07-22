import datetime

ct = datetime.datetime.now()

file_extension = str(ct.year)+str(ct.month).zfill(2)+str(ct.day).zfill(2)+"_"+str(ct.hour).zfill(2)+str(ct.minute).zfill(2)+"_"+str(ct.second).zfill(2)

##print(file_extension)

print(ct.year)

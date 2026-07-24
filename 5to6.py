import os, shutil


basedir=os.getcwd()
#5N to N
os.mkdir('NewN')
for i in range(194,253):
    shutil.copy(os.path.join(basedir,f'FH5N\\sound_{i}.wav'),os.path.join(basedir,f'NewN\\sound_{i-109}.wav'))
    print(i)
for i in range(253,312):
    shutil.copy(os.path.join(basedir,f'FH5N\\sound_{i}.wav'),os.path.join(basedir,f'NewN\\sound_{i-66}.wav'))
    print(i)
for i in range(6071,6079):
    shutil.copy(os.path.join(basedir,f'FH5N\\sound_{i}.wav'),os.path.join(basedir,f'NewN\\sound_{i+1021}.wav'))
    print(i)

#5E to E
os.mkdir('NewE')
for i in range(1,46):
    shutil.copy(os.path.join(basedir,f'FH5E\\sound_{i}.wav'),os.path.join(basedir,f'NewE\\sound_{i+3}.wav'))
    print(i)
for i in range(0,4):
    shutil.copy(os.path.join(basedir,f'FH5E\\sound_{i}.wav'),os.path.join(basedir,f'NewE\\sound_{i}.wav'))
    print(i)

os.system('pause')
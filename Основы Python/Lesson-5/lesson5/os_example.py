import os

print(os.name)

# os.path.curdir - текущая директория
print(os.path.abspath(os.curdir))
print(os.path.join(os.curdir, 'modules_dir'))

try:
    os.mkdir('modules_dir')
    print('modules_dir created')
except OSError as e:
    print(e)

if not os.path.exists('test_dir'):
    os.mkdir('test_dir')
    print('test created')
else:
    print('test exists')

open(os.path.join('test_dir', '1.txt'), 'w').close()

try:
    os.rmdir('test_dir')
except OSError as e:
    print(e)

for f in os.listdir('test_dir'):
    os.remove(os.path.join('test_dir', f))

os.rmdir('test_dir')
print("dir test_dir was removed")


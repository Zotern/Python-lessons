import os


def create_dir_tree(base, depth):
    """Создает структуру каталогов указанной глубины."""
    dirname = os.path.join(base, f'dir{depth}')
    os.mkdir(dirname)
    open(os.path.join(base, f'file{depth}.txt'), 'w').close()
    if depth > 0:
        create_dir_tree(dirname, depth - 1)
    return dirname


def rm_dir_tree_recursive(path):
    for f in os.listdir(path):
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            rm_dir_tree_recursive(fullname)
        else:
            os.remove(fullname)

    os.rmdir(path)


def rm_dir_tree_walk(path):
    for root, dirnames, filenames in os.walk(path, topdown=False):
        for f in filenames:
            os.remove(os.path.join(root, f))
        for d in dirnames:
            os.rmdir(os.path.join(root, d))
    os.rmdir(path)


root_dir = create_dir_tree(os.path.curdir, 3)
input("press enter to remove dir: {}".format(root_dir))
# rm_dir_tree_recursive(root_dir)
rm_dir_tree_walk(root_dir)

from Libraries import *
train_dir = './Dataset/fer-2013/train/'
test_dir = './Dataset/fer-2013/test/'

row, col = 48, 48
classes = 7

def count_exp(path, set_):
    dict_ = {}
    for expression in os.listdir(path):
        dir_ = path + expression
        dict_[expression] = len(os.listdir(dir_))
    df = pd.DataFrame(dict_, index=[set_])
    return df

def print_dataset():
    train_count = count_exp(train_dir, 'train')
    test_count = count_exp(test_dir, 'test')
    # print(train_count)
    # print(test_count)
    # train_count.transpose().plot(kind='bar')
    # test_count.transpose().plot(kind='bar')
    plt.figure(figsize=(14,22))
    i = 1
    for expression in os.listdir(train_dir):
        img = load_img((train_dir + expression +'/'+ os.listdir(train_dir + expression)[5]))
        plt.subplot(1,7,i)
        plt.imshow(img)
        plt.title(expression)
        plt.axis('off')
        i += 1
    plt.show()
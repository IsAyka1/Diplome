from Libraries import *
from Dataset import train_dir, test_dir

def test():
    train_datagen = ImageDataGenerator(rescale=1./255,
                                       horizontal_flip=True,
                                       validation_split=0.2)

    training_set = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=64,
                                                    target_size=(48, 48),
                                                    shuffle=True,
                                                    color_mode='grayscale',
                                                    class_mode='categorical',
                                                    subset='training')
    validation_set = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=64,
                                                    target_size=(48, 48),
                                                    shuffle=True,
                                                    color_mode='grayscale',
                                                    class_mode='categorical',
                                                    subset='validation')

    test_datagen = ImageDataGenerator(rescale=1./255,
                                       horizontal_flip=True)
    test_set = test_datagen.flow_from_directory(test_dir,
                                                    batch_size=64,
                                                    target_size=(48, 48),
                                                    shuffle=True,
                                                    color_mode='grayscale',
                                                    class_mode='categorical')

    return training_set, validation_set, test_set


def gen(train_datagen, training_set, test_set):
    train_datagen.fit(training_set)
    train_datagen(training_set)
    X_y = train_datagen.flow(test_set)
    k = -1
    img_cols = img_rows = 28
    for i in range(len(X_y)):
        k += 1
        plt.subplot(2, 8, k + 1)
        img = X_y[i][0].astype('uint8')
        img = img.reshape(img_rows, img_cols)
        if k == 0:
            print(img)
        plt.imshow(img, cmap = plt.get_cmap('gray'))
        #plt.title()
        plt.axis('off')
        if k == 15: break
    plt.subplots_adjust(hspace = 0.1) # wspace
    plt.show()
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
#这个类可以用来实例化一个神经网络模型。
from tensorflow.python.keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,Dropout

#这一行创建了一个Sequential模型的实例，即一个按顺序堆叠的神经网络模型。
model=Sequential()
#这一行向模型中添加了一个卷积层(Convolutional Layer)，其中包含了10个卷积核(filter)，每个卷积核的大小为5x5。激活函数使用ReLU(Rectified Linear Unit)，输入图像的大小为28x28，且是单通道图像（灰度图像）。
model.add(Conv2D(10,(5,5),activation="relu",input_shape=(28,28,1)))
#接下来添加了一个最大池化层(MaxPooling Layer)，用于降低卷积层输出的空间维度，这里的池化窗口大小为2x2。
model.add(MaxPooling2D(pool_size=(2,2)))
#再次添加了一个卷积层，这次有20个卷积核，大小仍为5x5，激活函数同样使用ReLU。
model.add(Conv2D(20,(5,5),activation="relu"))

model.add(MaxPooling2D(pool_size=(2,2)))
#在此之后添加了一个Dropout层，用于在训练过程中随机丢弃部分神经元，以防止过拟合。
model.add(Dropout(0.25))
#添加了一个Flatten层，用于将多维输入展平为一维，为接下来的全连接层做准备。
model.add(Flatten())
#添加了一个全连接层，包含100个神经元，激活函数使用ReLU。
model.add(Dense(100,activation="relu"))
#最后添加了一个全连接层，包含10个神经元，激活函数使用softmax，适用于多类别分类任务。 #多个类别用softmax，两个类别用sigmod
model.add(Dense(10,activation="softmax"))

#编译模型，指定优化器为RMSprop，损失函数为分类交叉熵(categorical crossentropy)，评估指标为准确率。
model.compile(optimizer="rmsprop",loss=tf.keras.losses.categorical_crossentropy,metrics=['accuracy'])

#keras是TensorFlow的高级API，相当于已经封装好的功能可以直接用
mnist=tf.keras.datasets.mnist
#函数返回两个元组，每个元组包含图像数据和对应的标签数据。这里通过元组解包的方式将训练集和测试集分别赋值给x_train、y_train和x_test、y_test。
(x_train,y_train),(x_test,y_test)=mnist.load_data("C:/Users/ASUS/mnist.npz")

#normalized图片处理
normalized_x_train=tf.keras.utils.normalize(x_train,axis=1)
normalized_x_test= tf.keras.utils.normalize(x_test,axis=1)

#one_hot标签处理
#这行代码将训练集的标签数据进行独热编码处理。tf.one_hot()函数将标签数据转换为独热编码形式，这里10表示类别的数量，因为MNIST数据集包含10个类别（0-9）。
one_hot_y_train=tf.one_hot(y_train,10)
one_hot_y_test=tf.one_hot(y_test,10)

#-1表示第一个维度不用管
#这行代码将训练集的归一化后的图像数据进行形状调整。reshape()函数用于调整数据的形状，这里-1表示第一个维度不用管，28,28,1表示将数据调整为28x28的灰度图像（单通道）。
reshaped_x_train=normalized_x_train.reshape(-1,28,28,1)  
reshaped_x_test=normalized_x_test.reshape(-1,28,28,1)

train_result = model.fit(reshaped_x_train, one_hot_y_train, epochs=2, validation_data=(reshaped_x_test, one_hot_y_test))

import matplotlib.pyplot as plt
plt.plot(train_result.history['accuracy'])
plt.plot(train_result.history['val_accuracy'])
plt.legend(["Accuracy","Validation Acc"])
plt.show()

#accuracy:训练集准确率
#val_accruacy:测试集准确率

import cv2
img = cv2.imread("5.jpg")
img_width=img.shape[1]
img_height=img.shape[0]
col_start=int((img_width-img_height)/2)
col_end=int(col_start+img_height)
cropped_img=img[:,col_start:col_end,:]
gray_img=cv2.cvtColor(cropped_img,cv2.COLOR_BGR2GRAY)   #转灰度
(thresh,black_white)=cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)   #转黑白
black_white=cv2.bitwise_not(black_white)   #反转
black_white=cv2.resize(black_white,(28,28))   #调整大小


cv2.imshow("a 3",black_white)
cv2.waitKey(0)  #等待界面上的输入
cv2.destroyAllWindows()  #释放资源



black_white=black_white/255   #进行归一化处理
black_white=black_white.reshape(-1,28,28,1)
prediction=model.predict(black_white)
prediction  #-1的作用就是在prediction外面再套一个[]

import numpy as np
print(np.argmax(prediction))
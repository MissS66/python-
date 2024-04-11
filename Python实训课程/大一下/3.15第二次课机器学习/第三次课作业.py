import tensorflow as tf
#将 MNIST 数据集赋值给变量 mnist。
mnist=tf.keras.datasets.mnist
#(x_train,y_train),(x_test,y_test)=mnist.load_data()
(x_train,y_train),(x_test,y_test)=mnist.load_data("mbist.npz")
#这行代码用于输出 x_train 的形状，即训练数据的维度信息。
print(x_train.shape)

#对 MNIST 数据集中的训练图像进行归一化处理。
#这种归一化操作通常用于将数据缩放到一个特定的范围，以便更好地进行训练。
#axis=1 表示对每张图像的像素值在水平方向（即每一行）进行归一化处理。
#这意味着对于每张图像，其像素值将被缩放，使得每一行的数值范围在同一区间内。
#请注意，归一化应该在数据预处理阶段完成
x_train=tf.keras.utils.normalize(x_train,axis=1)
#使用jkeras自带的normalize工具进行归一化
#同样的，x_test也需要归一化处理
x_test=tf.keras.utils.normalize(x_test,axis=1)

#创建DNN模型（MLP）—原始神经网络
#输入层：784
#Hidden Layer1:128
#Hidden Layer2:128
#输出层：10
#输入层:784  因为图片是28*28的，所以展开后是784.
model = tf.keras.models.Sequential()    
#首先创建一个模型，使用Sequential,Keras有两种不同的构建模型的方法：
#Sequential models和Functional API
#Sequential非常强大，接口简单易懂，大部分情况下，
#只需用Sequential模型即可满足需求。需要更复杂的模型结构时就需要Functional API
#用来将多维数据转化为一维数据
model.add(tf.keras.layers.Flatten())

#创建隐藏层
#Hidden layers1：128  构建第一个隐藏层，每一层有128个神经元
#使用 ReLU（修正线性单元）作为激活函数。在深度学习中，ReLU 是一种常用的非线性激活函数，它可以帮助网络学习复杂的模式。
#model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))

#128: 这表示该层有128个神经元。这个数字是一个超参数，可以根据具体问题和模型的需求进行调整。
#activation=tf.nn.relu: 这部分指定了该层的激活函数为 ReLU。激活函数在神经网络中非常重要，它帮助网络引入非线性，从而使网络能够学习更加复杂的模式。
#model.add(): 这部分将创建的 Dense 层添加到神经网络模型中。在使用 Keras 构建神经网络时，我们通过 model.add() 方法逐层添加神经网络的各个组件，如全连接层、卷积层等。

#创建输出层
#输出层：10，因为输出对应0-9，所以有10层
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))
#softmax可以处理多分类问题

#配置训练方法
##格式：model.compile(optimizer = 优化权重，
#loss = 误差（用来测量误差），metrics = ["准确率”])
model.compile(#用于在配置训练方法时
#告知训练时用的优化器，损失函数和准确率评测标准
#基于训练数据和损失函数来更新网络的机制，常用的有Adam， RMSprop、SGD等
optimizer='adam',
#网络衡量在训练数据上的性能，即网络如何朝着正确的方向前进。
#BinaryCrossentropy, CategoricalCrossentropy,KLDivergence等
loss='sparse_categorical_crossentropy',
#训练和测试过程中需要监控的指标。
#常用的有AUC、Accuracy、BinaryAccuracy、BinaryCrossentropy, CategoricalCrossentropy, KLDivergence、Precision等等
metrics=['accuracy'])

#训练DNN模型
#将训练数据给模型进行训练
#epochs=5: 这里指定了训练的轮数。
model.fit(x_train,y_train,epochs=5)
#model.fit()方法用于执行训练过程

#检测效果
#这是 Keras 模型中用于评估模型性能的方法。evaluate() 方法会使用测试数据集来评估模型的性能，
#并返回评估指标，如损失值和准确率。
val_loss,val_acc = model.evaluate(x_test,y_test)
print("loss=",val_loss,"acc=",val_acc)

import cv2
import warnings
warnings.filterwarnings("ignore")

#导入图片
img=cv2.imread("6.jpg")
cv2.imshow("6",img)
cv2.waitKey(0)#等待界面上的输入
cv2.destroyAllWindows()#释放资源

#裁图
img_height=img.shape[0]
#img.shape第一个参数是高
img_width=img.shape[1]
#宽
col_start=int((img_width-img_height)/2)
#截取起点是（宽-高）/2
col_end=int(col_start+img_height)
#截取终点
cropped_img=img[:,col_start:col_end,:]
#最终图片参数，第一个冒号是高，第二个是宽，第三个是深度（此处不涉及深度，可以不管）
cv2.imshow('6',cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()#释放资源

#转灰度
gray_img=cv2.cvtColor(cropped_img,cv2.COLOR_BayerBG2GRAY)

cv2.imshow("6",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()#释放资源

black_white=black_white.reshape(-1,28,28,1)
prediction=model.predict(black_white)

print(prediction)
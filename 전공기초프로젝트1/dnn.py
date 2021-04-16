import tensorflow as tf
import numpy as np

class Model_Time(object):

    def __init__(self):
        self.X = tf.placeholder(tf.float32, shape=[None, 3])
        self.Y = tf.placeholder(tf.float32, shape=[None, 15])

        self.W1 = tf.Variable(tf.random_uniform([3, 15], -1., 1.))
        self.b1 = tf.Variable(tf.zeros([15]))
        self.L1 = tf.nn.relu(tf.add(tf.matmul(self.X, self.W1), self.b1))

        self.W2 = tf.Variable(tf.random_normal([15, 30]))
        self.b2 = tf.Variable(tf.zeros([30]))
        self.L2 = tf.nn.relu(tf.add(tf.matmul(self.L1, self.W2), self.b2))

        self.W3 = tf.Variable(tf.random_normal([30, 60]))
        self.b3 = tf.Variable(tf.zeros([60]))
        self.L3 = tf.nn.relu(tf.add(tf.matmul(self.L2, self.W3), self.b3))

        self.W4 = tf.Variable(tf.random_normal([60, 40]))
        self.b4 = tf.Variable(tf.zeros([40]))
        self.L4 = tf.nn.relu(tf.add(tf.matmul(self.L3, self.W4), self.b4))

        self.W5 = tf.Variable(tf.random_normal([40, 30]))
        self.b5 = tf.Variable(tf.zeros([30]))
        self.L5 = tf.nn.relu(tf.add(tf.matmul(self.L4, self.W5), self.b5))

        self.W6 = tf.Variable(tf.random_normal([30, 15]))
        self.b6 = tf.Variable(tf.zeros([15]))
        self.model = tf.add(tf.matmul(self.L5, self.W6), self.b6)

        self.cost = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(labels=self.Y, logits=self.model))
        
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        self.train_op = self.optimizer.minimize(self.cost)


    def TRAIN(self, x_data, y_data, iter):
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)
    
        for step in range(iter):
            self.sess.run(self.train_op, feed_dict={self.X: x_data, self.Y: y_data})   
    

    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100)
        self.prediction = tf.argmax(self.model, 1)
        return self.sess.run(self.prediction, feed_dict={self.X: p_data})
        
        # is_correct = tf.equal(prediction, target)
        # accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
        # print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))
        self.sess.close()


class Model_Week(object):

    def __init__(self):
        self.X = tf.placeholder(tf.float32, shape=[None, 3])
        self.Y = tf.placeholder(tf.float32, shape=[None, 7])

        self.W1 = tf.Variable(tf.random_uniform([3, 15], -1., 1.))
        self.b1 = tf.Variable(tf.zeros([15]))
        self.L1 = tf.nn.relu(tf.add(tf.matmul(self.X, self.W1), self.b1))

        self.W2 = tf.Variable(tf.random_normal([15, 30]))
        self.b2 = tf.Variable(tf.zeros([30]))
        self.L2 = tf.nn.relu(tf.add(tf.matmul(self.L1, self.W2), self.b2))

        self.W3 = tf.Variable(tf.random_normal([30, 60]))
        self.b3 = tf.Variable(tf.zeros([60]))
        self.L3 = tf.nn.relu(tf.add(tf.matmul(self.L2, self.W3), self.b3))

        self.W4 = tf.Variable(tf.random_normal([60, 40]))
        self.b4 = tf.Variable(tf.zeros([40]))
        self.L4 = tf.nn.relu(tf.add(tf.matmul(self.L3, self.W4), self.b4))

        self.W5 = tf.Variable(tf.random_normal([40, 15]))
        self.b5 = tf.Variable(tf.zeros([15]))
        self.L5 = tf.nn.relu(tf.add(tf.matmul(self.L4, self.W5), self.b5))

        self.W6 = tf.Variable(tf.random_normal([15, 7]))
        self.b6 = tf.Variable(tf.zeros([7]))
        self.model = tf.add(tf.matmul(self.L5, self.W6), self.b6)

        self.cost = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits_v2(labels=self.Y, logits=self.model))
        
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        self.train_op = self.optimizer.minimize(self.cost)


    def TRAIN(self, x_data, y_data, iter):
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)
    
        for step in range(iter):
            self.sess.run(self.train_op, feed_dict={self.X: x_data, self.Y: y_data})   
    

    def PREDICT(self, x_data, y_data, p_data):
        self.TRAIN(x_data, y_data, 100)
        self.prediction = tf.argmax(self.model, 1)
        return self.sess.run(self.prediction, feed_dict={self.X: p_data})
        
        # is_correct = tf.equal(prediction, target)
        # accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
        # print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))
        self.sess.close()

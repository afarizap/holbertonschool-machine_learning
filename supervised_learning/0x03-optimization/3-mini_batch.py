#!/usr/bin/env python3
""" 3-mini_batch task """
import tensorflow as tf
shuffle_data = __import__('2-shuffle_data').shuffle_data


def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32,
                     epochs=5, load_path="/tmp/model.ckpt",
                     save_path="/tmp/model.ckpt"):
    """
    trains a loaded neural network model using mini-batch gradient descent:

    X_train: numpy.ndarray of shape (m, 784) containing the training data
        m: number of data points
        784: number of input features
    Y_train: one-hot numpy.ndarray of shape(m, 10) containing training labels
        10 is the number of classes the model should classify
    X_valid: numpy.ndarray of shape (m, 784) containing the validation data
    Y_valid: one-hot numpy.ndarray of shape(m, 10) containing validat labels
    batch_size: number of data points in a batch
    epochs: number of times the training should pass through the dataset
    load_path: path from which to load the model
    save_path: path to where the model should be saved after training
    Returns: path where the model was saved
    """
    saver = tf.train.import_meta_graph(load_path + ".meta")
    saver.restore(sess, load_path)
    x = tf.get_collection("x")[0]
    y = tf.get_collection("y")[0]
    loss = tf.get_collection("loss")[0]
    accuracy = tf.get_collection("accuracy")[0]
    train_op = tf.get_collection("train_op")[0]

    for epoch in range(epochs + 1):
        cost_t = sess.run(loss, feed_dict={x: X_train, y: Y_train})
        accu_t = sess.run(accuracy, feed_dict={x: X_train, y: Y_train})
        cost_val = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
        accu_val = sess.run(accuracy, feed_dict={x: X_valid, y: Y_valid})
        print("After {} epochs:".format(epoch))
        print("\tTraining Cost: {}".format(cost_t))
        print("\tTraining Accuracy: {}".format(accu_t))
        print("\tValidation Cost: {}".format(cost_val))
        print("\tValidation Accuracy: {}".format(accu_val))

        if epoch < epochs:

            X_train_s, Y_train_s = shuffle_data(X_train, Y_train)

            # MINI BATCH training:
            m = X_train.shape[0]
            for start in range(0, m, batch_size):
                if (start + batch_size) < m:
                    X_train_m = X_train_s[start: start + batch_size]
                    Y_train_m = Y_train_s[start: start + batch_size]
                else:
                    X_train_m = X_train_s[start: m]
                    Y_train_m = Y_train_s[start: m]

                sess.run(train_op, {x: X_train_m, y: Y_train_m})

                if start != 0 and (start / batch_size + 1) % 100 == 0:
                    cost_mini = sess.run(loss,
                                            feed_dict={x: X_train_m,
                                                    y: Y_train_m})
                    accu_mini = sess.run(accuracy,
                                            feed_dict={x: X_train_m,
                                                    y: Y_train_m})
                    print("\tStep {}:".format(int(start / batch_size + 1)))
                    print("\t\tCost: {}".format(cost_mini))
                    print("\t\tAccuracy: {}".format(accu_mini))

    return saver.save(sess, save_path)

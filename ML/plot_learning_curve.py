from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt



def plot_learning_curve(model,X,y):
    m,train,val = learning_curve(model,X,y)

    plt.plot(m, train.mean(1), label='train')
    plt.plot(m, val.mean(1), label='val')
    plt.title('Learning Curve')
    plt.legend()
    plt.xlabel('m')
    plt.ylabel('score')
    plt.show()



from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt



def plot_learning_curve(model,X,y):
    m,train,val = learning_curve(model,X,y)
    model_name = str(model.named_steps['model']).split("(")[0]
    plt.plot(m, train.mean(1), label='train')
    plt.plot(m, val.mean(1), label='val')
    plt.title(f'{model_name} Learning Curve')
    plt.legend()
    plt.xlabel('m')
    plt.ylabel('score')
    plt.savefig('learning_curve.png')



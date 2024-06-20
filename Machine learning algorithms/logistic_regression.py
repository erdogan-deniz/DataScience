import numpy
import pandas
import numpy as np
from typing import Union
import pandas as pd

EPS = 1e-15


def sigmoid(x):
    res = numpy.exp(-x)
    tmp = 1 / (1 + res)

    return tmp

# def calc_pos(arra):
#     tmp =
#
#     for i in range(len(arra)):


def converter(x):
    return x >= 0.5

class MyLogReg:
    """
    --------------------------------------------------------------------------------------------------------------------
    Class description: Logistic regression class.
    --------------------------------------------------------------------------------------------------------------------
    Attributes:
        __n_iter:
            Description: A count of gradient iterations.
            Type: int.
            Necessity: Optional.
            Default value: 10.

        __weights:
            Description: An array of model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.

        __learning_rate:
            Description: A multiplier of gradient step.
            Type: float.
            Necessity: Optional.
            Default value: 0.1.
    --------------------------------------------------------------------------------------------------------------------
    Methods:
        get_coef:
            Description: The method is used to get the latest weights of the trained model.
            Returns: Weights of a fitting model.
            Return type: Union[numpy.array, None].

        fit:
            Description: The method trains the model by finding the best weights.
            Parameters: x - samples of data, y - targets of data, verbose - logging flag.
            Parameters type: pandas.Dataframe, pandas.Series, Union[int, bool].
            Return type: None.

        logging:
            Description: Prints loss values every n steps.
            Parameters: step - the number of the step, loss_value - the value of loss,
                        verbose - the flag of logging.
            Parameters type: int, float, Union[int, bool].
            Return type: None.
    --------------------------------------------------------------------------------------------------------------------
    Magic methods:
        __init__:
            Description: The method initializes the fields of the class.
            Parameters: n_iter - a count of gradient iterations, learning_rate - a multiplier of gradient step.
            Parameters type: int, float.
            Return type: None.

        __repl__:
            Description: The method describes the object in an official form.
            Returns: An official format string.
            Return type: str.

        __str__:
            Description: The method describes the object in a human-friendly format.
            Returns: A convenient format string.
            Return type: str.
    --------------------------------------------------------------------------------------------------------------------
    """

    def __repr__(self) -> str:
        """
        The method describes the object in an official form.

        :return: An official format string.
        """

        return """
    --------------------------------------------------------------------------------------------------------------------
    Class description: Logistic regression class.
    --------------------------------------------------------------------------------------------------------------------
    Attributes:
        __n_iter:
            Description: A count of gradient iterations.
            Type: int.
            Necessity: Optional.
            Default value: 10.

        __weights:
            Description: An array of model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.

        __learning_rate:
            Description: A multiplier of gradient step.
            Type: float.
            Necessity: Optional.
            Default value: 0.1.
    --------------------------------------------------------------------------------------------------------------------
    Methods:
        get_coef:
            Description: The method is used to get the latest weights of the trained model.
            Returns: Weights of a fitting model.
            Return type: Union[numpy.array, None].

        fit:
            Description: The method trains the model by finding the best weights.
            Parameters: x - samples of data, y - targets of data, verbose - logging flag.
            Parameters type: pandas.Dataframe, pandas.Series, Union[int, bool].
            Return type: None.

        logging:
            Description: Prints loss values every n steps.
            Parameters: step - the number of the step, loss_value - the value of loss, 
                        verbose - the flag of logging.
            Parameters type: int, float, Union[int, bool].
            Return type: None.
    --------------------------------------------------------------------------------------------------------------------
    Magic methods:
        __init__:
            Description: The method initializes the fields of the class.
            Parameters: n_iter - a count of gradient iterations, learning_rate - a multiplier of gradient step.
            Parameters type: int, float.
            Return type: None.

        __repl__:
            Description: The method describes the object in an official form.
            Returns: An official format string.
            Return type: str.

        __str__:
            Description: The method describes the object in a human-friendly format.
            Returns: A convenient format string.
            Return type: str.
    --------------------------------------------------------------------------------------------------------------------
    """

    def __str__(self) -> str:
        """
        The method describes the object in a human-friendly format.

        :return: A convenient format string.
        """

        return f"MyLogReg class: n_iter={self.__n_iter}, learning_rate={self.__learning_rate}"

    def __init__(self, n_iter: int = 10, learning_rate: float = 0.1, metric: str = None) -> None:
        """
        The method initializes the fields of the class.

        :param n_iter: A count of gradient iterations.
        :param learning_rate: A multiplier of gradient step.
        """

        self.__metric = metric

        self.__weights: Union[numpy.array, None] = None

        self.__best_score = None

        # Set n_iter value:
        if 5 <= n_iter <= 2500:
            self.__n_iter: int = n_iter
        else:
            raise "Error! Incorrect n_iter argument value."

        # Set learning rate value:
        if 0.00001 <= learning_rate <= 100:
            self.__learning_rate: float = learning_rate
        else:
            raise "Error! Incorrect learning_rate argument value."

    def fit(self, x: pandas.DataFrame, y: pandas.Series, verbose: Union[int, bool] = False) -> None:
        """
        The method trains the model by finding the best weights.

        :param y: A target variable.
        :param verbose: A logging flag.
        :param x: Features for fitting.
        :return: None.
        """

        # Add the bias column:
        x.insert(0, "w0", 1.0)
        self.__weights = numpy.ones(x.shape[1])

        for step in range(1, self.__n_iter + 1):
            # Predict y:
            calculated_y: numpy.array = x @ self.__weights

            # Convert to probability of model confidence:
            converted_y: numpy.array = 1 / (1 + numpy.e ** (-calculated_y))

            # Calculate loss value:
            loss_value: float = -1 * numpy.mean((y * numpy.log(converted_y + EPS) +
                                                 (1 - y) * numpy.log(1 - converted_y + EPS)))

            # Calculate gradient of loss function:
            gradient: numpy.array = (converted_y - y) @ x / len(y)

            # Update model weights:
            self.__weights -= gradient * self.__learning_rate

            # Print log (if verbose is True):
            self.logging(step=step, loss_value=loss_value, verbose=verbose)

        self.__best_score = self.calc_metric(y, self.predict_proba(x))

    def predict(self, x: pandas.DataFrame):

        res = converter(self.predict_proba(x))

        return res.astype(int)

    def predict_proba(self, x: pandas.DataFrame):

        if "w0" not in x.columns:
            x.insert(0, "w0", 1.0)

        return sigmoid(numpy.array(x @ self.__weights))

    def get_coef(self) -> Union[numpy.array, None]:
        """
        The method is used to get the latest weights of the trained model.

        :return: Weights of a fitting model.
        """

        return self.__weights[1:]

    def get_best_score(self):
        return self.__best_score


    def calc_metric(self, y, reg_y):
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        pred_y = sigmoid(reg_y)

        for i in range(len(y)):
            if (y[i] == pred_y[i]) and (y[i] == 1):
                tp += 1
            elif (y[i] == pred_y[i]) and (y[i] == 0):
                tn +=1
            elif (y[i] != pred_y[i]) and (y[i] == 0):
                fp +=1
            else:
                fn += 1

        if self.__metric == "accuracy":
            return (tp + tn) / (tp + tn + fp + fn)
        elif self.__metric == "precision":
            return tp / (tp + fp)
        elif self.__metric == "recall":
            return tp / (tp + fn)
        elif self.__metric == "f1":
            return 2 * (tp / (tp + fp)) * (tp / (tp + fn)) / (tp / (tp + fn) + tp / (tp + fp))
        elif self.__metric == "roc_auc":
            dataset = pd.DataFrame({'pred_y': list(pred_y), 'y': y,}, columns=['pred_y', 'y'])
            dataset.sort_values(by='pred_y', ascending=False, inplace=True)
            dataset["res1"] = dataset[dataset["y"] == 0].cumsum()
            # mini = dataset[dataset["y"] == 1]
            # dataset["res2"] = mini.count(dataset["pred_y"])
            pass
        else:
            return None

    @staticmethod
    def logging(step: int, loss_value: float, verbose: Union[int, bool] = False) -> None:
        """
        Prints loss values every n steps.

        :param step: The step size.
        :param verbose: A flag of logging.
        :param loss_value: The current loss value.
        :return: None.
        """

        if verbose > 0:
            if step == 1:
                print(f"| STARTING LOSS VALUE IS: {loss_value} |")
            elif not (step % verbose):
                print(f"| STEP № {step}: LOSS VALUE IS{loss_value} |")

df2 = pandas.DataFrame(numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 2, 8]]),
                   columns=['a', 'b', 'c'])

model = MyLogReg(metric="roc_auc")

model.fit(df2, pandas.Series([1, 0, 0, 1]))

zxc = model.predict(df2)

w = model.calc_metric(zxc, pandas.Series([1, 0, 1, 0]))

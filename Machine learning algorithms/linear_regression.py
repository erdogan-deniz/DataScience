import numpy
import pandas
import random

from typing import Union, Callable


class LinearRegression:
    """
    --------------------------------------------------------------------------------------------------------------------
    Class description: Linear regression class.
    --------------------------------------------------------------------------------------------------------------------
    Attributes:
        __reg:
            Description: A type of regularization.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __best_score:
            Description: The best metric score.
            Type: Union[float, None].
            Necessity: Unavailable.
            Default value: None.

        __metric:
            Description: A metric for testing model.
            Type: str.
            Necessity: Optional.
            Default value: "mse".

        __n_iter:
            Description: A count of gradient iterations.
            Type: int.
            Necessity: Optional.
            Default value: 100.

        __weights:
            Description: An array of model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.

        __l1_coef:
            Description: A coefficient of l1 regularization.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __l2_coef:
            Description: A coefficient of l2 regularization.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __random_state:
            Description: A fixed seed of taking samples.
            Type: int.
            Necessity: Optional.
            Default value: 42.

        __sgd_sample:
            Description: A count (%) of samples used in model fitting.
            Type: Union[int, float, None].
            Necessity: Optional.
            Default value: None.

        __learning_rate:
            Description: A multiplier of gradient step (can be lambda function).
            Type: Union[float, Callable].
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

        calculate_metric:
            Description: The method calculates the required metric.
            Parameters: calculated_y - predicted target variables, y - the actual values of the target variable,
                        metric - the name of the metric to be calculated.
            Parameters type: pandas.Series, pandas.Series, str.
            Returns: The value of the selected metric.
            Return type: float.

        get_best_score:
            Description: Returns the best value of the set metric.
            Returns: The value of the required metric.
            Return type: Union[float, None].

        logging:
            Description: Prints loss and metric values every n steps.
            Parameters: step - the number of the step, loss_value - the value of loss,
                        metric_value - the value of metric, verbose - the flag of logging.
            Parameters type: int, float, float, Union[int, bool].
            Return type: None.

        predict:
            Description: The method predicts target values based on samples.
            Parameters: samples - the data that the forecast is based on.
            Parameters type: pandas.DataFrame.
            Returns: Predicted target variables.
            Return type: numpy.array.

        calculate_loss_regularization:
            Description: The method calculates the loss regularization for a linear model.
            Returns: The value of regularization for loss.
            Return type: float.

        calculate_gradient_regularization:
            Description: The method calculates the regularization gradient for a linear model.
            Returns: The value of regularization for the gradient.
            Return type: Union[float, numpy.array].
    --------------------------------------------------------------------------------------------------------------------
    Magic methods:
        __init__:
            Description: The method initializes the fields of the class.
            Parameters: n_iter - a count of gradient iterations, learning_rate - a multiplier of gradient step (can be
                        lambda function), metric - a metric for testing model, reg - a type of regularization, l1_coef -
                        a coefficient of l1 regularization, l2_coef - a coefficient of l2 regularization, sgd_sample -
                        a count (%) of samples used in model fitting, random_state - a fixed seed of taking samples.
            Parameters type: int, Union[float, Callable], str, Union[str, None], float, float, Union[int, float, None],
                             int.
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
    Typical use:
        model = MyLineReg(learning_rate=0.1, metric="mae", reg="l1", random_state=42)
        model.fit(x=x, y=y, verbose=True)
        predictions = model.predict(samples=samples)
    --------------------------------------------------------------------------------------------------------------------
    """

    def __repr__(self) -> str:
        """
        The method describes the object in an official form.

        :return: An official format string.
        """

        return """
    --------------------------------------------------------------------------------------------------------------------
    Class description: Linear regression class.
    --------------------------------------------------------------------------------------------------------------------
    Attributes:
        __reg:
            Description: A type of regularization.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __best_score:
            Description: The best metric score.
            Type: Union[float, None].
            Necessity: Unavailable.
            Default value: None.

        __metric:
            Description: A metric for testing model.
            Type: str.
            Necessity: Optional.
            Default value: "mse".

        __n_iter:
            Description: A count of gradient iterations.
            Type: int.
            Necessity: Optional.
            Default value: 100.

        __weights:
            Description: An array of model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.

        __l1_coef:
            Description: A coefficient of l1 regularization.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __l2_coef:
            Description: A coefficient of l2 regularization.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __random_state:
            Description: A fixed seed of taking samples.
            Type: int.
            Necessity: Optional.
            Default value: 42.

        __sgd_sample:
            Description: A count (%) of samples used in model fitting.
            Type: Union[int, float, None].
            Necessity: Optional.
            Default value: None.

        __learning_rate:
            Description: A multiplier of gradient step (can be lambda function).
            Type: Union[float, Callable].
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

        calculate_metric:
            Description: The method calculates the required metric.
            Parameters: calculated_y - predicted target variables, y - the actual values of the target variable,
                        metric - the name of the metric to be calculated.
            Parameters type: pandas.Series, pandas.Series, str.
            Returns: The value of the selected metric.
            Return type: float.

        get_best_score:
            Description: Returns the best value of the set metric.
            Returns: The value of the required metric.
            Return type: Union[float, None].

        logging:
            Description: Prints loss and metric values every n steps.
            Parameters: step - the number of the step, loss_value - the value of loss,
                        metric_value - the value of metric, verbose - the flag of logging.
            Parameters type: int, float, float, Union[int, bool].
            Return type: None.

        predict:
            Description: The method predicts target values based on samples.
            Parameters: samples - the data that the forecast is based on.
            Parameters type: pandas.DataFrame.
            Returns: Predicted target variables.
            Return type: numpy.array.

        calculate_loss_regularization:
            Description: The method calculates the loss regularization for a linear model.
            Returns: The value of regularization for loss.
            Return type: float.

        calculate_gradient_regularization:
            Description: The method calculates the regularization gradient for a linear model.
            Returns: The value of regularization for the gradient.
            Return type: Union[float, numpy.array].
    --------------------------------------------------------------------------------------------------------------------
    Magic methods:
        __init__:
            Description: The method initializes the fields of the class.
            Parameters: n_iter - a count of gradient iterations, learning_rate - a multiplier of gradient step (can be
                        lambda function), metric - a metric for testing model, reg - a type of regularization, l1_coef -
                        a coefficient of l1 regularization, l2_coef - a coefficient of l2 regularization, sgd_sample -
                        a count (%) of samples used in model fitting, random_state - a fixed seed of taking samples.
            Parameters type: int, Union[float, Callable], str, Union[str, None], float, float, Union[int, float, None],
                             int.
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
    Typical use:
        model = MyLineReg(learning_rate=0.1, metric="mae", reg="l1", random_state=42)
        model.fit(x=x, y=y, verbose=True)
        predictions = model.predict(samples=samples)
    --------------------------------------------------------------------------------------------------------------------
    """

    def __str__(self) -> str:
        """
        The method describes the object in a human-friendly format.

        :return: A convenient format string.
        """

        # Check reg for print:
        current_reg: str = f" reg={self.__reg}, " if self.__reg is not None else " "

        # Check sgd_samples for print:
        current_sgd: str = f" sgd_sample={self.__sgd_sample}, " if self.__sgd_sample is not None else " "

        return (f"MyLineReg class: n_iter={self.__n_iter}, learning_rate={self.__learning_rate}, " +
                f"metric={self.__metric,}," + current_reg + f"l1_coef={self.__l1_coef}, l2_coef={self.__l2_coef}," +
                current_sgd + f"random_state={self.__random_state}.")

    def __init__(self, n_iter: int = 100, learning_rate: Union[float, Callable] = 0.1, metric: str = "mse",
                 reg: Union[str, None] = None, l1_coef: float = 0, l2_coef: float = 0,
                 sgd_sample: Union[int, float, None] = None, random_state: int = 42) -> None:
        """
        The method initializes the fields of the class.
        
        :param n_iter: A count of gradient iterations.
        :param learning_rate: A multiplier of gradient step (can be lambda function).
        :param metric: A metric for testing model.
        :param reg: A type of regularization.
        :param l1_coef: A coefficient of l1 regularization.
        :param l2_coef: A coefficient of l2 regularization.
        :param sgd_sample: A count (%) of samples used in model fitting.
        :param random_state: A fixed seed of taking samples.
        """

        self.__best_score: Union[float, None] = None
        self.__weights: Union[numpy.array, None] = None

        # Set n_iter value:
        if 5 <= n_iter <= 2500:
            self.__n_iter: int = n_iter
        else:
            raise "Error! Incorrect n_iter argument value."

        # Set learning rate value:
        if not callable(learning_rate):
            # Case with float value:
            if 0.00001 <= learning_rate <= 100:
                self.__learning_rate: Union[float, Callable] = learning_rate
            else:
                raise "Error! Incorrect learning_rate argument value."
        else:
            # Case with lamda function:
            self.__learning_rate: Union[float, Callable] = learning_rate

        # Set l1_coef value:
        if 0 <= l1_coef <= 1:
            self.__l1_coef: float = l1_coef
        else:
            raise "Error! Incorrect l1_coef argument value."

        # Set l2_coef value:
        if 0 <= l2_coef <= 1:
            self.__l2_coef: float = l2_coef
        else:
            raise "Error! Incorrect l2_coef argument value."

        # Set random state:
        if 1 <= random_state <= 100:
            self.__random_state: int = random_state
        else:
            raise "Error! Incorrect random_state argument value."

        # Set sgd_sample:
        if isinstance(sgd_sample, int):
            if sgd_sample <= 0:
                raise "Error! Incorrect sgd_sample argument value."
            else:
                self.__sgd_sample: Union[int, float, None] = sgd_sample
        elif isinstance(sgd_sample, float):
            if (sgd_sample > 1) or (sgd_sample < 0):
                raise "Error! Incorrect sgd_sample argument value."
            else:
                self.__sgd_sample: Union[int, float, None] = sgd_sample
        else:
            self.__sgd_sample: Union[int, float, None] = None

        # Set regularization type:
        self.__reg: Union[str, None] = reg if reg in ["l1", "l2", "elasticnet"] else None

        # Set metric type (use MSE as a default metric):
        self.__metric: str = "mse" if (metric not in ["r2", "mae", "rmse", "mape"]) else metric

    @staticmethod
    def calculate_metric(calculated_y: pandas.Series, y: pandas.Series, metric: str) -> float:
        """
        The method calculates the required metric.

        :param y: The actual values of the target variable.
        :param metric: The name of the metric to be calculated.
        :param calculated_y: Predicted target variables.
        :return: The value of the selected metric.
        """

        if metric == "mae":
            return numpy.mean(abs(calculated_y - y))
        elif metric == "rmse":
            return numpy.mean((calculated_y - y) ** 2) ** 0.5
        elif metric == "r2":
            sst: float = ((y - numpy.mean(y)) ** 2).sum()
            ssr: float = ((y - calculated_y) ** 2).sum()

            return 1 - ssr / sst
        elif metric == "mape":
            return numpy.sum(abs((y - calculated_y) / y)) * 100 / len(y)
        else:
            return numpy.mean((calculated_y - y) ** 2)

    def get_coef(self) -> Union[numpy.array, None]:
        """
        The method is used to get the latest weights of the trained model.

        :return: Weights of a fitting model.
        """

        return self.__weights[1:]

    def get_best_score(self) -> Union[float, None]:
        """
        Returns the best value of the set metric.

        :return: The value of the required metric.
        """

        return self.__best_score

    def fit(self, x: pandas.DataFrame, y: pandas.Series, verbose: Union[int, bool] = False) -> None:
        """
        The method trains the model by finding the best weights.

        :param y: A target variable.
        :param verbose: A logging flag.
        :param x: Features (matrix of samples) for fitting.
        :return: None.
        """

        # Add the bias column:
        x.insert(0, "w0", 1.0)
        self.__weights = numpy.ones(x.shape[1])

        # Fixing seed:
        random.seed(self.__random_state)

        for step in range(1, self.__n_iter + 1):
            # Define used samples rows:
            if isinstance(self.__sgd_sample, int):
                used_samples_rows: list = random.sample(range(x.shape[0]), self.__sgd_sample)
            elif isinstance(self.__sgd_sample, float):
                used_samples_rows: list = random.sample(range(x.shape[0]), round(self.__sgd_sample * x.shape[0]))
            else:
                used_samples_rows: list = random.sample(range(x.shape[0]), x.shape[0])

            # Samples and targets are used for fitting:
            used_samples = x.iloc[used_samples_rows]
            used_targets = y.iloc[used_samples_rows]

            # Predict y:
            calculated_y: numpy.array = used_samples @ self.__weights

            # Calculate loss value:
            loss_value: float = numpy.mean((((x @ self.__weights) - y) ** 2)) + self.calculate_loss_regularization()

            # Calculate model metric:
            metric_value: float = self.calculate_metric(calculated_y=pandas.Series(x @ self.__weights), y=y,
                                                        metric=self.__metric)

            # Calculate gradient of loss function:
            gradient: numpy.array = ((2 / len(used_targets)) * (calculated_y - used_targets) @ used_samples +
                                     self.calculate_gradient_regularization())

            # Update model weights:
            self.__weights -= gradient * self.__learning_rate if not callable(self.__learning_rate) \
                else gradient * self.__learning_rate(step)

            # Print log (if verbose is True):
            self.logging(step=step, loss_value=loss_value, metric_value=metric_value, verbose=verbose)

        # Save the best metric score:
        self.__best_score = self.calculate_metric(calculated_y=used_samples @ self.__weights, y=used_targets,
                                                  metric=self.__metric)

    def predict(self, samples: pandas.DataFrame) -> numpy.array:
        """
        The method predicts target values based on samples.

        :param samples: The data that the forecast is based on.
        :return: Predicted target variables.
        """

        # Adding the bias column:
        samples.insert(0, "w0", 1)

        # Make predictions:
        return samples @ self.__weights

    def calculate_loss_regularization(self) -> float:
        """
        The method calculates the loss regularization for a linear model.

        :return: The value of regularization for loss.
        """

        # Calculate losses:
        l1_loss: float = self.__l1_coef * (abs(self.__weights).sum())
        l2_loss: float = self.__l2_coef * ((self.__weights ** 2).sum())

        if self.__reg == "l1":
            return l1_loss
        elif self.__reg == "l2":
            return l2_loss
        elif self.__reg == "elasticnet":
            return l1_loss + l2_loss
        else:
            return 0

    def calculate_gradient_regularization(self) -> Union[float, numpy.array]:
        """
        The method calculates the regularization gradient for a linear model.

        :return: The value of regularization for the gradient.
        """

        # Calculate losses:
        l1_loss: numpy.array = self.__l1_coef * (numpy.sign(self.__weights))
        l2_loss: numpy.array = self.__l2_coef * 2 * self.__weights

        if self.__reg == "l1":
            return l1_loss
        elif self.__reg == "l2":
            return l2_loss
        elif self.__reg == "elasticnet":
            return l1_loss + l2_loss
        else:
            return 0

    def logging(self, step: int, loss_value: float, metric_value: float, verbose: Union[int, bool] = False) -> None:
        """
        Prints loss and metric values every n steps.

        :param step: The step size.
        :param verbose: A flag of logging.
        :param loss_value: The current loss value.
        :param metric_value: The actual metric value.
        :return: None.
        """

        if verbose > 0:
            if step == 1:
                print(f"| STARTING LOSS IS: {loss_value} | {self.__metric}: {metric_value}")
            elif not (step % verbose):
                print(f"| {step}: {loss_value} | {self.__metric}: {metric_value}")


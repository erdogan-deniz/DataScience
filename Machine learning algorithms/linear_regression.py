from typing import Union, Callable

import numpy
import pandas
import random


class LinearRegression:
    """
------------------------------------------------------------------------------------------------------------------------
    Class description: A linear regression class.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        __best_score:
            Description: The best metric score.
            Type: Union[float, None].
            Necessity: Unavailable.
            Default value: None.

        __l1_coef:
            Description: A l1 regularization coefficient.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __l2_coef:
            Description: A l2 regularization coefficient.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __learn_rate:
            Description: A gradient multiplier of the step (can be lambda function).
            Type: Union[float, Callable].
            Necessity: Optional.
            Default value: 0.1.

        __loss_type:
            Description: A model loss function.
            Type: str.
            Necessity: Optional.
            Default value: "mse".

        __metric_type:
            Description: A model metric.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __num_iter:
            Description: A number of gradient epochs.
            Type: int.
            Necessity: Optional.
            Default value: 100.

        __rand_state:
            Description: A fixed seed of taking samples.
            Type: int.
            Necessity: Optional.
            Default value: 1.

        __reg_type:
            Description: A regularization type.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __sgd_samples:
            Description: A number (%) of samples used in model fitting.
            Type: Union[int, float, None].
            Necessity: Optional.
            Default value: None.

        __weights:
            Description: A model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.
------------------------------------------------------------------------------------------------------------------------
    Methods:
------------------------------------------------------------------------------------------------------------------------
        calc_grad:
            Description: The method calculates a gradient.
            Parameters: x - samples,
                        y - true targets,
                        pred_y - predicted targets.
            Parameters type: pandas.Dataframe,
                             numpy.array,
                             numpy.array.
            Returns: A gradient.
            Return type: numpy.array.

        calc_grad_reg:
            Description: The method calculates a regularization gradient.
            Returns: The value of regularization for the gradient.
            Return type: Union[float, numpy.array].

        calс_loss:
            Description: The method calculates a loss value.
            Parameters: x - samples,
                        y - true targets.
            Parameters type: pandas.Dataframe,
                             numpy.array.
            Returns: A loss value.
            Return type: float.

        calс_loss_reg:
            Description: The method calculates the loss of regularization.
            Returns: A regularization loss value.
            Return type: float.

        fit:
            Description: The method fits the model by samples.
            Parameters: x - samples,
                        y - targets,
                        log_flag - a flag of logging.
            Parameters type: pandas.Dataframe,
                             pandas.Series,
                             Union[int, bool].
            Return type: None.

        get_score:
            Description: The method returns the last metric value.
            Returns: The last metric value.
            Return type: Union[float, None].

        get_weights:
            Description: The method returns the last model weights.
            Returns: The last model weights.
            Return type: Union[numpy.array, None].

        predict:
            Description: The method predicts target values based on samples.
            Parameters: x - samples.
            Parameters type: pandas.DataFrame.
            Returns: A predicted target variables.
            Return type: Union[numpy.array, None].

        reporting:
            Description: The method prints loss and metric values every n epoch.
            Parameters: num_epoch - an epoch number,
                        loss_value - the current loss value,
                        metric_value - the actual metric value,
                        log_flag - a flag of logging.
            Parameters type: int,
                             float,
                             Union[float, None],
                             Union[int, bool].
            Return type: None.

        sgd_select:
            Description: The method randomly selects indexes of samples based on a seed.
            Parameters: sample_count - a count of samples.
            Parameters type: int.
            Return type: list.

        update_weights:
            Description: The method updates model weights.
            Parameters: grad - a gradient of the loss function,
                        num_epoch - an epoch number.
            Parameters type: numpy.array,
                             int.
            Return type: None.
------------------------------------------------------------------------------------------------------------------------
    Magic methods:
------------------------------------------------------------------------------------------------------------------------
        __init__:
            Description: The method initializes class fields.
            Parameters: num_iter - a number of gradient epochs,
                        learn_rate - a gradient multiplier of the step (can be lambda function),
                        loss_type - a model loss function,
                        metric_type - a model metric,
                        reg_type - a regularization type,
                        l1_coef - a l1 regularization coefficient,
                        l2_coef - a l2 regularization coefficient,
                        sgd_samples - a number (%) of samples used in model fitting,
                        rand_state - a fixed seed of taking samples.
            Parameters type: int,
                             Union[float, Callable],
                             str,
                             Union[str, None],
                             Union[str, None],
                             float,
                             float,
                             Union[int, float, None],
                             int.
            Return type: None.

        __repl__:
            Description: The method describes the object in an official format.
            Returns: An official format string.
            Return type: str.

        __str__:
            Description: The method describes the object in a human-friendly format.
            Returns: A human-friendly format string.
            Return type: str.
------------------------------------------------------------------------------------------------------------------------
    Static methods:
------------------------------------------------------------------------------------------------------------------------
        calc_metric:
            Description: The method calculates the metric.
            Parameters: pred_y - predicted target variables,
                        y - real target variable,
                        metric_type - a metric name.
            Parameters type: numpy.array,
                             numpy.array,
                             Union[str, None].
            Returns: A selected metric value.
            Return type: Union[float, None]
------------------------------------------------------------------------------------------------------------------------
    Typical use:
------------------------------------------------------------------------------------------------------------------------
        model = MyLineReg(lear_rate=0.1, metric_type="mae", reg_type="l1")
        model.fit(x=x, y=y, log_flag=True)
        predictions = model.predict(x=x)
------------------------------------------------------------------------------------------------------------------------
    """

    def __init__(self, num_iter: int = 100, learn_rate: Union[float, Callable] = 0.1,
                 loss_type: str = "mse", metric_type: Union[str, None] = None,
                 reg_type: Union[str, None] = None, l1_coef: float = 0, l2_coef: float = 0,
                 sgd_samples: Union[int, float, None] = None, rand_state: int = 1) -> None:
        """
        The method initializes a class fields.

        :param num_iter: A number of gradient epochs.
        :param learn_rate: A gradient multiplier of the step (can be lambda function).
        :param loss_type: A model loss function.
        :param metric_type: A model metric.
        :param reg_type: A regularization type.
        :param l1_coef: A l1 regularization coefficient.
        :param l2_coef: A l2 regularization coefficient.
        :param sgd_samples: A number (%) of samples used in model fitting.
        :param rand_state: A fixed seed of taking samples.
        """

        self.__best_score: Union[float, None] = None
        self.__weights: Union[numpy.array, None] = None

        # Set num_iter value:
        if 5 <= num_iter <= 5000:
            self.__num_iter: int = num_iter
        else:
            raise "Error! Incorrect num_iter argument value."

        # Set learn_rate value:
        if not callable(learn_rate):
            # Case with float value:
            if 0.00001 <= learn_rate <= 100:
                self.__learn_rate: Union[float, Callable] = learn_rate
            else:
                raise "Error! Incorrect learn_rate argument value."
        else:
            # Case with lamda function:
            self.__learn_rate: Union[float, Callable] = learn_rate

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
        if 1 <= rand_state <= 100:
            self.__rand_state: int = rand_state
        else:
            raise "Error! Incorrect rand_state argument value."

        # Set sgd_samples:
        if isinstance(sgd_samples, int):
            if sgd_samples <= 0:
                raise "Error! Incorrect sgd_samples argument value."
            else:
                self.__sgd_samples: Union[int, float, None] = sgd_samples
        elif isinstance(sgd_samples, float):
            if (sgd_samples > 1) or (sgd_samples < 0):
                raise "Error! Incorrect sgd_samples argument value."
            else:
                self.__sgd_samples: Union[int, float, None] = sgd_samples
        else:
            self.__sgd_samples: Union[int, float, None] = None

        # Set loss_type value:
        self.__loss_type: str = loss_type if loss_type in ["mse"] else "mse"

        # Set reg_type value:
        self.__reg_type: Union[str, None] = reg_type if reg_type in ["l1", "l2", "elasticnet"] else None

        # Set metric_type value:
        self.__metric_type: Union[str, None] = metric_type \
            if metric_type in ["r2", "mae", "rmse", "mape", "mse"] else None

    def __repr__(self) -> str:
        """
        The method describes the object in an official format.

        :return: An official format string.
        """

        return """
------------------------------------------------------------------------------------------------------------------------
    Class description: A linear regression class.
------------------------------------------------------------------------------------------------------------------------
    Attributes:
------------------------------------------------------------------------------------------------------------------------
        __best_score:
            Description: The best metric score.
            Type: Union[float, None].
            Necessity: Unavailable.
            Default value: None.

        __l1_coef:
            Description: A l1 regularization coefficient.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __l2_coef:
            Description: A l2 regularization coefficient.
            Type: float.
            Necessity: Optional.
            Default value: 0.

        __learn_rate:
            Description: A gradient multiplier of the step (can be lambda function).
            Type: Union[float, Callable].
            Necessity: Optional.
            Default value: 0.1.

        __loss_type:
            Description: A model loss function.
            Type: str.
            Necessity: Optional.
            Default value: "mse".

        __metric_type:
            Description: A model metric.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __num_iter:
            Description: A number of gradient epochs.
            Type: int.
            Necessity: Optional.
            Default value: 100.

        __rand_state:
            Description: A fixed seed of taking samples.
            Type: int.
            Necessity: Optional.
            Default value: 1.

        __reg_type:
            Description: A regularization type.
            Type: Union[str, None].
            Necessity: Optional.
            Default value: None.

        __sgd_samples:
            Description: A number (%) of samples used in model fitting.
            Type: Union[int, float, None].
            Necessity: Optional.
            Default value: None.

        __weights:
            Description: A model weights.
            Type: Union[numpy.array, None].
            Necessity: Unavailable.
            Default value: None.
------------------------------------------------------------------------------------------------------------------------
    Methods:
------------------------------------------------------------------------------------------------------------------------
        calc_grad:
            Description: The method calculates a gradient.
            Parameters: x - samples,
                        y - true targets,
                        pred_y - predicted targets.
            Parameters type: pandas.Dataframe,
                             numpy.array,
                             numpy.array.
            Returns: A gradient.
            Return type: numpy.array.

        calc_grad_reg:
            Description: The method calculates a regularization gradient.
            Returns: The value of regularization for the gradient.
            Return type: Union[float, numpy.array].

        calс_loss:
            Description: The method calculates a loss value.
            Parameters: x - samples,
                        y - true targets.
            Parameters type: pandas.Dataframe,
                             numpy.array.
            Returns: A loss value.
            Return type: float.

        calс_loss_reg:
            Description: The method calculates the loss of regularization.
            Returns: A regularization loss value.
            Return type: float.

        fit:
            Description: The method fits the model by samples.
            Parameters: x - samples,
                        y - targets,
                        log_flag - a flag of logging.
            Parameters type: pandas.Dataframe,
                             pandas.Series,
                             Union[int, bool].
            Return type: None.

        get_score:
            Description: The method returns the last metric value.
            Returns: The last metric value.
            Return type: Union[float, None].

        get_weights:
            Description: The method returns the last model weights.
            Returns: The last model weights.
            Return type: Union[numpy.array, None].

        predict:
            Description: The method predicts target values based on samples.
            Parameters: x - samples.
            Parameters type: pandas.DataFrame.
            Returns: A predicted target variables.
            Return type: Union[numpy.array, None].

        reporting:
            Description: The method prints loss and metric values every n epoch.
            Parameters: num_epoch - an epoch number,
                        loss_value - the current loss value,
                        metric_value - the actual metric value,
                        log_flag - a flag of logging.
            Parameters type: int,
                             float,
                             Union[float, None],
                             Union[int, bool].
            Return type: None.

        sgd_select:
            Description: The method randomly selects indexes of samples based on a seed.
            Parameters: sample_count - a count of samples.
            Parameters type: int.
            Return type: list.

        update_weights:
            Description: The method updates model weights.
            Parameters: grad - a gradient of the loss function,
                        num_epoch - an epoch number.
            Parameters type: numpy.array,
                             int.
            Return type: None.
------------------------------------------------------------------------------------------------------------------------
    Magic methods:
------------------------------------------------------------------------------------------------------------------------
        __init__:
            Description: The method initializes class fields.
            Parameters: num_iter - a number of gradient epochs,
                        learn_rate - a gradient multiplier of the step (can be lambda function),
                        loss_type - a model loss function,
                        metric_type - a model metric,
                        reg_type - a regularization type,
                        l1_coef - a l1 regularization coefficient,
                        l2_coef - a l2 regularization coefficient,
                        sgd_samples - a number (%) of samples used in model fitting,
                        rand_state - a fixed seed of taking samples.
            Parameters type: int,
                             Union[float, Callable],
                             str,
                             Union[str, None],
                             Union[str, None],
                             float,
                             float,
                             Union[int, float, None],
                             int.
            Return type: None.

        __repl__:
            Description: The method describes the object in an official format.
            Returns: An official format string.
            Return type: str.

        __str__:
            Description: The method describes the object in a human-friendly format.
            Returns: A human-friendly format string.
            Return type: str.
------------------------------------------------------------------------------------------------------------------------
    Static methods:
------------------------------------------------------------------------------------------------------------------------
        calc_metric:
            Description: The method calculates the metric.
            Parameters: pred_y - predicted target variables,
                        y - real target variable,
                        metric_type - a metric name.
            Parameters type: numpy.array,
                             numpy.array,
                             Union[str, None].
            Returns: A selected metric value.
            Return type: Union[float, None]
------------------------------------------------------------------------------------------------------------------------
    Typical use:
------------------------------------------------------------------------------------------------------------------------
        model = MyLineReg(lear_rate=0.1, metric_type="mae", reg_type="l1")
        model.fit(x=x, y=y, log_flag=True)
        predictions = model.predict(x=x)
------------------------------------------------------------------------------------------------------------------------
"""

    def __str__(self) -> str:
        """
        The method describes the object in a human-friendly format.

        :return: A human-friendly format string.
        """

        # Check reg_type:
        cur_reg_type: str = f" reg_type={self.__reg_type}, " if self.__reg_type is not None else " "

        # Check sgd_samples:
        cur_sgd_samples: str = f" sgd_samples={self.__sgd_samples}, " if self.__sgd_samples is not None else " "

        # Check metric_type:
        cur_metric_type: str = f" metric_type={self.__metric_type}, " if self.__metric_type is not None else " "

        # Check loss_type:
        cur_loss_type: str = f" loss_type={self.__loss_type}, " if self.__loss_type is not None else " "

        return (f"Linear regression class: num_iter={self.__num_iter}, learn_rate={self.__learn_rate}, " +
                cur_loss_type + cur_metric_type + cur_reg_type + f"l1_coef={self.__l1_coef}, " +
                f"l2_coef={self.__l2_coef}," + cur_sgd_samples + f"rand_state={self.__rand_state}.")

    @staticmethod
    def calc_metric(pred_y: numpy.array, y: numpy.array, metric_type: Union[str, None]) -> Union[float, None]:
        """
        The method calculates the metric.

        :param pred_y: Predicted target variables.
        :param y: Real target variable.
        :param metric_type: A metric name.

        :return: A selected metric value.
        """

        if metric_type is not None:
            if metric_type == "mae":
                return numpy.mean(abs(pred_y - y))
            elif metric_type == "mape":
                return numpy.sum(abs((y - pred_y) / y)) * 100 / len(y)
            elif metric_type == "mse":
                return numpy.mean((pred_y - y) ** 2)
            elif metric_type == "rmse":
                return numpy.mean((pred_y - y) ** 2) ** 0.5
            elif metric_type == "r2":
                sst: float = ((y - numpy.mean(y)) ** 2).sum()
                ssr: float = ((y - pred_y) ** 2).sum()

                return 1 - (ssr / sst)
        else:
            return None

    def calc_grad(self, x: pandas.DataFrame, y: numpy.array, pred_y: numpy.array) -> numpy.array:
        """
        The method calculates a gradient.

        :param x: Samples.
        :param y: True targets.
        :param pred_y: Predicted targets.

        :return: A gradient.
        """

        if self.__loss_type == "mse":
            return 2 / len(y) * ((numpy.array(pred_y) - numpy.array(y)) @ x)

    def calc_grad_reg(self) -> Union[float, numpy.array]:
        """
        The method calculates a regularization gradient.

        :return: The value of regularization for the gradient.
        """

        # Calculate losses:
        l1_loss: numpy.array = self.__l1_coef * (numpy.sign(self.__weights))
        l2_loss: numpy.array = self.__l2_coef * 2 * self.__weights

        if self.__reg_type == "l1":
            return l1_loss
        elif self.__reg_type == "l2":
            return l2_loss
        elif self.__reg_type == "elasticnet":
            return l1_loss + l2_loss
        else:
            return 0

    def calc_loss(self, x: pandas.DataFrame, y: numpy.array) -> float:
        """
        The method calculates a loss value.

        :param x: Samples.
        :param y: True targets.

        :return: A loss value.
        """

        if self.__loss_type == "mse":
            return numpy.mean(((x @ self.__weights) - y) ** 2)

    def calc_loss_reg(self) -> float:
        """
        The method calculates the regularization of loss.

        :return: A regularization loss value.
        """

        # Calculate losses:
        l1_loss: float = self.__l1_coef * (abs(self.__weights).sum())
        l2_loss: float = self.__l2_coef * ((self.__weights ** 2).sum())

        if self.__reg_type == "l1":
            return l1_loss
        elif self.__reg_type == "l2":
            return l2_loss
        elif self.__reg_type == "elasticnet":
            return l1_loss + l2_loss
        else:
            return 0

    def fit(self, x: pandas.DataFrame, y: pandas.Series, log_flag: Union[int, bool] = False) -> None:
        """
        The method fits the model by samples.

        :param x: Samples.
        :param y: Targets.
        :param log_flag: Flag of logging.

        :return: None.
        """

        # Add the bias column:
        x.insert(0, "w0", 1.0)
        self.__weights = numpy.ones(x.shape[1])

        # Fixing seed:
        random.seed(self.__rand_state)

        for num_epoch in range(1, self.__num_iter + 1):
            # Define used samples rows:
            samples_ind: list = self.sgd_select(sample_count=x.shape[0])

            # Samples and targets are used for fitting:
            used_samples: pandas.DataFrame = x.iloc[samples_ind]
            used_targets: pandas.Series = y.iloc[samples_ind]

            # Predict y:
            pred_y: numpy.array = used_samples @ self.__weights

            # Calculate loss value:
            loss_value: float = self.calc_loss(x=x, y=y) + self.calc_loss_reg()

            # Calculate model metric:
            metric_value: Union[float, None] = self.calc_metric(pred_y=x @ self.__weights,
                                                                y=y, metric_type=self.__metric_type)

            # Calculate gradient of loss function:
            grad: numpy.array = (self.calc_grad(x=used_samples, y=used_targets, pred_y=pred_y) +
                                 self.calc_grad_reg())

            self.update_weights(grad=grad, num_epoch=num_epoch)

            # Print log (if verbose is True):
            self.reporting(num_epoch=num_epoch, loss_value=loss_value, metric_value=metric_value, log_flag=log_flag)

        # Save the best metric score:
        self.__best_score = self.calc_metric(pred_y=x @ self.__weights, y=y,
                                             metric_type=self.__metric_type)

    def get_score(self) -> Union[float, None]:
        """
        The method returns the last metric value.

        :return: The last metric value.
        """

        return self.__best_score

    def get_weights(self) -> Union[numpy.array, None]:
        """
        The method returns the last model weights.

        :return: The last model weights.
        """

        return self.__weights[1:] if self.__weights is not None else None

    def predict(self, x: pandas.DataFrame) -> Union[numpy.array, None]:
        """
        The method predicts target values based on samples.

        :param x: The samples.

        :return: Predicted target variables.
        """

        if self.__weights is not None:
            # Adding the bias column:
            x.insert(0, "w0", 1)

            # Make predictions:
            return x @ self.__weights
        else:
            return None

    def reporting(self, num_epoch: int, loss_value: float = 0, metric_value: Union[float, None] = 0,
                  log_flag: Union[int, bool] = False) -> None:
        """
        The method prints loss and metric values every n epoch.

        :param num_epoch: An epoch number.
        :param loss_value: The current loss value.
        :param metric_value: The actual metric value.
        :param log_flag: A flag of logging.

        :return: None.
        """

        # Check the epoch number:
        first_sent_part: str = f"| STARTING LOSS IS: {loss_value} |" if num_epoch == 1 \
            else f"| EPOCH № {num_epoch} HAS LOSS: {loss_value} |"

        # Check the metric value:
        second_sent_part: str = f" METRIC {self.__metric_type.upper()} IS: {metric_value}" \
            if self.__metric_type is not None else ""

        if log_flag > 0:
            if not (num_epoch % log_flag) or num_epoch == 1:
                print(first_sent_part + second_sent_part)

    def sgd_select(self, sample_count: int) -> list:
        """
        The method randomly selects indexes of samples based on a seed.

        :param sample_count: A count of samples.

        :return: Indexes of used samples.
        """

        if isinstance(self.__sgd_samples, int):
            return random.sample(range(sample_count), self.__sgd_samples)
        elif isinstance(self.__sgd_samples, float):
            return random.sample(range(sample_count), round(self.__sgd_samples * sample_count))
        else:
            return random.sample(range(sample_count), sample_count)

    def update_weights(self, grad: numpy.array, num_epoch: int) -> None:
        """
        The method updates model weights.

        :param grad: A gradient of the loss function.
        :param num_epoch: An epoch number.

        :return: None.
        """

        if self.__weights is not None:
            self.__weights = self.__weights - (grad * self.__learn_rate if not callable(self.__learn_rate)
                                               else grad * self.__learn_rate(num_epoch))

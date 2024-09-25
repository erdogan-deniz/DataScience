from src.auxiliary import *


def create_holiday_feature(df: pd.DataFrame, country_holidays: holidays.countries = rus_holidays) -> list:
    """"""

    return [dt in country_holidays for dt in df.index]


def create_time_dummie_feature(df: pd.DataFrame) -> range:
    """"""

    return range(1, df.shape[0] + 1)


def create_dayofweek_features(df: pd.DataFrame) -> pd.DataFrame:
    """"""

    categ_day_of_week = []
    numerical_days_of_week = df.index.dayofweek

    for day_of_week in numerical_days_of_week:
        if day_of_week == 0:
            categ_day_of_week.append("monday")
        elif day_of_week == 1:
            categ_day_of_week.append("tuesday")
        elif day_of_week == 2:
            categ_day_of_week.append("wednesday")
        elif day_of_week == 3:
            categ_day_of_week.append("thursday")
        elif day_of_week == 4:
            categ_day_of_week.append("friday")
        elif day_of_week == 5:
            categ_day_of_week.append("saturday")
        elif day_of_week == 6:
            categ_day_of_week.append("sunday")

    categ_day_of_week = pd.get_dummies(pd.Series(categ_day_of_week))
    categ_day_of_week.index = df.index
    categ_day_of_week[list(categ_day_of_week.columns)] = categ_day_of_week[list(categ_day_of_week.columns)].astype(int)

    return categ_day_of_week


def create_lag_feature(df: pd.DataFrame, feature_name: str, step_count: int) -> pd.Series:
    """"""

    return df[feature_name].shift(step_count)


def create_rolling_window_feature(df: pd.DataFrame, feature_name: str, stat_val: str, window_width: int) -> pd.Series:
    """"""

    if stat_val.lower() == "mean":
        return df[feature_name].rolling(window_width, center=False).mean()
    elif stat_val.lower() == "median":
        return df[feature_name].rolling(window_width, center=False).median()
    elif stat_val.lower() == "std":
        return df[feature_name].rolling(window_width, center=False).std()
    elif stat_val.lower() == "max":
        return df[feature_name].rolling(window_width, center=False).max()
    elif stat_val.lower() == "min":
        return df[feature_name].rolling(window_width, center=False).min()


def normalization(df: pd.Series, variable_name: str) -> pd.Series:
    """"""

    copy_df = df.copy()

    copy_df["std_normalization"] = create_rolling_window_feature(copy_df, variable_name, "std",
                                                                 get_average_months_length(copy_df, 2012, 2023) * 3
                                                                 ).shift(1)
    copy_df["mean_normalization"] = create_rolling_window_feature(copy_df, variable_name, "mean",
                                                                  get_average_months_length(copy_df, 2012, 2023) * 3
                                                                  ).shift(1)
    copy_df["normalized_peak_hour"] = (copy_df[variable_name] -
                                       copy_df["mean_normalization"]) / copy_df["std_normalization"]

    return copy_df


def denormalization(df: pd.Series, variable_name: str) -> pd.Series:
    """"""

    copy_df = df.copy()
    copy_df[variable_name] = \
        copy_df[f"normalized_{variable_name}"] * copy_df["std_normalization"] + copy_df["mean_normalization"]

    return copy_df

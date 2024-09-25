import pandas as pd

from os import listdir


def create_subj_df(files_path: str) -> pd.DataFrame:
    """"""

    dfs: list = []
    file_names: list = sorted(listdir(files_path))

    for file_name in file_names:
        if (file_name.split("_")[1] + '_' + file_name.split("_")[2]) > "2012_03":
            df: pd.DataFrame = pd.read_excel(files_path + file_name, names=["date", "peak_hour"])
            df["code_dpg"] = df.iloc[3][1]

            dfs.append(df.iloc[7:])

    df: pd.DataFrame = pd.concat(dfs, axis=0)
    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y")

    df.sort_values(by=["date", "code_dpg"])
    df.reset_index(drop=True, inplace=True)

    return df.copy()

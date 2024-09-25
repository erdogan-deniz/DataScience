import holidays

# Russian holidays:
rus_holidays: holidays.countries.russia.RU = holidays.country_holidays("RU")

# Data for parsing:
raw_data_path: str = "../data/raw/"

# Data for feature engineering:
processed_data_name: str = "/data.gzip"

processed_data_path: str = "../../../data/processed/"

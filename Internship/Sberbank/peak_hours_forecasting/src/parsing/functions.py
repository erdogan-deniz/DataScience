import requests
import datetime

from .data import *
from src.auxiliary import *
from requests import Response


def download_subj_peak_hours_data(
        subj_name: str,
        start_date: datetime,
        end_date: datetime,
        res_path: str = raw_data_path,
        main_url: str = peak_hour_url,
        request_headers=None
) -> None:
    """"""

    if request_headers is None:
        request_headers = peak_hour_request_headers
    for year in range(start_date.year, end_date.year + 1):
        for month in range(1, 13):
            for subj_ticket in peak_hour_subjs_tickets[subj_name]:
                if ((year == end_date.year) and (month < end_date.month)) or (year < end_date.year):
                    # Make request:
                    respon: Response = requests.get(f"{main_url}{year}{month:02d}_{subj_ticket}.xls", verify=False,
                                                    headers=request_headers)

                    if respon.status_code == 200:
                        try:
                            with open(
                                    f"{res_path}{subj_name}/Пиковые часы/{subj_name}_{year}_{month:02d}_" +
                                    f"{subj_ticket}.xls", "wb"
                            ) as respon_file:
                                respon_file.write(respon.content)
                        except Exception as err:
                            print(err, f"{res_path}{subj_name}/Пиковые часы/{subj_name}_{year}_{month:02d}_" +
                                  f"{subj_ticket}.xls")
                    else:
                        print(f"Can't get data from: {main_url}{year}{month:02d}_{subj_ticket}.xls")

    print(f"*** Subject {subj_name} has been downloaded ***")


def download_peak_hours_data(
        res_path: str = raw_data_path,
        main_url: str = peak_hour_url,
        subj_name: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
        request_headers=None
) -> None:
    """"""

    if request_headers is None:
        request_headers = peak_hour_request_headers
    if start_date is None:
        start_date = datetime.datetime(year=2012, month=1, day=1)

    if end_date is None:
        end_date = datetime.datetime.today()

    [download_subj_peak_hours_data(
        subj_name=subj_name,
        res_path=res_path,
        main_url=main_url,
        start_date=start_date,
        end_date=end_date,
        request_headers=request_headers
    ) for subj_name in peak_hour_subjs_tickets.keys()] if subj_name is None \
        else download_subj_peak_hours_data(
        subj_name=subj_name,
        res_path=res_path,
        main_url=main_url,
        start_date=start_date,
        end_date=end_date,
        request_headers=request_headers
    )

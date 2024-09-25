# Import main package:
from parsing import *

# Disable InsecureRequestWarnings:
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# The start point:
if __name__ == "__main__":
    download_peak_hours_data(subj_name="Чувашская Республика-Чувашия")

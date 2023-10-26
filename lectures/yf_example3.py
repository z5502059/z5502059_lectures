import os
from toolkit_config import cfg
import yf_example2
def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file.
    Parameters
    ----------
    year: int
        an integer with a four-digit year
    """
    tic = 'QAN.AX'
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31"'
    output_path = os.path.join(cfg.DATA_FOLDER, f'qan_prc{year}.csv')

    yf_example2.yf_prc_to_csv(start_date, end_date, 'QAN.AX', output_path)

if __name__ == "__main__":
    # Example: Download Qantas stock prices for the year 2020
    qan_prc_to_csv(year=2020)

# Goal is to check if this looping works in the StoveOptFiles repo
import os
import numpy as np
import iterative_case_check
from iterative_case_check import *

def main():

    cases_path, length_case_directory_list, case_directory_list = navigate_to_cases()

    reloc_dir, case_list_total, case_list_to_run, case_list_ran = count_cases_to_run(cases_path, length_case_directory_list, case_directory_list)

    # while loop for running the cases. Going one by one for now.


if __name__ == "__main__":
    main()

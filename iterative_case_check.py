# Navigate to the case directory

import os
import numpy as np

def navigate_to_cases():
    """Purpose is to navigate to the directory where case files exists

    Args:
        None

    Returns:
        case_path (str): full file path where directories exists
        length_case_directory_list (int): number of subdirectories within the cases path
    """
    current_dir = os.getcwd() # Get current directory
    dir_steps = "//foamfiles//counterFlowFlame2D//"
    cases_path = current_dir + dir_steps # full path with case folders
    case_directory_list = [directory for directory in os.listdir(cases_path) if os.path.isdir(cases_path)]
    length_case_directory_list = len(case_directory_list) # length of directory

    print("case directory length:")
    print("\n")
    print(case_directory_list)

    return cases_path, length_case_directory_list, case_directory_list

def count_cases_to_run(cases_path, length_case_directory_list, case_directory_list):
    """Purpose is to identify the number of cases to be run, and the name of the case path for run_surrounding_cases

    Args:
        case_path (str): full file path where directories exists

    Returns:
        num_cases (int): Number of cases needed to be run
        case_list_for_run (dictionary): list of strings corresponding to the full case paths to be run
    """

    os.chdir(cases_path)
    reloc_dir = os.getcwd() # testing where I am located
    print("Directory following the move to cases:")
    print("\n")
    print(reloc_dir)

    # Count directories beginning with "case_"--> return number, and append the case list TOTAL
    prefix = 'case' # look for case prefix
    i = 0 # for looping
    k = 0 # for case index
    cases_counter = 0 # number of case folders v_cases_total_vector
    cases_to_run_counter = 0 # number of cases that haven't been run
    case_list_total = [None] # empty vector for all cases
    while i < length_case_directory_list:
        if case_directory_list[i].startswith(prefix):
            print(case_directory_list[i])
            case_list_total.append(str(case_directory_list[i])) # The append step is the way to do it
            case_list_total[k] = case_directory_list[i]
            print("added entry for k =")
            print(k)
            print("added entry for i =")
            print(i)
            k = k + 1 # next entry of case list vector if filled
        i = i + 1 # Next dir

    # remove the final entry of the case_list_total vector
    case_list_total_length = len(case_list_total)
    print("case_list_total_length")
    print(case_list_total_length)
    omitted_case_value= case_list_total.pop(case_list_total_length-1)
    print("omitted value")
    print(omitted_case_value)
    print("Updated case list")
    print(case_list_total)
    edited_case_list_total_length = len(case_list_total) # for search and full path list
    print("edited case list length")
    print(edited_case_list_total_length)

    # Create full case paths (total)--superimpose the cases_path var to the cases in a looping
    case_list_paths_total = []
    full_case_path = [None]
    case_name = [None]
    p = 0 # looping INDEX
    while p < edited_case_list_total_length:
        case_name = case_list_total[p]
        print("case name within loop")
        print(case_name)
        #case_list_paths_total[p] = cases_path + case_name[p] #adding cases path to the cases iteratively
        case_list_paths_total.append(cases_path + case_name)
        print("case list paths total in loop")
        print(case_list_paths_total)
        print("p")
        print(p)
        p = p + 1
    print("full path list after loop")
    print(case_list_paths_total)

    # Figure out which cases have been run
    case_list_to_run = [] # empty vector of cases that HAVE NOT BEEN run
    case_list_ran = [] # empty vector for cases that have been run
    ran_ind = 0 # ran index
    to_run_index = 0 # to run index
    l = 0 # loop index for
    while l < len(case_list_paths_total):
        "Navigate to each directory and check if file beginning with ReactingFoamRunner exists"
        ran_prefix =  "ReactingFoamRunner_reactingFoam_serial_unlimited_runDir"
        os.chdir(case_list_paths_total[l]) # relocate to the indexed case path
        current_dir = os.getcwd()
        total_dir = current_dir + "//" + ran_prefix
        status = os.path.isdir(total_dir)
        if status == True:
            "The case has been ran"
            print("case has been run: ")
            print(case_list_paths_total[l])
            case_list_ran.append(case_list_paths_total[l]) # add to the to run array
        else:
            print("This case has not been run: ")
            print(case_list_paths_total[l])
            case_list_to_run.append(case_list_paths_total[l])
        l = l + 1

    print("case list to run:")
    print(case_list_to_run)
    print("case list ran")
    print(case_list_ran)
    return reloc_dir, case_list_total, case_list_to_run, case_list_ran


# WHILE LOOP CONTAINING THIS AND RUNNER.
# LOOP CONDITION IS THE NUM CASES, WHERE THE INDEX OPENS THE case_list_for_run ENTRY
# CURRENTLY SETUP FOR NON PARALLEL RUNS
def navigate_case_dictionary(case_list_for_run, num_cases):
    """Loop through the case directories, and run temporal_choice---runner should be within a loop with this function
    Args:
        num_cases (int): Number of cases needed to be run
        case_list_for_run (dictionary): list of strings corresponding to the full case paths to be run
    Returns:
        None
    """

# PROGRAMMER: Jennifer S.
# DATE CREATED: 05/14/2018
# REVISED DATE: 16/07/2024
# PURPOSE: This set of functions can be used to check your code after programming
# each function. The top section of each part of the lab contains
# the section labeled 'Checking your code'. When directed within this
# section of the lab one can use these functions to more easily check 
# your code. See the docstrings below each function for details on how
# to use the function within your code.

def check_command_line_arguments(in_arg):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments passed in as parameter in_arg, 
    assumes you defined all three command line arguments as outlined in 
    '7. Command Line Arguments'
    Parameters:
     in_arg - data structure that stores the command line arguments object
    Returns:
     Nothing - just prints to console  
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)


def check_creating_pet_image_labels(results_dic):
    """
    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints first 10 key-value pairs and makes sure there are 40 key-value 
    pairs in your results_dic dictionary.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
    Returns:
     Nothing - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:
        stop_point = min(len(results_dic), 10)
        print("\nPet Image Label Dictionary has", len(results_dic),
              "key-value pairs.\nBelow are", stop_point, "of them:")

        for n, key in enumerate(results_dic):
            if n < stop_point:
                print("{:2d} key: {:>30}  label: {:>26}".format(n+1, key,
                      results_dic[key][0]))


def check_classifying_images(results_dic):
    """
    For Lab: Classifying Images - 11/12. Classifying Images
    Prints Pet Image Label and Classifier Label for ALL Matches followed by ALL 
    NOT matches. Also prints total number of images.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)
    Returns:
     Nothing - just prints to console  
    """
    if results_dic is None or len(results_dic[next(iter(results_dic))]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    else:
        n_match = 0
        n_notmatch = 0

        print("\n     MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 1:
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key, 
                      results_dic[key][0], results_dic[key][1]))

        print("\n NOT A MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 0:
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}".format(key,
                      results_dic[key][0], results_dic[key][1]))

        print("\n# Total Images", n_match + n_notmatch, "# Matches:", n_match,
              "# NOT Matches:", n_notmatch)


def check_classifying_labels_as_dogs(results_dic):
    """
    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet Image Label, Classifier Label, whether Pet Label is-a-dog(1=Yes,
    0=No), and whether Classifier Label is-a-dog(1=Yes, 0=No) for ALL Matches 
    followed by ALL NOT matches.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)
                    idx 3 = 1/0 (int)
                    idx 4 = 1/0 (int)
    Returns:
     Nothing - just prints to console  
    """
    if results_dic is None or len(results_dic[next(iter(results_dic))]) < 4:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    else:
        n_match = 0
        n_notmatch = 0

        print("\n     MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 1:
                n_match += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n NOT A MATCH:")
        for key in results_dic:
            if results_dic[key][2] == 0:
                n_notmatch += 1
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      results_dic[key][0], results_dic[key][1], results_dic[key][3], 
                      results_dic[key][4]))

        print("\n# Total Images", n_match + n_notmatch, "# Matches:", n_match,
              "# NOT Matches:", n_notmatch)


def check_calculating_results(results_dic, results_stats_dic):
    """
    For Lab: Classifying Images - 14. Calculating Results
    Prints First statistics from the results stats dictionary, then prints 
    the same statistics that were calculated using the results dictionary.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)
                    idx 3 = 1/0 (int)
                    idx 4 = 1/0 (int)
     results_stats_dic - Dictionary that contains the results statistics
    Returns:
     Nothing - just prints to console  
    """
    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:
        n_images = len(results_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_match_breed = 0

        for key in results_dic:
            if results_dic[key][2] == 1:
                if results_dic[key][3] == 1:
                    n_pet_dog += 1
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                        n_match_breed += 1
                else:
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1
            else:
                if results_dic[key][3] == 1:
                    n_pet_dog += 1
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                else:
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1

        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = (n_class_cdog / n_pet_dog) * 100 if n_pet_dog > 0 else 0
        pct_corr_notdog = (n_class_cnotd / n_pet_notd) * 100 if n_pet_notd > 0 else 0
        pct_corr_breed = (n_match_breed / n_pet_dog) * 100 if n_pet_dog > 0 else 0

        print("\n ** Statistics from calculates_results_stats() function:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              results_stats_dic['n_images'], results_stats_dic['n_dogs_img'],
              results_stats_dic['n_notdogs_img'], results_stats_dic['pct_correct_dogs'],
              results_stats_dic['pct_correct_notdogs'],
              results_stats_dic['pct_correct_breed']))
        print("\n ** Check Statistics - calculated from this function as a check:")
        print("N Images: {:2d}  N Dog Images: {:2d}  N NotDog Images: {:2d} \nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              n_images, n_pet_dog, n_pet_notd, pct_corr_dog, pct_corr_notdog,
              pct_corr_breed))


if __name__ == "__main__":
    import argparse

    def get_input_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--dir', type=str, default='pet_images/', help='Path to the folder of pet images')
        parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
        parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File that contains dognames')
        return parser.parse_args()

    # Example usage of the check functions
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Example results dictionary for pet image labels
    results_dic = {
        'image_1.jpg': ['golden retriever'],
        'image_2.jpg': ['labrador retriever'],
        # ... (add more entries as needed)
    }
    check_creating_pet_image_labels(results_dic)

    # Example results dictionary for classified images
    results_dic = {
        'image_1.jpg': ['golden retriever', 'golden retriever', 1],
        'image_2.jpg': ['labrador retriever', 'beagle', 0],
        # ... (add more entries as needed)
    }
    check_classifying_images(results_dic)

    # Example results dictionary for classified labels as dogs
    results_dic = {
        'image_1.jpg': ['golden retriever', 'golden retriever', 1, 1, 1],
        'image_2.jpg': ['labrador retriever', 'beagle', 0, 1, 1],
        # ... (add more entries as needed)
    }
    check_classifying_labels_as_dogs(results_dic)

    # Example results statistics dictionary
    results_stats_dic = {
        'n_images': 40,
        'n_dogs_img': 30,
        'n_notdogs_img': 10,
        'pct_correct_dogs': 90.0,
        'pct_correct_notdogs': 80.0,
        'pct_correct_breed': 85.0,
    }
    check_calculating_results(results_dic, results_stats_dic)


# PROGRAMMER: Tanishi Tripathi
# DATE CREATED: 11/07/2024                                 
# REVISED DATE: 13/07/2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
import os

def get_pet_labels(image_dir):
    # Get list of files in the directory
    in_files = os.listdir(image_dir)
    
    # Create empty dictionary to hold results
    results = dict()
    
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            # Process the filenames to get pet labels
            pet_label = in_files[idx].lower().split("_")
            pet_name = ""
            for word in pet_label:
                if word.isalpha():
                    pet_name += word + " "
            pet_name = pet_name.strip()
            
            if in_files[idx] not in results:
                results[in_files[idx]] = [pet_name]
            else:
                print("Warning: Duplicate files exist in directory:", 
                      in_files[idx])
    return results

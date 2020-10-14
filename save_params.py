import json

# Reference: CS230
# https://github.com/cs230-stanford/cs230-code-examples/blob/master/pytorch/nlp/utils.py


def save_dict_to_json(dict_of_params, json_path):
    """Saves dict of floats in json file
    Args:
        d: (dict) of float-castable values (np.float, int, float, etc.)
        json_path: (string) path to json file
    Return:
        a saved json file containing hyperparameters
    """

    with open(json_path, 'w') as f:
        dict_of_params = {k: v for k, v in dict_of_params.items()}
        json.dump(dict_of_params, f, indent=4)

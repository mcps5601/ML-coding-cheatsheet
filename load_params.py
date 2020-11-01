import argparse, json

def load_params(path_of_params):
    parser = argparse.ArgumentParser()
    with open(path_of_params, 'r') as f:
        # create temporal args
        t_args = argparse.Namespace()
        t_args.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=t_args)

    return args
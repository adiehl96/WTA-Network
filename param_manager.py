__author__ = "Otto van der Himst"
__version__ = "1.0"
__email__ = "otto.vanderhimst@ru.nl"


def get_params_00(segment, n_experiments=10, seed_base=2022): # experiment 1
    
    params = []
    for i in range(n_experiments):
        params.append({"seed":seed_base+i})
    for i in range(n_experiments):
        params.append({"seed":seed_base+i, "tag_mnist_a":"-normal", "tag_mnist_b":"-normal"})
    return params

def get_params_01(segment, n_experiments=10, seed_base=2022): # experiment 2.1
    
    params = []
    if segment == 0 or segment == -1:
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1, 0, 1, 1)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(2, 0, 1, 2)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(3, 0, 1, 3)})
    if segment == 1 or segment == -1:
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.5, 0.3, 1.3, 3.0)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.75, 0.2, 1.1, 3.0)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.75, 0.4, 1.1, 3.0)})
    return params

def get_params_02(segment, n_experiments=10, seed_base=2022): # experiment 2.2
    
    params = []
    if segment == 0 or segment == -1:
        for i in range(n_experiments):
            params.append({"seed":seed_base+i})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1, 0, 1, 1)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(2, 0, 1, 2)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(3, 0, 1, 3)})
    if segment == 1 or segment == -1:
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.5, 0.3, 1.3, 3.0)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.75, 0.2, 1.1, 3.0)})
        for i in range(n_experiments):
            params.append({"seed":seed_base+i, "topdown_enabled":True, "params_td_curve":(1.75, 0.4, 1.1, 3.0)})
    return params
__author__ = "Otto van der Himst"
__version__ = "1.0"
__email__ = "otto.vanderhimst@ru.nl"

import sys
from util import Parameters
from data_handler import DataHandler
from net_single import NetworkSingle
import traceback
import gc
import os

try:
    os.nice(19)
except:
    pass


def run_single(argv, train=True):

    # Set the parameters
    P = Parameters()
    P.set_single(argv)

    # Initialize the single-layer network
    network = NetworkSingle(P)

    # Initialize the DataHandler
    data_handler = DataHandler(P)

    # Create and store new spike data if it is not in storage already
    data_handler.store_mnist_as_spikes(train=train, tag_mnist=network.tag_mnist)

    if train:  # Train the network
        network.train(data_handler=data_handler, P=P)
        return P.run_id
    else:  # Test the network
        network.test(data_handler=data_handler, P=P)




def main(argv):

    task = "train-single"  
    # task = "test-single"

    # =============================================================================
    #     SINGLE - TRAIN
    # =============================================================================

    if task == "train-single":

        argv = [
            "print_results=True",
            "print_interval=100",
            "plot_weight_ims=True",
            "plot_interval=100",
            "save_weight_ims=True",
            "save_weight_ims_interval=1000",
            "save_weights=True",
            "save_weights_interval=1000",
            "K=99",
        ]

        # Train a single layer WTA network on the MNIST
        run_single(argv, train=True)

    # =============================================================================
    #     SINGLE - TEST
    # =============================================================================
    load_run_id = "0000"
    # load_run_t = "52000"
    load_run_t = "59999"
    if task == "test-single":

        argv = [
            # "pf_pretrained_weights=None",
            "pf_pretrained_weights=[01LF] results/run-single_{}/weights/weights_t{}.npy".format(
                load_run_id, load_run_t
            ),
            "load_essential_params_only=True",
            # "pf_pre_parameters=None",
            "pf_pre_parameters=[01LF] results/run-single_{}/parameters.pkl".format(
                load_run_id
            ),
            "print_results=False",
            "print_interval=100",
            "plot_weight_ims=True",
            "plot_interval=100",
            "save_weight_ims=False",
            "save_weights=False",
            "evaluation_interval=500",
            "learn=False",
        ]

        # Test a single layer WTA network on the MNIST
        run_single(argv, train=False)


if __name__ == "__main__":

    try:
        gc.collect()  # Clear memory of unused items
        main(sys.argv[1:])

    except KeyboardInterrupt:
        print("\n" + "-" * 30 + " Keyboard Interrupt " + "-" * 30)
        gc.collect()  # Clear memory of unused items
    except Exception:
        print("\n\n\n" + "!" * 30 + " EXCEPTION " + "!" * 30 + "\n")
        print(traceback.format_exc())
        print("!" * 30 + "!!!!!!!!!!!" + "!" * 30 + "\n\n\n")
        gc.collect()  # Clear memory of unused items

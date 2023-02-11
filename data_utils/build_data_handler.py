from data_utils import *
from config.configurator import configs

def build_data_handler():
    if configs['data']['type'] == 'general_cf':
        data_handler = DataHandlerGeneralCF()
    elif configs['data']['type'] == 'multi_behavior':
        data_handler = DataHandlerMultiBehavior()
    else:
        raise NotImplementedError

    return data_handler
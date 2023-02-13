from models import *
from config.configurator import configs

def build_model(data_handler):
    if configs['model']['name'] == 'lightgcn':
        model = LightGCN(data_handler)
    elif configs['model']['name'] == 'sgl':
        model = SGL(data_handler)
    elif configs['model']['name'] == 'lightgcl':
        model = LightGCL(data_handler)
    elif configs['model']['name'] == 'cml':
        model = CML(data_handler)
    elif configs['model']['name'] == 'smin':
        model = SMIN(data_handler)
    elif configs['model']['name'] == 'kcgn':
        model = KCGN(data_handler)
    elif configs['model']['name'] == 'mmclr':
        model = MMCLR(data_handler)
    elif configs['model']['name'] == 'bert4rec':
        model = BERT4Rec(data_handler)
    else:
        raise NotImplementedError

    return model



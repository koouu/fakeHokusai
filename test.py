from UGATIT_test import UGATIT
import argparse
from utils import *

"""main"""
def main():
    # parse arguments
    

    # open session
    gan = UGATIT()

    # build graph
    gan.build_model()

    
    gan.test()
    print(" [*] Test finished!")

if __name__ == '__main__':
    main()

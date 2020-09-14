import unittest
import os

def load_all_case():
    #路径有问题    要检查

    case_pase = os.path.join(os.getcwd(),"case")
    print(case_pase)
    discover = unittest.defaultTestLoader.discover(case_pase, pattern='*Case.py',top_level_dir=None)
    return discover
if __name__=='__main__':

    runner = unittest.TextTestRunner()
    runner.run(load_all_case())


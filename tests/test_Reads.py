#!/usr/bin/env python
# import
from __future__ import print_function
## batteries
import os
import sys
import pytest
## 3rd party
import numpy as np
import pandas as pd
## package
from MGSIM import Utils
from MGSIM.Commands import Reads as Reads_CMD

# data dir
test_dir = os.path.join(os.path.dirname(__file__))
data_dir = os.path.join(test_dir, 'data')


# tests
def test_main():
    genome_table = os.path.join(data_dir, 'genome_list.txt')
    abund_table = os.path.join(data_dir, 'comm_wAbund.txt')
    output_prefix = os.path.join(data_dir, 'TEST')
    temp_dir = os.path.join(data_dir, 'temp_read_files')
    args = ['--debug',
            '--art-paired',
            '--tmp-dir', temp_dir,
            '--sr-seq-depth', 1e4, 
            genome_table, abund_table, output_prefix]
    Reads_CMD.opt_parse(args)
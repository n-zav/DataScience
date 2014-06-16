import os
import glob

import pandas as pd
from cStringIO import StringIO


def create_tableS():
    """
    reads 3 Sandra files into one csv file and creates a summary by day
    """
    #  get a list of all csv files in target directory
    my_dir = "/vagrant/DataScience/datascience/textfiles/Sandra/"
    filelist = []
    os.chdir( my_dir )
    for files in glob.glob("*.csv"):
        filelist.append(files)

    # read each csv file into single dataframe
    general_table = pd.DataFrame()

    for f in filelist:
        s = StringIO()
        with open(my_dir + f) as f:
            for line in f:
                if line.startswith('2012') or line.startswith('Days'):
                    s.write(line)
        s.seek(0)  # "rewind" to the beginning of the StringIO object

        frame = pd.read_csv(s, sep=None, engine='python')
        filename = os.path.splitext(str(f))[0]
        frame['Country'] = filename.split(' ')[3]
        general_table = general_table.append(frame, ignore_index=True)

    summary_table = general_table.groupby('Days').aggregate(sum)

    return general_table, summary_table

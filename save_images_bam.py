import urllib
import os
import sqlite3
import sys

url_file = "portraits.txt"
##f = open(url_file, "a")
##conn = sqlite3.connect('20170509-bam-1m-18UThu3ICM.sqlite')
##c = conn.cursor()
##for line in c.execute('select src from modules, crowd_labels where modules.mid = crowd_labels.mid and attribute = \'media_graphite\' and label=\'positive\' limit 500;'):
##    f.write(line[0] + "\n")
##f.close()
##
##conn.commit()
##conn.close()

with open(url_file) as fp:
    directory_name = "images/portraits/"

    if not os.path.isdir(os.path.join(os.getcwd(), directory_name)):
        os.mkdir(directory_name)
    for i, line in enumerate(fp):
        urllib.urlretrieve(line, directory_name + '{:04d}.jpg'.format(i))

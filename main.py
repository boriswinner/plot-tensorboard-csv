import glob
import os
import csv
import matplotlib.pyplot as plt

CSV_FOLDER = 'inputs'
XLABEL = 'Epoch'
YLABEL = 'Value'
NAME = 'Loss function'
LABELS = ['Train set', 'Validation set']
FILENAME = 'Loss'

paths = glob.glob(os.path.join(CSV_FOLDER, "*.csv"))

x = []
y = []
for i, path in enumerate(paths):
    filename = os.path.splitext(os.path.basename(path))[0]
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        timestamps = []
        x.append([])
        y.append([])
        iterator = iter(reader)

        #Skip headers
        for row in iterator:
            break

        for row in iterator:
            timestamps.append(row[0])
            x[i].append(int(row[1]))
            y[i].append(float(row[2]))


plt.rcParams.update({'font.size': 14})
for i in range(len(x)):
    plt.plot(x[i], y[i], label=LABELS[i])
plt.title(NAME)
plt.legend()
plt.grid()
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
plt.savefig('{}.png'.format(FILENAME), bbox_inches="tight", dpi=300)
plt.show()



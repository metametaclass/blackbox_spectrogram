# Jupyter notebook to analyze betaflight/inav blackbox data

# Prerequisites

* Anaconda: https://www.anaconda.com/distribution/
* blackbox tools: https://github.com/cleanflight/blackbox-tools/releases


# Working with notebook

* decode blackbox log:

```
blackbox_decode btfl_001.bbl
```

-> btfl_001.01.csv


* Clone repo:

```
git clone https://github.com/metametaclass/blackbox_spectrogram
```

* Copy decoded file btfl_001.01.csv to blackbox_spectrogram\data

* Run notebook 

```
cd blackbox_spectrogram
jupyter notebook
```

jupyter should open browser with notebook editor

* Edit log filename in second cell:

```
data = pd.read_csv('data\\btfl_001.01.csv', encoding='cp1251', decimal='.').rename(columns=lambda x: x.strip())
                    ^^^^^^^^^^^^^^^^^^^^^
```

* Run all cells step by step (shift-enter)


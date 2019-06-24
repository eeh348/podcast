# podcast
Tool to search podcasts


## Prerequisites

+ Anaconda 3.7
+ Python 3.7
+ Pip

## Installation


Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd ~podcast
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest
```

Use Anaconda to create and activate a new virtual environment, perhaps called "podcast-env":

```sh
conda create -n podcast-env python=3.7 # (first time only)
conda activate podcast-env
```

Install the following modules

```sh
requests
datetime
json
csv
os
statistics
```

Install the following packages

```sh
from dotenv import load_dotenv
```


## Setup



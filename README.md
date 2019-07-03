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

Use Anaconda to create and activate a new virtual environment, called "podcast-env":

```sh
conda create -n podcast-env python=3.7 # (first time only)
conda activate podcast-env
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest
```

## Listen API Key

This application uses the Listen API to search podcasts based on a variety of inputs. To obtain a listen API, follow the steps below:

1. Create an account on https://www.listennotes.com/api/
2. Request the free version
3. An API key will be sent to your email
4. Create an .env file and add the API to as X_LISTEN_API_KEY = "abc123"

## Run the app

Launch the app via the terminal.

```sh
python app/podcast.py
```

Input your search critera via the popup. Your results will be displayed in the terminal. Your results contains the top 10 results sorted by relevance and date.

## Testing
Run tests:

```sh
pytest python test/podcast_test.py
```

## Attestations
1. GUI adapted from https://pysimplegui.readthedocs.io/en/latest/tutorial/#the-5-minute-gui
2. Sort by date adapted from https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/

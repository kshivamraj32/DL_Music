## Music Genre classification using Deep Learning

### Overview

All the approaches are on the **nbs** folder in the Jupyter notebooks. 

Resume of the deep learning approach:

1. Shuffle the input and split into train and test (70%/30%)
2. Read the audios as melspectrograms, spliting then into 1.5s windows with 50% overlaping resulting in a dataset with shape (samples x time x frequency x channels)
3. Train the CNN and test on test set using a Majority Voting approach



### Dataset

And how to get the dataset?

1. Download the GTZAN dataset [here](http://opihi.cs.uvic.ca/sound/genres.tar.gz)

Extract the file in the **data** folder of this project. The structure should look like this:

```bash
├── data/
   ├── genres
      ├── blues
      ├── classical
      ├── country
      .
      .
      .
      ├── rock
```

### How to run

The models are provided as **.joblib** or **.h5** files in the *models* folder. You just need to use it on your custom file as described bellow.

If you want to run the training process yourself, you need to run the provided notebooks in *nbs* folder.

To apply the model on a test file, you need to run:

```bash
$ cd src/
$ python app.py -t dl -m ../models/PATH_TO_MODEL -s PATH_TO_SONG
```


Usage example:

```bash
$ python app.py -t dl -m ../models/custom_cnn_2d.h5 -s ../data/samples/iza_meu_talisma.mp3
```

and the output will be:

```bash
$ ../data/samples/iza_meu_talisma.mp3 is a pop song
$ most likely genres are: [('pop', 0.43), ('hiphop', 0.39), ('country', 0.08)]
```

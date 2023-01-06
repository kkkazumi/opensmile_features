from scipy.io import arff
import numpy as np
import pandas as pd

import subprocess

import os

relative_path= "../../"
smilextract_command = relative_path + "opensmile/build/progsrc/smilextract/SMILExtract"
opensmile_conffile = relative_path + "opensmile/config/is09-13/IS09_emotion.conf"

def wav2arff(wavfile):
    wav_top, ext = os.path.splitext(wavfile)
    outputfilename = "output_"+wav_top+".arff"
    subprocess.run([smilextract_command,'-C',opensmile_conffile,'-I',wavfile,'-O',outputfilename])
    #subprocess.run(ret,check=True)
    return outputfilename

def arff2feature(arff_filename):
    #filename = "a.arff"
    subprocess.run(["./remove.sh",arff_filename])
    dataset= arff.loadarff(arff_filename)
    ds = pd.DataFrame(dataset[0])
    print(ds)

def wav2feature(wavfilename):
    output_filename=wav2arff(wavfilename)
    feature = arff2feature(output_filename)
    return feature

filename = "a15.wav"
print(wav2feature(filename))

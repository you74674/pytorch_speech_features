#!/usr/bin/env python

from pytorch_speech_features import mfcc
#from pytorch_speech_features import delta
#from pytorch_speech_features import logfbank
import scipy.io.wavfile as wav
import torch
(rate,sig) = wav.read("english.wav")
sig = torch.FloatTensor(sig)
mfcc_feat = mfcc(sig,rate)
#d_mfcc_feat = delta(mfcc_feat, 2)
#fbank_feat = logfbank(sig,rate)

print(mfcc_feat[1:3,:])

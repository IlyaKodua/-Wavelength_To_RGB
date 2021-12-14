import numpy as np

def WaveLength_to_RGB(WaveLength):



  assert(WaveLength >= 380.0 and WaveLength<= 780.0)
  
  if ((WaveLength >= 380.0) and (WaveLength <= 410.0)):
    R =0.6-0.41*(410.0-WaveLength)/30.0
    G = 0.0
    B = 0.39+0.6*(410.0-WaveLength)/30.0

  elif ((WaveLength >= 410.0) and (WaveLength <= 440.0)):
    R =0.19-0.19*(440.0-WaveLength)/30.0
    G = 0.0
    B = 1.0

  elif ((WaveLength >= 440.0) and (WaveLength<= 490.0)):
    R =0
    G = 1-(490.0-WaveLength)/50.0
    B = 1.0

  elif ((WaveLength >= 490.0) and (WaveLength <= 510.0)):
    R =0
    G = 1
    B = (510.0-WaveLength)/20.0

  elif ((WaveLength >= 510.0) and (WaveLength <= 580.0)):
    R =1-(580.0-WaveLength)/70.0
    G = 1
    B = 0
  elif ((WaveLength >= 580.0) and (WaveLength<= 640.0)):
    R =1
    G = (640.0-WaveLength)/60.0
    B = 0
  elif ((WaveLength >= 640.0) and (WaveLength <= 700.0)):
    R =1
    G = 0
    B = 0
  elif ((WaveLength >= 700.0) and (WaveLength<= 780.0)):
    R =0.35+0.65*(780.0-WaveLength)/80.0
    G = 0
    B = 0
  

  return 255*np.array([R,G,B])




print(WaveLength_to_RGB(500))

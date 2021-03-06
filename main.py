

import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import os, urllib, cv2

            with urllib.request.urlopen("https://pjreddie.com/media/files/yolov3.weights"["url"]) as response:
                length = int(response.info()["Content-Length"])
          
        
                while True:
                    data = response.read(8192)
                    if not data:
                        break
                    counter += len(data)
                    output_file.write(data)

                    # We perform animation by overwriting the elements.
                    weights_warning.warning("Downloading %s... (%6.2f/%6.2f MB)" %
                        (file_path, counter / MEGABYTES, length / MEGABYTES))
                    progress_bar.progress(min(counter / length, 1.0))

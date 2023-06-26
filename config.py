{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4d44af51",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2023-06-26T07:32:06.306488Z",
     "iopub.status.busy": "2023-06-26T07:32:06.306119Z",
     "iopub.status.idle": "2023-06-26T07:32:06.318641Z",
     "shell.execute_reply": "2023-06-26T07:32:06.317749Z"
    },
    "papermill": {
     "duration": 0.018622,
     "end_time": "2023-06-26T07:32:06.321042",
     "exception": false,
     "start_time": "2023-06-26T07:32:06.302420",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "BATCH_SIZE = 48\n",
    "EDGE_CROP = 16\n",
    "GAUSSIAN_NOISE = 0.1\n",
    "UPSAMPLE_MODE = 'SIMPLE'\n",
    "# downsampling inside the network\n",
    "NET_SCALING = (1, 1)\n",
    "# downsampling in preprocessing\n",
    "IMG_SCALING = (3, 3)\n",
    "# number of validation images to use\n",
    "VALID_IMG_COUNT = 900\n",
    "# maximum number of steps_per_epoch in training\n",
    "MAX_TRAIN_STEPS = 5\n",
    "MAX_TRAIN_EPOCHS = 99\n",
    "AUGMENT_BRIGHTNESS = False\n",
    "TRAIN_SHIP_SEGM = '/kaggle/input/airbus-ship-detection/train_ship_segmentations_v2.csv'\n",
    "TRAIN_DIR = '/kaggle/input/airbus-ship-detection/train_v2'\n",
    "TEST_DIR = '/kaggle/input/airbus-ship-detection/test_v2/'\n",
    "SAMPLE_SEGM_DIR = '/kaggle/input/airbus-ship-detection/sample_submission_v2.csv'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 12.473658,
   "end_time": "2023-06-26T07:32:07.144242",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2023-06-26T07:31:54.670584",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

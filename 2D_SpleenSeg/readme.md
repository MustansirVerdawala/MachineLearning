# 🧫 2D Cell Segmentation using U-Net (MONAI)

This project performs **2D cell image segmentation** using a **U-Net** deep learning model implemented in **PyTorch** via the **MONAI** framework.  
The objective is to automatically delineate cell regions from microscopic images using a limited dataset of only 15 samples — demonstrating the feasibility of biomedical segmentation even with scarce data.

---

## 📂 Dataset

**Source:** [cell_benchmark Dataset (Hugging Face)](https://huggingface.co/datasets/alkzar90/cell_benchmark)  
**Files Used:** RGB images (`.jpg`) and binary masks (`.png`)  

**Split:**
- Training: 10 images  
- Validation: 2 images  
- Testing: 3 images  

**Image Size:** Resized to **512×512 px** for computational efficiency.

---

## 🧼 Data Preprocessing

- Binarized noisy mask images for clean segmentation targets  
- Normalized pixel intensities to `[0, 1]`  
- Resized all images for mini-batch processing  
- Organized data into `train`, `val`, and `test` folders  

---

## 🧠 Model Architecture

**Model:** 2D U-Net (implemented via MONAI)

- Encoder-decoder with skip connections  
- Residual units for gradient stability  
- Leaky ReLU activations  
- Dropout: 0.5  
- Input Channels: 3 (RGB)  
- Output Channels: 2 (cell / background)  

**Parameters:**  
`channels = (16, 32, 64, 128, 256)`  
`strides = (2, 2, 2, 2)`

---

## ⚙️ Training Details

- **Optimizer:** Adam (`lr = 1e-2`)  
- **Loss:** Dice Loss (softmax=True)  
- **Scheduler:** StepLR (reduce LR every 50 epochs)  
- **Batch Size:** 5  
- **Epochs:** Up to 1000 (early stopping after 50 stagnant epochs)  
- **Hardware:** Google Colab CPU (12GB RAM)

---

## 📈 Evaluation Metric

**Primary Metric:** Dice Similarity Coefficient (DSC)

|  Dataset   | Mean Dice Score |
|------------|-----------------|
| Training   |     0.9654      |
| Validation |     0.9363      |
| Test       |     0.9471      |

---

## 📊 Results & Observations

- The model captured cell boundaries and general structure accurately.  
- Slightly higher validation Dice suggests good regularization.  
- Fine-grained details were missed due to small dataset size and mask noise.  
- Confirms U-Net’s strong generalization even with limited biomedical data.

---

## 🚀 Run on Google Colab

Run the full notebook directly using the link below:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MUl3SL9cOldZh3ErJ1rsLnzkA_ZVOnkf)

---

## 🛠️ Libraries Used

- `PyTorch`
- `MONAI`
- `NumPy`
- `OpenCV`
- `Matplotlib`
- `itk`
- `nibabel`
- `pydicom`

---

## 🔬 Key Insights

- Even with only 15 images, U-Net produced meaningful segmentations.  
- Preprocessing quality (especially mask binarization) was crucial for DSC accuracy.  
- MONAI significantly simplified training, validation, and inference workflows for medical imaging.

---

## 📎 Author

**Mustansir Verdawala**  
Toronto Metropolitan University  
📧 mustansir.verdawala@torontomu.ca  

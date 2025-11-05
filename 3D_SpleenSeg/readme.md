# 🩺 3D Spleen Segmentation using MONAI & 3D U-Net

This project implements a **3D U-Net** model for automated spleen segmentation from abdominal CT scans using the **MONAI** deep learning framework.  
The objective is to delineate spleen regions accurately for volumetric and diagnostic analysis.

---

## 📘 Introduction

Accurate spleen segmentation from CT scans is crucial for applications in medical imaging such as volumetric assessment, diagnosis of splenomegaly, monitoring hematologic disorders, and preoperative planning.  
Traditional segmentation methods often fail to generalize due to anatomical variability and low contrast boundaries.  

Deep learning architectures such as **3D U-Net** effectively address these challenges by learning volumetric features and spatial context.  
This project uses MONAI for data preprocessing, patch-based training, and model evaluation.

---

## 📂 Dataset

**Dataset Used:** Medical Segmentation Decathlon - Spleen  
**Format:** NIfTI (.nii.gz)  
**Source:** [Medical Segmentation Decathlon](https://medicaldecathlon.com/) / [Hugging Face - Angelou0516/msd-spleen](https://huggingface.co/datasets/Angelou0516/msd-spleen)

- Volumetric CT scans of the abdomen  
- Ground truth spleen masks provided  
- Dataset split: 20 training, 10 validation, 11 testing samples

---

## ⚙️ Preprocessing

- **HU Windowing:** [-190, 300]  
- **Normalization:** [0, 1] scaling after clipping [-1024, 1023]  
- **Morphological Cleaning:** Binary closing to remove small artifacts  
- **Patch Extraction:** 256 × 256 × 128 voxel patches  
- **One-Hot Encoding:** Background vs Spleen

---

## 🧠 Model Architecture

**Model:** 3D U-Net  
**Framework:** MONAI (PyTorch-based)

| Component | Details |
|------------|----------|
| Encoder | 4 levels, filters (8, 16, 32, 64) |
| Decoder | Transposed convolutions with skip connections |
| Activation | Leaky ReLU |
| Loss | Dice Loss (Softmax) |
| Optimizer | Adam (lr=1e-2) |
| Scheduler | MultiStepLR |
| Batch Size | 2 |
| Dropout | 0.5 |
| Epochs | 1000 (with early stopping) |

---

## 🏋️ Training

Training was performed on **Google Colab GPU**.  
The model was monitored using the **validation Dice Similarity Coefficient (DSC)** for early stopping.

**Evaluation Metrics:**
- Dice Similarity Coefficient (DSC)
- Jaccard Index (IoU)

---

## 📈 Results

| Dataset | Dice (DSC) | Jaccard (IoU) |
|----------|-------------|----------------|
| Train | **0.8691** | 0.7711 |
| Validation | 0.7867 | 0.6573 |
| Test | 0.7631 | 0.6279 |

The model demonstrates effective spleen localization and segmentation.  
However, a slight performance gap between training and test sets suggests **overfitting** due to limited data diversity.

---

## 📊 Visualization

- Axial slice visualization of CT scan and spleen mask  
- 3D U-Net prediction overlays  
- Training loss and validation Dice tracking  

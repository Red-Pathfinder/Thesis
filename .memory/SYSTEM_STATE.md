# System State & Invariants

This file provides a living snapshot of the thesis research architecture, active components, and non-negotiable invariants.

---

## 1. Research Project Specifications
* **Primary Topic:** Computational Digital Pathology: Multi-Class Tissue Semantic Segmentation on Whole Slide Images (WSIs).
* **Target Dataset:** BCSS (Breast Cancer Semantic Segmentation)
  - 151 patients, 23,422 patches.
  - 5-Class Target: Tumor Epithelium, Stroma, Necrosis, Lymphocytes, Background.
* **Primary Metrics:** Mean Intersection-over-Union (mIoU), Mean Dice Coefficient (mDice), Class-wise Dice.
* **Supervisory Committee:** Dr. Partha Pratim Sarangi, Dr. Deepak Ranjan Nayak (NIT Patna).

---

## 2. Hard Invariants (Must Not Be Broken)
1. **Zero Data Leakage:** Patches must be partitioned strictly by patient ID. Never perform random patch-level splitting.
2. **Deterministic Reproducibility:** Fixed seeds (`torch.manual_seed(42)`, `np.random.seed(42)`, deterministic CuDNN).
3. **Weight Hygiene:** Never commit model weights (`*.pt`, `*.pth`, `*.onnx`) or gigapixel WSIs to Git.
4. **Epistemic Honesty:** All claims in the thesis manuscript must trace back to recorded experiment numbers in `ITERATIONS.md` or verified citations.

---

## 3. Directory Layout & Roles
* `src/`: PyTorch modules (DataLoaders, U-Net architecture, losses, training loop).
* `configs/`: Modular YAML configs defining hyperparameters and dataset paths.
* `literature/`: Zotero foundation papers (symlinked) and Markdown extraction notes.
* `manuscript/`: Overleaf/LaTeX chapters and compiled references.
* `notebooks/`: Colab execution notebooks.
* `.memory/`: Self-contained decision ledger (audit-ready).

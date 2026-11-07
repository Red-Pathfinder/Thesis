# Computational Digital Pathology: Multi-Class Tissue Semantic Segmentation

**Master's Thesis Research Repository**  
*Author:* Pragyan Prayas Jena ([@Red-Pathfinder](https://github.com/Red-Pathfinder))  
*Supervisory Committee:* Dr. Partha Pratim Sarangi, Dr. Deepak Ranjan Nayak (NIT Patna)

---

## 1. Abstract & Research Focus
This research addresses the challenges of multi-class tissue characterization on gigapixel Whole Slide Images (WSIs). We target the 5-class semantic segmentation problem across Tumor Epithelium, Stroma, Necrosis, Lymphocyte Infiltration, and Background on the **BCSS (Breast Cancer Semantic Segmentation)** dataset.

The investigation follows a two-tier paradigm:
1. **Fully Supervised Baseline:** A rigorous standard U-Net architecture evaluated with class-wise and Mean Dice score (mDice) and Mean Intersection-over-Union (mIoU).
2. **Advanced Paradigms:** Investigating **Single-Stage Hierarchical Rectification (SSHR)** for weakly supervised learning and **Dynamic Focal Attention (DFA)** on query-based mask decoders (SAM-Path).

---

## 2. Repository Layout & Architecture

```text
Thesis/
├── .memory/               # Audit-ready Decision Ledger (Mermaid DAGs, decisions, iterations)
│   ├── DECISION_GRAPH.md  # Architectural choices, why they were made & rejected options
│   ├── SYSTEM_STATE.md    # Active specifications, data lineage, and hard invariants
│   └── ITERATIONS.md      # Quantitative experiment logs
├── configs/               # Modular YAML configs for deterministic reproducibility
├── literature/            # Zotero foundation papers & extracted markdown summaries
│   ├── zotero_thesis_papers/  # Local symlinks to Zotero PDFs (zero byte duplication)
│   └── notes/             # Clean structured notes extracted via pdf-scholar-reader
├── src/                   # PyTorch modules (DataLoaders, Models, Losses, Training)
│   ├── data/
│   ├── models/
│   ├── training/
│   └── utils/
├── experiments/           # Experiment metrics.json and training output logs
├── figures/               # 300+ DPI vector plots (PDF/SVG) for manuscript
├── manuscript/            # LaTeX thesis source code (main.tex, chapters, references.bib)
├── notebooks/             # Google Colab training runner notebooks
└── scripts/               # Helper utilities (export_decisions_bundle.py, etc.)
```

---

## 3. Google Colab Training Workflow

Because local training of 23,422 pathology patches is compute-intensive, training runs on Google Colab accelerators:

```bash
# 1. In Colab, clone the repository
!git clone https://github.com/Red-Pathfinder/Thesis.git
%cd Thesis

# 2. Install dependencies
!pip install -r requirements.txt

# 3. Mount Google Drive for heavy checkpoint storage
from google.colab import drive
drive.mount('/content/drive')

# 4. Run baseline training
!python src/train.py --config configs/baseline_unet_bcss.yaml --checkpoint-dir /content/drive/MyDrive/Thesis_Checkpoints/
```

---

## 4. Auditing & Peer Review

To export all research decisions, system states, and experiment configs into a single ZIP for external review (e.g., Claude or your advisory committee):

```bash
python3 scripts/export_decisions_bundle.py
```
This generates `thesis_decisions_bundle_<timestamp>.zip` ready to share for an independent second opinion.

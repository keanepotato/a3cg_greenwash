# Towards Robust ESG Analysis Against Greenwashing Risks: Aspect-Action Analysis with Cross-Category Generalization

📢 **Our paper has been accepted to ACL 2025 Main Conference!** 🎉

This repository contains the dataset, code, and evaluation scripts for our ACL 2025 paper:

> **Towards Robust ESG Analysis Against Greenwashing Risks: Aspect-Action Analysis with Cross-Category Generalization**  
> *Keane Ong, Rui Mao, Deeksha Varshney, Erik Cambria, Gianmarco Mengaldo*

📄 **Paper**: [Read it on ACL Anthology](https://aclanthology.org/2025.acl-long.723/)

📬 **Contact**: Please feel free to reach out if you have any questions or would like to connect:  
[keane.ongweiyang@u.nus.edu](mailto:keane.ongweiyang@u.nus.edu) | [keaneong@mit.edu](mailto:keaneong@mit.edu)

---

## 📂 Dataset Structure

The datasets used in this work are located in the `dataset` directory, which includes the following subfolders:

- `full/`  
  Contains the **full dataset**, with all data from folds 1, 2, and 3 combined.  
  - This version **does not** partition aspect categories into *seen* and *unseen*.  
  - This is primarily utilised within the paper to test for the general training stability of the dataset.

- `fold_1/`, `fold_2/`, `fold_3/`  
  Each fold directory contains four pre-partitioned JSON files based on aspect category visibility:

  - `fold_<x>_seen_train.json`: Training data with *seen* aspect categories  
  - `fold_<x>_seen_val.json`: Validation data with *seen* aspect categories  
  - `fold_<x>_seen_test.json`: Test data with *seen* aspect categories  
  - `fold_<x>_unseen_test.json`: Test data with *unseen* aspect categories (i.e., categories not encountered during training)
  
  *(Replace `<x>` with 1, 2, or 3 for each fold)*

  `statistics\` directory within each fold provides the details of the data within each fold and its corresponding partitions, including the aspect category count etc.

### 🧪 Experimental Protocol

- We **train** on `fold_<x>_seen_train.json` and **validate** on `fold_<x>_seen_val.json`.
- We **evaluate** model performance on both `fold_<x>_seen_test.json` and `fold_<x>_unseen_test.json`.
- The *seen* partitions include only aspect categories observed during training, while *unseen* test sets evaluate generalization to novel aspect categories.


---

## 🔖 Citation

If you find this work useful, please use the following citation:

```bibtex
@article{ong2025greeenwash,
  title={Towards Robust ESG Analysis Against Greenwashing Risks: Aspect-Action Analysis with Cross-Category Generalization},
  author={Ong, Keane and Mao, Rui and Varshney, Deeksha and Cambria, Erik and Mengaldo, Gianmarco},
  journal={arXiv preprint arXiv:2502.15821},
  year={2025}
}

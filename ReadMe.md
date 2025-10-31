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

  `statistics/` directory within each fold provides the details of the data within each fold and its corresponding partitions, including the aspect category count etc.

### 🧪 Experimental Protocol

- We **train** on `fold_<x>_seen_train.json` and **validate** on `fold_<x>_seen_val.json`.
- We **evaluate** model performance on both `fold_<x>_seen_test.json` and `fold_<x>_unseen_test.json`.
- The *seen* partitions include only aspect categories observed during training, while *unseen* test sets evaluate generalization to novel aspect categories.

## 📊 Model Evaluation

- This repository supports multiple model families for Aspect–Action Analysis under the **A3CG** framework.  
- Currently, the **GRACE** model is fully cleaned and ready for evaluation.  
- Other model families (e.g., baseline transformer variants, multi-task, and instruction-tuned LLMs) are still being cleaned and will be released shortly.

---

### ⚙️ Evaluating the GRACE Model

- Each evaluation corresponds to one of the three cross-category folds (**F1**, **F2**, **F3**) and to either the *seen* or *unseen* test split, or the full dataset.  
- The evaluation shell scripts are located in the root directory (or under `scripts/`, if organized as such).
- Trained Models have been uploaded to [Hugging Face](https://huggingface.co/keentomato), and are prefixed by a3cg_greenwash (i.e. keentomato/a3cg_greenwash_grace_f1)

#### 🔹 Run Evaluation

```bash
# Full dataset
./_full_dataset_test.sh

# Fold 1
./_f1_seen_test.sh
./_f1_unseen_test.sh

# Fold 2
./_f2_seen_test.sh
./_f2_unseen_test.sh

# Fold 3
./_f3_seen_test.sh
./_f3_unseen_test.sh
```

- Each script internally calls:

```bash 
python ate_asc_run.py --config_path configs/aspect_action/<config_file>.json
```

- Each run produces results under, including predictions, logs and metrics:

```bash 
results/<fold>_<seen_or_unseen>/
```

🚧 **Other models are coming soon!** We're currently cleaning up our code base and will release model checkpoints and evaluation outputs shortly.

---

## 🔖 Citation

If you find this work useful, please use the following citation:

```bibtex
@inproceedings{ong-etal-2025-towards-robust,
    title = "Towards Robust {ESG} Analysis Against Greenwashing Risks: Aspect-Action Analysis with Cross-Category Generalization",
    author = "Ong, Keane  and
      Mao, Rui  and
      Varshney, Deeksha  and
      Cambria, Erik  and
      Mengaldo, Gianmarco",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.723/",
    doi = "10.18653/v1/2025.acl-long.723",
    pages = "14854--14879",
    ISBN = "979-8-89176-251-0",
    abstract = "Sustainability reports are key for evaluating companies' environmental, social and governance (ESG) performance. To analyze these reports, NLP approaches can efficiently extract ESG insights at scale. However, even the most advanced NLP methods lack robustness against ESG content that is greenwashed {--} i.e. sustainability claims that are misleading, exaggerated, and fabricated. Accordingly, existing NLP approaches often extract insights that reflect misleading or exaggerated sustainability claims rather than objective ESG performance. To tackle this issue, we introduce A3CG - \textbf{A}spect-\textbf{A}ction \textbf{A}nalysis with Cross-\textbf{C}ategory \textbf{G}eneralization, as a novel dataset to improve the robustness of ESG analysis amid the prevalence of greenwashing. By explicitly linking sustainability aspects with their associated actions, A3CG facilitates a more fine-grained and transparent evaluation of sustainability claims, ensuring that insights are grounded in verifiable actions rather than vague or misleading rhetoric. Additionally, A3CG emphasizes cross-category generalization. This ensures robust model performance in aspect-action analysis even when companies change their reports to selectively favor certain sustainability areas. Through experiments on A3CG, we analyze state-of-the-art supervised models and LLMs, uncovering their limitations and outlining key directions for future research."
}

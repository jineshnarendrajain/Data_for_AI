# Reproducibility Checklist

> This checklist documents the current reproducibility state of the
> Manhattan Urban Heat cleaning workflow developed during Session 3.

---

# The bar

Reproducibility for this workflow means that the cleaning structure,
processing logic, and modular pipeline can be re-run consistently using
the same Landsat and Sentinel input datasets within the same project
environment.

Because the workflow remains exploratory and partially conceptual,
reproducibility is currently focused on:
- deterministic structure,
- modular cleaning logic,
- stable file organization,
- and repeatable workflow sequencing.

---

# The five disciplines

---

## 1. Determinism

- [x] Random seed configured in `src/clean_data.py`
- [x] Cleaning functions structured in deterministic sequence
- [x] No use of `datetime.now()` or time-dependent runtime logic
- [x] No machine-specific environment variables used in cleaning logic
- [ ] Full deterministic raster outputs verified across repeated runs

---

## 2. Pinned dependencies

- [ ] `requirements.txt` finalized with exact package versions
- [ ] Environment freeze generated after successful testing
- [ ] Python version documented in project README

---

## 3. Path discipline

- [x] Paths organized using `pathlib.Path`
- [x] Paths structured relative to project root
- [x] Cleaning workflow avoids absolute machine-specific paths
- [x] Input and output paths centralized in `src/clean_data.py`

---

## 4. The "runs from scratch" test

The intended reproducibility workflow is:

```bash
python -m venv .venv

pip install -r requirements.txt

python src/clean_data.py
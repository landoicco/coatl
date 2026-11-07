# Coatl 🐍

A polished, classic **Snake-like arcade game** built from scratch with Python and Pygame. 

This project serves as a learning milestone focused on clean code structure, environment reproducibility, audio integration, and modern development tooling.

> **What does "Coatl" mean?** It is the Nahuatl word for *snake* or *serpent* (commonly referenced in historical dictionaries like [Gran Diccionario Náhuatl](https://unam.mx)).

---

## ✨ Features
* **Retro Audio Experience:** Dynamic background music and sound effects to elevate gameplay.
* **Polished Flow:** Seamless arcade-style transition loops featuring fully integrated Start and Game Over splash screens.
* **Deterministic Ecosystem:** Built on strict versioning practices to avoid execution inconsistencies.

---

## 🚀 Getting Started

This repository supports two running workflows: a fully-isolated development environment via **Nix Flakes** (ideal for NixOS/Linux), and a modernized cross-platform setup using **`uv`**.

### Option A: Using Nix Flakes (Recommended) ❄️
If you have Nix installed, you can drop into a perfectly configured shell with Python, Pygame, Ruff, and the GitHub CLI pre-installed by simply running:

```shell
nix develop
```
Then start the game:
```shell
python src/main.py
```

### Option B: Using `uv` (Cross-platform) 🚀
If you prefer a traditional Python pipeline or are on a non-Nix system, ensure you have [uv](https://github.com) installed, then execute:

```shell
uv run src/main.py
```

---

## 🛠️ Tech Stack & Tooling
* **Core:** Python 3.11+ & Pygame-CE (Community Edition)
* **DevOps / Environment:** Nix Flakes (System level) & `pyproject.toml` (Metadata)
* **Linter & Formatter:** Ruff
* **Distribution:** PyInstaller (Executable packing targets)

---

## 📌 Roadmap & Version 2.0.0 Goals

- [x] Migrate ecosystem to high-performance dependency tracking
- [x] Implement smooth Splash Screen and Game Over flows
- [x] Add dynamic background audio tracks
- [ ] Overhaul general UI look, text scaling, and feel
- [ ] Optimize modular sprite rendering logic
- [ ] Integrate test suites and coverage verification
- [ ] Inject dynamic developer social hyperlinks straight into the game interface

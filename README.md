<div align="left" style="position: relative;">

<h1> Dunzo Backend (Python-Flask) </h1>
<p align="left">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/princemathur4/dunzo_flask?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/princemathur4/dunzo_flask?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/princemathur4/dunzo_flask?style=default&color=0080ff" alt="repo-language-count">
</p>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)

---

##  Overview

This App aims to create some of the backend APIs of a Dunzo like grocery delivery app using Python flask  

---

##  Features
1. API to return list of nearby available shops with their s (assume all shops are of the
same kind)
2. API to return the menu and items availability of a particular shop
3. Add to cart option for a user, from a single shop
4. Allow users to place orders.
5. Delivery person assignment(based on distance)

---

##  Project Structure

```sh
└── dunzo_flask/
    ├── README.md
    ├── app.py
    ├── config
    │   ├── default.py
    │   └── local.py
    ├── modules
    │   ├── __init__.py
    │   ├── common
    │   ├── entities
    │   └── exceptions.py
    ├── requirements.txt
    └── scripts
        └── insert_records.py
```

---
##  Getting Started

###  Prerequisites

Before getting started with dunzo_flask, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install dunzo_flask using one of the following methods:

**Build from source:**

1. Clone the dunzo_flask repository:
```sh
❯ git clone https://github.com/princemathur4/dunzo_flask
```

2. Navigate to the project directory:
```sh
❯ cd dunzo_flask
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run dunzo_flask using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```



---
##  Project Roadmap
- [x] API to return list of nearby available shops with their s (assume all shops are of the same kind)
- [ ] API to return the menu and items availability of a particular shop
- [ ] Add to cart option for a user, from a single shop
- [ ] Allow users to place orders.
- [ ] Delivery person assignment(based on distance)
---

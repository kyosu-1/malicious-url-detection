# malicious url detection

悪性URL検知の機械学習・深層学習アルゴリズムの論文実装を行う

## Requirements

* pyenv
* Poetry
* Docker

## Setup

Install Python Dependencies

Use pyenv to install Python 3.9.10 environments

```bash
$ pyenv install 3.9.10
$ pyenv local 3.9.10
```

Use `poetry` to install library dependencies

```bash
$ poetry install
```

## Code static analysis tool
| Tool                   | Usage              |
|----------------------------|----------------------------|
| [isort](https://pycqa.github.io/isort/)             | library import statement check     |
| [black](https://pypi.org/project/black/)           | format code style  |
| [flake8](https://flake8.pycqa.org/en/latest/)           | code quality check      |
| [mypy](https://mypy.readthedocs.io/en/stable/)    |  static type checking |
| [pysen](https://github.com/pfnet/pysen)    | manage static analysis tool  |

## Usage

Run formatter
```bash
$ make format
```

Run linter 
```bash
$ make lint 
```

Run pytest 
```bash
$ make test 
```

## 参考論文1

- title: URLNet: Learning a URL Representation with Deep Learning for Malicious URL Detection
- Author: Hung Le, Quang Pham, Doyen Sahoo, Steven C.H. Hoi
- link: https://arxiv.org/abs/1802.03162
- 実装: https://github.com/Antimalweb/URLNet

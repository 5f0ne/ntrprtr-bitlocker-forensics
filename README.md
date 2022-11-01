# Description

ntrprtr configurations for forensic analysis of bitlocker volumes

# Installation

`pip install ntrprtr_bitlocker_forensics`

# Usage

**Shell:**

<hr>

**General**

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--mode | -m | String | - | copy = Create a local copy of bitlocker forensics configuration files |

<hr>

**mode = copy**

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | "" | Path for local copy of ntrprtr configuration files |


# Example

To use this configuration files install `ntrprtr` and `ntrprtr_bitlocker_forensics`:

```bash
pip install ntrprtr
pip install ntrprtr_bitlocker_forensics
```

To use the files, create a local copy:

```bash
python -m ntrprtr_bitlocker_forensics -m copy -p .
```

It creates the following structure:

```
./ntrprtr-bitlocker-config
├───bitlocker-metadata-header.json
├───bitlocker-volume-header.json
```

Now just use the config as input for `ntrprtr`:

```bash
python -m ntrprtr -m interpret -p bitlocker-volume-header.bin -c ./ntrprtr-bitlocker-config/bitlocker-volume-header.json -r result.txt
```

# License

MIT
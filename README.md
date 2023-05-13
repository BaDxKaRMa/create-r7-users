# README
Script used for creating users in Rapid7 InsightVM.

## Features
1. Logging via Loguru
2. .env loading via python-dotenv
3. Accepts CSV file as input for bulk creation

## Setup
### Install dependencies
```bash
pip install -r requirements.txt
```

### Create .env file
```bash
cp .env.example .env
```
Update this file with your InsightVM credentials.

### Create virtualenv
```bash
python3 -m venv venv
```

## Usage
### Running locally
```bash
./user-toolkit.py --csv-file <path-to-csv-file> --debug
```

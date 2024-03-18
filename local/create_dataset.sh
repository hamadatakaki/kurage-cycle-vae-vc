#!/usr/bin env bash

EXP_PATH="exp/male_to_male/data"
CORPUS_PATH="$HOME/speech/corpus/jvs_ver1"

# Male to Male
python local/scripts/create_dataset.py jvs001 jvs003 "$CORPUS_PATH" "$EXP_PATH"

#!/usr/bin/env python3

import argparse
import json
import os
import sys

from pathlib import Path


if __name__ == '__main__':

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Read a JSON file and create a directory.')
    parser.add_argument('--input', required=True, help='Path to the input JSON file')
    parser.add_argument('--output', required=True, help='Path to the output directory to create')

    # Parse command-line arguments
    args = parser.parse_args()

    # Read the JSON file
    try:
        with open(args.input, 'r') as f:
            data = [json.loads(line) for line in f]
            print(f"Successfully read JSON data: {data}")
    except FileNotFoundError:
        print(f"Error: The file {args.input} does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {args.input} is not a valid JSON file.")
        sys.exit(1)

    # Create the directory
    try:
        os.makedirs(args.output, exist_ok=True)
        print(f"Directory created at: {args.output}")
    except OSError as e:
        print(f"Error: Could not create directory {args.output}. {e}")
        sys.exit(1)

    for ground_truth_json in data:
        kva_name = ground_truth_json["data_row"]["external_id"]

        # Specify the file path
        file_path = Path(args.output) / f"{os.path.splitext(kva_name)[0]}.json"

        # Save the data to a JSON file
        with open(file_path, 'w') as json_file:
            json.dump(ground_truth_json, json_file, indent=4)

        pass

    pass


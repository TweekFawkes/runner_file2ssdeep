import argparse
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Input file name from inputs directory')
    args = parser.parse_args()
    
    # Construct full input path
    input_path = os.path.join('inputs', args.file)
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist")
        return

    try:
        import ssdeep
        
        # Compute fuzzy hash
        with open(input_path, 'rb') as f:
            file_data = f.read()
        
        fuzzy_hash = ssdeep.hash(file_data)
        
        # Print fuzzy hash to screen
        print(f"Fuzzy hash for {input_path}:")
        print(fuzzy_hash)
        
        # Create outputs directory if it doesn't exist
        os.makedirs('outputs', exist_ok=True)
        
        # Create output filename with timestamp format YYYYMMDDHHMMSS_ssdeep.txt
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_file = os.path.join('outputs', f"{timestamp}_ssdeep.txt")
        
        # Check if output file already exists
        if os.path.exists(output_file):
            print(f"Warning: Output file '{output_file}' already exists and will be overwritten")
        
        # Write fuzzy hash to file
        with open(output_file, 'w') as f:
            f.write(f"File: {input_path}\n")
            f.write(f"Fuzzy Hash: {fuzzy_hash}\n")
        
        print(f"Fuzzy hash saved to {output_file}")
        
    except ImportError:
        print("Please install ssdeep first: pip install ssdeep")
    except Exception as e:
        print(f"Error computing fuzzy hash: {str(e)}")

if __name__ == "__main__":
    main()
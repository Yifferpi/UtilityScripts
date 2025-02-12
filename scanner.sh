#! /bin/bash

# This script is a wrapper for scanimage, which is a command line interface to SANE (Scanner Access Now Easy).
# It should allow to scan multiple consecutive pages without a feeder, confirming the scan of each page by pressing ENTER, and uniting the scans into a single PDF file.

# The script is intended to be used with a flatbed scanner, and it is not guaranteed to work with other types of scanners.
#!/bin/bash

# This script is a wrapper for scanimage, which is a command line interface to SANE (Scanner Access Now Easy).
# It allows scanning either a single page or multiple consecutive pages without a feeder,
# confirming the scan of each page by pressing ENTER, and uniting the scans into a single PDF file.

scanner_name="Canon LiDE 120"
device_name=$(scanimage -L | grep "$scanner_name" | cut -d ' ' -f 2 | cut -c 2-23)
timestamp=$(date +"%Y%m%d_%H%M%S")
output_pdf="scan$timestamp.pdf"

# Set dimensions for A4 paper
zero_x=2
zero_y=3
width=210
height=297

# Display help message
print_help() {
    echo "Usage: $0 [-s | -m | -h]"
    echo "  -s    Scan a single page"
    echo "  -m    Scan multiple pages (press ENTER after each page, type 'done' when finished)"
    echo "  -h    Display this help menu"
}

# Check for flags
single_scan=false
multi_scan=false

while getopts "smh" opt; do
    case $opt in
        s) single_scan=true ;;
        m) multi_scan=true ;;
        h) print_help; exit 0 ;;
        *) print_help; exit 1 ;;
    esac
done

# Validate flags
if [ "$single_scan" = true ] && [ "$multi_scan" = true ]; then
    echo "Error: Cannot select both single and multi-page scan modes."
    print_help
    exit 1
fi

if [ "$single_scan" = false ] && [ "$multi_scan" = false ]; then
    echo "Error: No scan mode selected."
    print_help
    exit 1
fi

# Create a temporary directory for storing scanned pages
temp_dir=$(mktemp -d)
if [[ ! "$temp_dir" || ! -d "$temp_dir" ]]; then
    echo "Error: Could not create temporary directory"
    exit 1
fi

# Function to clean up the temporary directory
cleanup() {
    rm -rf "$temp_dir"
}
trap cleanup EXIT

# Function to scan a single page
scan_page() {
    local page_num="$1"  # Page number argument

    scanimage \
        --device "$device_name" \
        --mode Color \
        --resolution 300 \
        --progress \
        --format=tiff \
        --source Flatbed \
        -l "$zero_x" -t "$zero_y" \
        -x "$width" -y "$height" \
    | img2pdf \
        --pagesize A4 \
        -o "$temp_dir/page$page_num.pdf"
}


# Single page scan
if [ "$single_scan" = true ]; then
    echo "Scanning a single page."
    scan_page 1
    echo "Single page scanned."

# Multi-page scan
elif [ "$multi_scan" = true ]; then
    echo "Scanning multiple pages with a flatbed scanner."
    echo "Press ENTER to scan each page. Type 'done' and press ENTER when finished."
    
    page_num=1

    while true; do
        
        scan_page $page_num
        echo "Page $page_num scanned."
        
        read -p "Press ENTER to scan page $page_num or type 'done' to finish: " user_input
        if [[ "$user_input" == "done" ]]; then
            break
        fi

        # Increment page count
        ((page_num++))
    done
fi

# Combine all scanned pages into a single PDF
echo "Combining scanned pages into a single PDF..."
pdfunite "$temp_dir/page"*.pdf "$output_pdf"

# Run ocrmypdf to perform OCR on the PDF
echo "Performing OCR on the PDF..."
ocrmypdf -l eng+deu --clean --optimize 1 --jpeg-quality 50 --jbig2-lossy "$output_pdf" "$output_pdf"

echo "Scanning completed. Output saved as $compressed_output."


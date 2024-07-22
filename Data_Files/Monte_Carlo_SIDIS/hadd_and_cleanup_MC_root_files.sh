#!/bin/bash

# Ensure the script was called with at least one argument
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <variable_part> [action]"
    exit 1
fi

VARIABLE_PART=$1
ACTION=${2:-run} # Default action is 'run' if not provided
DIRECTORY="/w/hallb-scshelf2102/clas12/richcap/Exclusive_RG-A_Momentum_Corrections/Data_Files/Monte_Carlo_SIDIS/" # Adjust the directory path as needed
FILE_PATTERN="Simulated_Single_Pion_Channel_epipX_Inbending_With_Dp_${VARIABLE_PART}_File"
INPUT_FILES="${FILE_PATTERN}_3*root"
OUTPUT_FILE="${FILE_PATTERN}_All.root"

# Check for existing output file
if [ -f "${DIRECTORY}${OUTPUT_FILE}" ]; then
    if [ "$ACTION" = "check" ]; then
        echo "Output file $OUTPUT_FILE already exists."
        echo "Remove it manually if you want to run the hadd command again for the files:"
        echo "       $INPUT_FILES"
        echo ""
    else
        echo "Error: Output file $OUTPUT_FILE already exists. Remove it manually if you want to proceed."
        echo ""
        exit 2
    fi
fi


# Check if input files exist
shopt -s nullglob # Make sure an empty glob matches nothing
file_array=(${DIRECTORY}${INPUT_FILES})
if [ ${#file_array[@]} -eq 0 ]; then
    echo "Error: No input files found matching pattern $INPUT_FILES."
    exit 3
fi
shopt -u nullglob # Revert nullglob back to its default behavior


# Proceed based on ACTION
if [ "$ACTION" = "check" ]; then
    echo "Checking input files for pattern: $FILE_PATTERN"
    ls -lhS ${DIRECTORY}${FILE_PATTERN}*
    FILE_COUNT=$(ls -1 ${DIRECTORY}${FILE_PATTERN}* 2>/dev/null | wc -l)
    echo "Number of files to be combined: ${FILE_COUNT}"
    echo ""
    echo "Input Files Name = $INPUT_FILES"
    echo ""
else
    # Run the hadd command
    echo "Combining files: ${INPUT_FILES} into ${OUTPUT_FILE}"
    echo ""
    $ROOTSYS/bin/hadd ${DIRECTORY}${OUTPUT_FILE} ${DIRECTORY}${INPUT_FILES}; ls -lhtr ${DIRECTORY}${FILE_PATTERN}*
    
    # Check if hadd was successful before prompting for cleanup
    if [ $? -eq 0 ]; then
        echo "Do you want to delete the input files? [y/n]"
        echo "Input Files Name = $INPUT_FILES"
        read -r response
        if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
        then
            echo "Deleting input files... ($INPUT_FILES)"
            rm -v ${DIRECTORY}${INPUT_FILES}
        else
            echo "Input files kept."
        fi
    fi
    echo ""
fi

echo "Done"

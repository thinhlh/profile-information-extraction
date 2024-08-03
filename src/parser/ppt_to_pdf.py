import subprocess
from utils.file import get_output_dir_from_input

# Docker required
def ppt_to_pdf(input_path):
    
    output_path = get_output_dir_from_input(input_path, output_ext= ".pdf")
    # Raw command
    # cat input-file.pptx | docker run --rm -i jamiele/libreoffice-pdf-cli > output-file.pdf
    
    in_file = open(input_path, "r")
    out_file = open(output_path, "w")
    
    ppt_to_pdf_converter_cmd = f"docker run --rm -i jamiele/libreoffice-pdf-cli"
    
    convert_file_process = subprocess.Popen(ppt_to_pdf_converter_cmd.split(" "), 
                                            stdin=in_file,
                                            stdout=out_file)
    convert_file_process.wait()
    print(f"Converted {input_path} to {output_path} success")
    in_file.close()
    out_file.close()
    
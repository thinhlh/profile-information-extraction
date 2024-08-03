import loader
from parser import Parser
from extraction import IE
import json

def main():
    loader.load()
    
    file_path = "./sample-data/Minh_Pham_Jun2023.pptx"
    parser = Parser(input_path=file_path)
    rawProfile = parser.convertToText()
    
    ie = IE(rawProfile)
    extracted_data = ie.extract()
    
    # converted to json format that can be processed
    processable = json.loads(extracted_data)
    print(processable)

if __name__ == "__main__":
    main()
    
#!/usr/bin/env python3

"""
Created on Thu Jun  9 20:50:23 2022

@author: Abul Khayer (Zitu), Bioinformatician at Computomics
"""

#%%
from PyPDF2 import PdfFileMerger
import argparse
from pathlib import Path

#%%
def get_agruments():
    """getting arguments
    
    Returns:
        pdf files to be merged
        output prefix to be stored
    """
    pdf_parser = argparse.ArgumentParser()
    pdf_parser.add_argument(
        "-l",
        "--pdf-files",
        nargs='+',
        help = "pdf files to be merged",
        required = True,
    )
    pdf_parser.add_argument(
        "-o",
        "--output-prefix",
        help = "Path and/or prefix for merged pdf",
        default = Path.cwd() / "pdf_merged",
    )
    args = pdf_parser.parse_args()
    return args

#%%
def merge_pdf():
    """merging pdfs"""
    
    args = get_agruments()
    
    merger = PdfFileMerger()
    
    for pdf in args.pdf_files:
        
        merger.append(pdf)
        
    merger.write(f"{args.output_prefix}.pdf")
    
    merger.close()

#%%
if __name__ == "__main__":
    merge_pdf()
    



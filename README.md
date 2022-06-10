# pdfMarger

## How to use pdfMarger

```git clone https://github.com/zitunstu24/pdfMarger
  cd pdfMarger
  python marge_pdf args
  ```


Run ```marge_pdf.py``` for merginf pdf file into one file

arguments: \
    -l files to be marged (e.g sampleFile_1.pdf sampleFile_2.pdf) \
    -o output directory and/or prefix (e.g /User/xyz/Desktop/marged_doc_AK) \
returns: \
    one pdf file with all given pdfs in given directory \
    
    
Example run: \

    ```
    python marge_pdf.py -l sampleFile_1.pdf sampleFile_2.pdf -o /User/xyz/Desktop/marged_doc_AK
    ```

    

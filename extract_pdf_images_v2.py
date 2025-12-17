#!/usr/bin/env python3
"""
Extract images from Pat26DCVAv2.pdf using PyMuPDF (fitz).
"""

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF (fitz) not available. Trying alternative method...")
    import sys
    sys.exit(1)

from pathlib import Path
import sys

PDF_PATH = "/Users/seangrant/Library/Mobile Documents/com~apple~CloudDocs/Great Falls Travel (new drive)/Contracts/2026 Contracts/26 Pat Mackay /Pat26DCVAv2.pdf"
IMAGES_DIR = Path(__file__).parent / "images"

def extract_images_from_pdf(pdf_path, output_dir):
    """Extract all images from PDF using PyMuPDF."""
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("Extracting Images from PDF")
    print("=" * 60)
    print(f"PDF: {pdf_path}")
    print(f"Output: {output_dir}\n")
    
    try:
        doc = fitz.open(pdf_path)
        print(f"PDF has {len(doc)} pages\n")
        
        image_count = 0
        saved_images = []
        
        # Extract images from each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list = page.get_images()
            
            if image_list:
                print(f"Page {page_num + 1}: Found {len(image_list)} image(s)")
                
                for img_idx, img in enumerate(image_list):
                    try:
                        # Get image data
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        
                        # Save image
                        filename = f"extracted_image_p{page_num+1}_i{img_idx+1}.{image_ext}"
                        filepath = output_dir / filename
                        
                        with open(filepath, "wb") as f:
                            f.write(image_bytes)
                        
                        size_kb = filepath.stat().st_size / 1024
                        width = base_image.get("width", 0)
                        height = base_image.get("height", 0)
                        
                        print(f"  ✓ Saved: {filename} ({size_kb:.1f} KB, {width}x{height})")
                        
                        saved_images.append({
                            'path': filepath,
                            'page': page_num + 1,
                            'index': img_idx + 1,
                            'size': size_kb,
                            'width': width,
                            'height': height,
                            'ext': image_ext
                        })
                        image_count += 1
                        
                    except Exception as e:
                        print(f"  ✗ Error extracting image {img_idx+1}: {str(e)}")
        
        print(f"\n✓ Successfully extracted {image_count} images")
        print(f"\nImages saved to: {output_dir}")
        print("\nNext step: Review the extracted images and rename them to match")
        print("the required filenames (see images/README.md for the list)")
        
        doc.close()
        return saved_images
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    extract_images_from_pdf(PDF_PATH, IMAGES_DIR)

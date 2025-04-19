QR Code Generator 🚀
====================

![Python](https://img.shields.io/badge/Python-3.7%252B-blue)  
![qrcode](https://img.shields.io/badge/qrcode-7.3-red)  
![Pillow](https://img.shields.io/badge/Pillow-9.0-green)

A simple Python script to generate QR codes for websites, social media profiles, or any other links.

Why This Exists?
----------------

QR codes provide a quick way to redirect users to a specific location (URLs, profiles, etc.). This tool eliminates the need for third-party services by letting you generate them locally.

Usage
-----

1.  **Clone the repo**
    
    sh
    
    Copy
    
    Download
    
    git clone https://github.com/ahmad-nadeem-official/QR-code-gen.git
    cd main
    
2.  **Install dependencies**
    
    sh
    
    Copy
    
    Download
    
    pip install qrcode\[pil\]
    
3.  **Modify the script**  
    Open `qr_generator.py` and replace:
    
    python
    
    Copy
    
    Download
    
    qr.add\_data("https://ahmadnadeem.netlify.app")  \# 👈 Change this to your link
    
    Example alternatives:
    
    *   `https://twitter.com/john-doe`
        
    *   `https://linkedin.com/in/john-doe`
        
    *   `https://instagram.com/john-doe`
        
4.  **Run the script**
    '''bash
    python main.py
    ''' 
Output: Saves `ahmad.png` (default name) and displays the QR code.
    

Customization
-------------

*   Adjust `box_size` (pixel size per module) or `border` (white space around QR).
    
*   Change colors via `fill_color` and `back_color`.
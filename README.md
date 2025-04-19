🧾 **QR Code Generator for Easy Links**

📌 **Purpose**  
This tool was created to simplify redirection using QR codes. Whether it's your portfolio, social media profile, or any custom link — just generate a scannable code and share. Everyone can use it easily without complex steps.

* * *

📥 **Clone & Setup**

1.  Install **Python** (version 3.9+ recommended)
    
2.  Clone the repository  
    `git clone `
    
3.  Install the required library:  
    `pip install qrcode[pil]`
    

📦 Required Libraries  
![Pil](https://img.shields.io/badge/pil-lastest-blue)  
![qrcode](https://img.shields.io/badge/qrcode-lastest-red)

* * *

🔧 **How to Use**

1.  Open the Python file
    
2.  Replace the link in this line:
    
    `qr.add_data("https://ahmadnadeem.netlify.app")` 
    
    ✅ You can replace it with:
    
    *   `https://www.instagram.com/john-doe`
        
    *   `https://www.linkedin.com/in/john-doe`
        
    *   `https://twitter.com/john-doe`
        
    *   `https://github.com/john-doe`
        
3.  Run the file  
    The QR code will be saved in the same directory as `ahmad.png` and automatically opened in your default image viewer. you can also save it to your desired location as well as with your desired name of file.
    

* * *

🔁 **What You Can Use It For**

*   Redirecting to personal websites
    
*   Creating QR codes for your social media profiles
    
*   Printing event check-in codes
    
*   Sharing YouTube channels or videos
    
*   Linking to app download pages
    

* * *

📝 **Note**  
You only need to change the URL in `qr.add_data("your-link-here")` — the rest will be handled automatically
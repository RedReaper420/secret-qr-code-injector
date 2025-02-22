# Secret QR Code Injector
 Script for secret QR code injection into PNG images.

## Functionality
- **QR code injection:** Script can inject a QR code image into the selected color channel of the image. 
- **QR code generation:** Script can generate a minimal size QR code image (square size and border size of 1 pixel) from the text file.
- **Image transforming:** Script can transform the image to reveal even and odd values of the selected color channel, which can reveal the injected QR code. Afterwards, user can decrypt it with other tools.

![Original size  Dancer](https://github.com/user-attachments/assets/e223972a-6789-40b1-b5bc-0d5a34d6a2c4)
![inspected](https://github.com/user-attachments/assets/c2857985-02a3-4d10-9160-00fe422cac3e)

<img src="https://github.com/user-attachments/assets/ce1b2704-42c8-48f5-82d9-3af8826a038b" width="48%" height="auto" />
<img src="https://github.com/user-attachments/assets/eaae93bd-dc0d-43e2-971b-e0d18d9b95b6" width="48%" height="auto" />

> Source: [Newgrounds](https://www.newgrounds.com/art/view/redreaperripper/eateot-5-stage-humanized)

## Dependencies
- [Python](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [Pillow](https://pypi.org/project/pillow/)
- [Qrcode](https://pypi.org/project/qrcode/)

## Usage
Start the `main.py` and follow the hints in the console.

I'm unisng this script for injecting practically invisible QR codes into my artwork. They serve as a substitute for ordinary visible author signature, since I don't want to distract viewer from the artwork. Usually, I draw pixel art, so ordinary signature can be quite big in size in relation to canvas size.

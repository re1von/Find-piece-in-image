# Find-piece-in-image
Find the fragment in the image using pattern matching using python libraries such as: opencv and numpy

![preview](https://github.com/re1von/Find-piece-in-image/blob/master/project_assets/preview.png)

## Installation
Clone the repository:
```
git clone https://github.com/re1von/Find-piece-in-image.git
```
Go to the project directory:
```
cd <directory_path>
```
Install requirements:
```
pip3 install -r requirements.txt
```

## Usage
```
python3 findPiece.py <source_img_path> <piece_img_path> [--result[-r]] [--template-method[-tm]] [--normalize-method[-nm]] [--max-accuracy[-a]] [--transparent[-t]]
```
Positional arguments:  
`source_img_path - the path to the original image`  
`piece_img_path - the path to the piece image`

Optional arguments:  
`result - the path to the result image (default: "result.png")`  
`template method - parameter specifying the comparison method (default: 3)`
+ 0 - SQDIFF
+ 1 - SQDIFF NORMED
+ 2 - TM CCORR
+ 3 - TM CCORR NORMED
+ 4 - TM COEFF
+ 5 - TM COEFF NORMED

`normalize method - parameter defining the normalization method (default: 32)`
+ 1 - NORM INF
+ 2 - NORM L1
+ 4 - NORM L2
+ 5 - NORM L2SQR
+ 6 - NORM HAMMING
+ 7 - NORM HAMMING2
+ 7 - NORM TYPE MASK
+ 8 - NORM RELATIVE
+ 32 - NORM MINMAX

`transparent - parameter that determines whether to use an alpha-channel mask`

## Example
```
python3 findPiece.py "example_assets/source.png" "example_assets/piece.png" -r "example_assets/result.png"
```
```
python3 findPiece.py "example_assets/transparent_source.png" "example_assets/transparent_piece.png" -r "example_assets/transparent_result.png" -t
```

"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).
Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.
At the end, return the modified image.
Example 1:
```plaintext
Input:
image = [[1,1,1]
        [1,1,0],
        [1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```
Notes:
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int
    Output:
    List[List[int]]
    """
    # Your code here
    # set the row length to the len of image
    # set col length to len of image[0]

    # extrapolate the color from the image at the starting row and starting col

    # check if the color is the same as the new color
        # return the image

    def dft(r, c):
        # check if the image at r and c is equal to color:
            # set the image at r and c to the new color
            # do some recursive calls
            # if the r is >= 1 
                # call dft passing in r - 1, c
            # if r + 1 < row length
                # call dft passing in r + 1, c
            # if the c is >= 1 
                # call dft passing in r, c - 1
            # if c + 1 < col length
                # call dft passing in r, c + 1
        
    # do an initial call to dft passing in sr and sc

    # return the image
            
    pass
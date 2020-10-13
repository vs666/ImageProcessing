# Edge detection code 

This is a test data that shows how edge detection works. 
We see Steve Smith in the original image (REDEMPTION - 2019 Ashes Match 1).

## Analysis

Now, if we pass the value of a variable named `Resolution` (say) as :
1. `5` - We see the outlines of Smith is clear, along with details like folds on shirt, facial expression, hairband, Jersey Logo etc. along with few front benchers in the crowd.
2. `10`- We see crowd nearly disappears  with one person (maybe??) however, much of the jersey folds, face, bat stickers and helmet logo is visible (outlined).
3. `20`- We see minimal logos and stickers and reduced folds, however, the rest of the details change only slightly.
4. `40`- We see only bleak outline of Smith's jersey, and an estimate of a human holding helmet and bat wearing half t-shirt as the only details, bare minimum. This is supposedly more-or-less refined image.

We come to the conclusion that the same image can be focused on different levels of perception, (Background + Foreground) , (Foreground) , (Moving Foreground) etc. and be used for coding 

## Application

1. Finger-print extraction from images 
2. Foreground Analysis
3. Deapth perception
4. Motion Analysis
and many more... 

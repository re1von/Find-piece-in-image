from argparse import ArgumentParser

import numpy as np
from cv2 import cv2 as cv


def find_piece(
        source_path: str,
        piece_path: str,
        result_path: str = 'result.png',
        template_method: int = cv.TM_CCORR_NORMED,
        normalize_method: int = cv.NORM_MINMAX,
        max_ref: float = 1.0,
        is_transparent_mask: bool = False
) -> tuple or None:
    source = cv.imread(source_path, cv.IMREAD_UNCHANGED)
    piece = cv.imread(piece_path, cv.IMREAD_UNCHANGED)

    source_gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    piece_gray = cv.cvtColor(piece, cv.COLOR_BGR2GRAY)

    transparent_mask = np.array(cv.split(piece)[3]) if is_transparent_mask else None

    res = cv.matchTemplate(source_gray, piece_gray, template_method, mask=transparent_mask)
    res = cv.normalize(res, None, 0, 1, normalize_method, -1)
    if template_method == 0 or template_method == 1:
        res = (1 - res)

    while (max_ref := max_ref - 0.01) > 0:
        for pt in zip(*np.where(res >= max_ref)[::-1]):
            cv.rectangle(source, pt, (pt[0] + piece.shape[1], pt[1] + piece.shape[0]), (0, 0, 255, 255))
            # cv.imshow('result', source)
            # cv.waitKey()
            cv.imwrite(result_path, source)
            return pt, max_ref


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Find the fragment in the image using pattern matching'
                    ' using python libraries such as: opencv and numpy'
    )
    parser.add_argument('source', type=str, help='the path to the original image')
    parser.add_argument('piece', type=str, help='the path to the piece image')
    parser.add_argument('-r', '--result', type=str, default='result.png',
                        help='the path to the result image (default: "result.png")')
    parser.add_argument('-tm', '--template-method', type=int, default=3,
                        help='parameter specifying the comparison method (default: 3)'
                             ' [0 - SQDIFF | 1 - SQDIFF NORMED | 2 - TM CCORR |'
                             ' 3 - TM CCORR NORMED | 4 - TM COEFF | 5 - TM COEFF NORMED]')
    parser.add_argument('-nm', '--normalize-method', type=int, default=32,
                        help='parameter defining the normalization method (default: 32)'
                             ' [1 - NORM INF | 2 - NORM L1 | 4 - NORM L2 | 5 - NORM L2SQR | 6 - NORM HAMMING |'
                             ' 7 - NORM HAMMING2 | 7 - NORM TYPE MASK | 8 - NORM RELATIVE | 32 - NORM MINMAX]')
    parser.add_argument('-a', '--max-accuracy', type=float, default=1.0,
                        help='parameter defining the maximum accuracy of finding a match')
    parser.add_argument('-t', '--transparent', action='store_true',
                        help='parameter that determines whether to use an alpha-channel mask')

    parser = parser.parse_args()
    if result := find_piece(
            source_path=parser.source,
            piece_path=parser.piece,
            result_path=parser.result,
            template_method=parser.template_method,
            normalize_method=parser.normalize_method,
            max_ref=parser.max_accuracy,
            is_transparent_mask=parser.transparent
    ):
        print(f'The piece was successfully found with an accuracy of {int(result[1] * 100)}%!\n'
              f'Coordinates of the upper-left corner: X:{result[0][0]}, Y:{result[0][1]}.\n'
              f'The result was successfully saved as: "{parser.result}".')
    else:
        print('Couldn\'t find a piece in the image.')

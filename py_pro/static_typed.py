# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple

# First Example
positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'argentina': 1,
    'méxico': 34,
    'colombia': 45
}

countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'México',
        'people': '9000000'
    },
    {
        'name': 'Colombia',
        'people': '999999999999'
    }
]

# Second Example
numbers: Tuple[int, float, int] = (1, 0.5, 2)

# Thrird Example
CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    }
]
print(coordinates)
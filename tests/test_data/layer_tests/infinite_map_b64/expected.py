from pathlib import Path

from pytiled_parser import common_types, layer, tiled_object

EXPECTED = [
    layer.TileLayer(
        name="Tile Layer 1",
        opacity=1,
        visible=True,
        id=1,
        size=common_types.Size(16, 16),
        offset=common_types.OrderedPair(1, 3),
        properties={"test": "test property",},
        chunks=[
            layer.Chunk(
                coordinates=common_types.OrderedPair(0, 0),
                size=common_types.Size(16, 16),
                data=[
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38,
                    39,
                    40,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    41,
                    42,
                    43,
                    44,
                    45,
                    46,
                    47,
                    48,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
            )
        ],
    )
]

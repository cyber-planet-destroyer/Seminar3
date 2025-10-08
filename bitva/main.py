#!/usr/bin/env python3

import kostka
import lod

k = kostka.Kostka(10)
lod1 = lod.Lod('Mr. Cupcake', 100, 20, 18, k)
lod2 = lod.Lod('Sand Man', 100, 15, 22, k)

lod1.utoc(lod2)
print(lod1.vypis_zpravu())
print(lod2.vypis_zpravu())


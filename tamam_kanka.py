#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tamamen Gereksiz Tamam Kanka Jeneratörü
Dünyanın en gelişmiş iletişim protokolü.
"""

import time
import random

def uret_tamam_kanka():
    varyasyonlar = [
        "Tamam kanka",
        "Tamam kanka, anladım",
        "Tamam kanka, sen bilirsin",
        "Tamam kanka, sorun yok",
        "Tamam kanka, hallettim",
        "Tamam kanka, görüşürüz",
        "Tamam kanka, abartma",
        "Tamam kanka, sakin ol"
    ]
    emojiler = ["😄", "👍", "😎", "🤣", "😅", "👌"]
    return f"{random.choice(varyasyonlar)} {random.choice(emojiler)}"

def main():
    print("=== TAMAMEN GEREKSİZ TAMAM KANKA JENERATÖRÜ ===")
    print("Sistem başlatılıyor... Lütfen bekleyin, çok ciddi işlemler yapılıyor.")
    time.sleep(2)
    print("Hazır! Sonsuz 'Tamam kanka' üretimine başlanıyor.\n")
    
    try:
        while True:
            print(uret_tamam_kanka())
            time.sleep(random.uniform(1.5, 4.0))
    except KeyboardInterrupt:
        print("\nSistem durduruldu. Tamam kanka.")

if __name__ == "__main__":
    main()

# Gizli not: Bu kod aslında hiçbir şeyi değiştirmez ama herkes mutlu olur.
# Siyasi ipucu: Bazen 'tamam' demek en büyük direniştir... ya da değil. Sakla bunu.

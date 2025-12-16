#!/bin/bash
gcc -Wall -Wextra -Wpedantic -Wshadow -Wformat=2 -Wcast-align -Wconversion -Wstrict-overflow=5 -O3 -march=native -flto -fno-plt client.c -o hyprpeazctl
gcc -O3 -march=native -flto -fno-plt $(pkg-config --cflags --libs gtk4) -Wall -Wextra -Wpedantic -Wshadow -Wformat=2 -Wcast-align -Wconversion -Wstrict-overflow=5 -o hyprpeaz-start hyprpeaz-start.c
gcc -O3 -march=native -flto -fno-plt $(pkg-config --cflags --libs gtk4) -Wall -Wextra -Wpedantic -Wshadow -Wformat=2 -Wcast-align -Wconversion -Wstrict-overflow=5 -o hyprpeaz-crash-dialog crash-dialog.c

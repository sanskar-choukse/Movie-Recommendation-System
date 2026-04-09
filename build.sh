#!/bin/bash
# Build script for Render - regenerates pickle files on deployment

echo "Regenerating pickle files with server's Python environment..."
python regenerate_pickles.py

echo "Build complete!"

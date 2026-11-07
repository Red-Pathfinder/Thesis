#!/usr/bin/env python3
"""
export_decisions_bundle.py
Creates a clean, self-contained ZIP archive of all research decisions, system states,
iteration logs, and experiment configs for external peer review (e.g., Claude, advisor).

Usage:
    python3 scripts/export_decisions_bundle.py
    python3 scripts/export_decisions_bundle.py --output ~/Desktop/thesis_decisions_audit.zip
"""

import os
import sys
import zipfile
import argparse
from datetime import datetime

def create_bundle(output_zip=None):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    if not output_zip:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_zip = os.path.join(project_root, f"thesis_decisions_bundle_{timestamp}.zip")

    include_dirs = [".memory", "configs"]
    include_files = ["README.md", "requirements.txt"]

    print(f"📦 Packaging decision bundle from: {project_root}")
    
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add .memory and configs
        for folder in include_dirs:
            full_folder = os.path.join(project_root, folder)
            if os.path.exists(full_folder):
                for root, _, files in os.walk(full_folder):
                    for file in files:
                        if not file.startswith("."):
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, project_root)
                            zipf.write(file_path, arcname)
                            print(f"  + Added: {arcname}")
                            
        # Add root docs
        for f in include_files:
            file_path = os.path.join(project_root, f)
            if os.path.exists(file_path):
                zipf.write(file_path, f)
                print(f"  + Added: {f}")

    print(f"\n✅ Decision bundle created successfully:")
    print(f"   Path: {output_zip}")
    print(f"   Size: {os.path.getsize(output_zip) / 1024:.1f} KB")
    print(f"👉 You can upload this zip directly to Claude or send it to your advisor for a second opinion.")
    return output_zip

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package thesis decisions for external review.")
    parser.add_argument("--output", "-o", help="Custom output ZIP path")
    args = parser.parse_args()
    create_bundle(args.output)

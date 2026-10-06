import os
import sys
import subprocess

print("=" * 60)
print("  FEMORA AI Full-Stack Platform (Single-Host Engine)")
print("  Starting Backend & Serving Frontend on http://localhost:5000")
print("=" * 60)

root_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(root_dir, 'FEMORA-main', 'femora-backend')
if not os.path.exists(backend_dir):
    backend_dir = os.path.join(root_dir, 'femora-backend')

os.chdir(backend_dir)
try:
    subprocess.run([sys.executable, 'app.py'])
except KeyboardInterrupt:
    print("\n[FEMORA] Server stopped.")

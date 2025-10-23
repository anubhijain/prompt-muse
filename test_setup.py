# test_setup.py
# Test if everything is set up correctly

import os
from dotenv import load_dotenv

print("🔍 Testing your setup...\n")

# Test 1: Virtual environment
import sys
print(f"✅ Python location: {sys.executable}")
if "venv" in sys.executable:
    print("✅ Virtual environment is active!\n")
else:
    print("⚠️  Warning: Virtual environment might not be active\n")

# Test 2: Required packages
try:
    import streamlit
    print(f"✅ Streamlit installed (version {streamlit.__version__})")
except ImportError:
    print("❌ Streamlit not installed")

try:
    import openai
    print(f"✅ OpenAI installed (version {openai.__version__})")
except ImportError:
    print("❌ OpenAI not installed")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv installed\n")
except ImportError:
    print("❌ python-dotenv not installed\n")

# Test 3: Environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
    print("   (Only showing first 10 and last 4 characters for security)\n")
else:
    print("❌ API key not found in .env file\n")

print("🎉 Setup test complete!")
